"""
http://API.py - SuiAutoforge Project

This module sets up a FastAPI application that provides an endpoint for generating
Sui Move smart contracts based on user prompts. It uses the chatbot functionality from
http://chatbot.py to generate contract logic and the contract_generator module to create the final contract.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatbot import get_sui_contract
from contract_generator import load_template, generate_contract

app = FastAPI()

# Pydantic model to validate incoming request bodies.
class ContractPrompt(BaseModel):
    prompt: str

@app.post("/generate-contract")
async def generate_contract_endpoint(request: ContractPrompt):
    try:
        # Generate contract logic from the provided prompt.
        generated_logic = get_sui_contract(request.prompt)
        if not generated_logic or generated_logic.startswith("Error"):
            raise ValueError("Failed to generate contract logic")
        
        # Load the Sui Move template.
        template = load_template("sui_template.move")
        if template is None:
            raise FileNotFoundError("Template file not found")
        
        # Generate the final contract by injecting the generated logic.
        final_contract = generate_contract(template, generated_logic)
        return {"contract": final_contract}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except FileNotFoundError as fe:
        raise HTTPException(status_code=404, detail=str(fe))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred: " + str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)