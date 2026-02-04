import streamlit as st
import requests

st.set_page_config(page_title="AI Agent Chatbot", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.title("Agent Configuration")

provider = st.sidebar.selectbox(
    "Model Provider",
    ["groq", "openai"]
)

model = st.sidebar.selectbox(
    "Model",
    ["llama3-70b-8192", "gpt-4o-mini"]
)

system_prompt = st.sidebar.text_area(
    "System Prompt",
    "act as friend"
)

allow_search = st.sidebar.checkbox("Enable Web Search")

# ---------- MAIN ----------
st.title("AI Agent Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type here...")

if user_input:
    # show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # ✅ PAYLOAD MUST BE DEFINED
    payload = {
        "provider": provider,
        "model": model,
        "system_prompt": system_prompt,
        "query": user_input,
        "allow_search": allow_search,
        "chat_history": st.session_state.messages
    }

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json=payload,
                timeout=120
            )

            answer = response.json()["response"]
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )


