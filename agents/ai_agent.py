from langgraph.prebuilt import create_react_agent
from agents.llm_provider import get_llm

def get_response(payload):
    try:
        tools = []
        llm = get_llm(payload["provider"], payload["model"])

        agent = create_react_agent(llm, tools)

        messages = payload.get("chat_history", [])
        messages.append(("user", payload["query"]))

        result = agent.invoke({"messages": messages})

        return result["messages"][-1].content

    except Exception as e:
        # 🚨 backend never crash
        return f"Backend agent error: {str(e)}"
