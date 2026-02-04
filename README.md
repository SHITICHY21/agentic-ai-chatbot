# 🤖 Agentic AI Chatbot

**FastAPI + Streamlit + Groq and OpenAI powered Agentic Chatbot**

An end-to-end **Agentic AI Chatbot** that combines a **FastAPI backend** with a **Streamlit frontend**, supporting multiple LLM providers (OpenAI & Groq) with optional web search via Tavily. The project is designed with a **clean, modular, production-ready architecture** and can be run locally with a single command.


▶️ **Agentic AI Chatbot – Live Demo**

> Upload your demo video (`Demo Chatbot.mp4`) directly in the GitHub README editor.
> GitHub will automatically embed the video player here.
> 
[![Demo Video](https://img.shields.io/badge/Click%20to-Watch%20Demo-blue?style=for-the-badge)](
https://github.com/SHITICHY21/agentic-ai-chatbot/blob/main/Demo%20Chatbot.mp4
)

https://github.com/SHITICHY21/agentic-ai-chatbot/blob/main/Demo%20Chatbot.mp4


## ✨ Features

* 🧠 Agentic reasoning using **LangChain** & **LangGraph**
* 🔌 Multiple LLM providers:
  * OpenAI (GPT models)
  * Groq (LLaMA-3 models)
* 🌐 Optional Web Search (Tavily API)
* ⚡ FastAPI backend (REST API)
* 🎨 Streamlit interactive chat UI
* 🚀 One-command startup (Backend + Frontend together)
* 🔐 Secure API key handling using environment variables

## 🧱 Project Structure

```
agentic_chatbot/
│
├── agents/
│   ├── ai_agent.py          # LangGraph agent logic
│   ├── llm_provider.py      # OpenAI / Groq provider selection
│   └── tools.py             # Optional tools (web search, etc.)
│
├── app/
│   ├── route.py             # FastAPI routes
│   ├── model.py             # Pydantic request/response models
│   └── config.py            # Environment configuration
│
├── frontend/
│   └── streamlit_app.py     # Streamlit UI
│
├── main.py                  # FastAPI entry point
├── run_app.py               # One-command launcher (backend + frontend)
├── requirements.txt
├── .env.example
└── README.md
```
## 🛠️ Tech Stack

* **Backend**: FastAPI, Uvicorn
* **Frontend**: Streamlit
* **LLM Framework**: LangChain, LangGraph
* **Models**: OpenAI, Groq (LLaMA-3)
* **Web Search**: Tavily API
* **Language**: Python 3.11

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/agentic-ai-chatbot.git
cd agentic-ai-chatbot
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

### 🚀 One-Command Run (Recommended)

```bash
python run_app.py
```
Will start:

* **FastAPI backend** → [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **Streamlit frontend** → [http://localhost:8501](http://localhost:8501)

## 👥 Contributors

## Shiti Chowdhury
- 🎓 Department: Computer Science & Engineering (CSE), CUET  
- 🔗 GitHub: [SHITICHY21](https://github.com/SHITICHY21)

## Adnan Faisal
- 🎓 Department: Computer Science & Engineering (CSE), CUET  
- 🔗 GitHub: [AJFaisal002](https://github.com/AJFaisal002)





