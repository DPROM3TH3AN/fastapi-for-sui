from fastapi import APIRouter, HTTPException, FastAPI
from pydantic import BaseModel
from chatbot import get_chatbot_response
from contract_generator import generate_contract

router = APIRouter()

class GenerationRequest(BaseModel):
    prompt: str

class GenerationResponse(BaseModel):
    contract_code: str
    message: str

@router.post("/generate_contract", response_model=GenerationResponse)
async def generate_smart_contract(request: GenerationRequest):
    try:
        chatbot_response = get_chatbot_response(request.prompt)
        contract_code = generate_contract(chatbot_response)
        return GenerationResponse(contract_code=contract_code, message="Contract generated successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app = FastAPI()

app.include_router(router)