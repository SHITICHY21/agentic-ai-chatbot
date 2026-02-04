from langchain.tools import tool
from tavily import TavilyClient

@tool
def web_search(query: str):
    """
    Search the web using Tavily and return relevant information.
    """
    client = TavilyClient()
    result = client.search(query)
    return result
