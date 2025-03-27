"""
http://API.py - SuiAutoforge Project

This module sets up a FastAPI application that provides an endpoint for generating
Sui Move smart contracts based on user prompts. It uses the chatbot functionality
from http://chatbot.py and the contract generator to produce the final contract.
"""
from fastapi import APIRouter, HTTPException, FastAPI
from pydantic import BaseModel
from chatbot import get_sui_contract  # Ensure this function returns the generated logic string
from contract_generator import load_template, generate_contract

app = FastAPI()

class ContractPrompt(BaseModel):
    prompt: str

@app.post("/generate-contract")
async def generate_contract_endpoint(request: ContractPrompt):
    # Generate the contract logic from the chatbot using the provided prompt.
    generated_logic = get_sui_contract(request.prompt)
    if not generated_logic or generated_logic.startswith("Error"):
        raise HTTPException(status_code=500, detail="Failed to generate contract logic")
    
    # Load the Sui Move template from the current directory.
    template = load_template("sui_template.move")
    if template is None:
        raise HTTPException(status_code=500, detail="Template file not found")
    
    # Inject the generated logic into the template.
    final_contract = generate_contract(template, generated_logic)
    
    return {"contract": final_contract}
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)"""