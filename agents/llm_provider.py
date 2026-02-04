import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

def get_llm(provider: str, model: str):
    if provider == "openai":
        return ChatOpenAI(
            model=model,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    if provider == "groq":
        return ChatGroq(
            model=model,
            api_key=os.getenv("GROQ_API_KEY")
        )

    raise ValueError("Unsupported provider")
