import subprocess
import sys
import time
import os
from dotenv import load_dotenv

# 🔥 LOAD .env HERE
load_dotenv()

ENV = os.environ.copy()

def run_backend():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "main:app",
            "--host",
            "127.0.0.1",
            "--port",
            "8000",
            "--workers",
            "1",
        ],
        env=ENV  # 🔥 PASS ENVIRONMENT
    )

def run_frontend():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "frontend/streamlit_app.py",
            "--server.port",
            "8502",
        ],
        env=ENV
    )

if __name__ == "__main__":
    print("🚀 Starting FastAPI backend...")
    backend = run_backend()

    time.sleep(3)

    print("🎨 Starting Streamlit frontend...")
    frontend = run_frontend()

    backend.wait()
    frontend.wait()
