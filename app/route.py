from fastapi import APIRouter
from app.model import ChatRequest
from agents.ai_agent import get_response

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest):
    try:
        answer = get_response(req.dict())
        return {"response": answer}
    except Exception as e:
        return {"response": f"API error: {e}"}
