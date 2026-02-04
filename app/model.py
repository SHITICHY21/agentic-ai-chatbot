from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    provider: str
    model: str
    system_prompt: str
    query: str
    allow_search: bool
    chat_history: List[dict]
