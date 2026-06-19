from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="CloudLabs AI Proctor API",
    version="0.1.0"
)


class ChatRequest(BaseModel):
    user_message: str
    lab_id: str | None = None
    lab_name: str | None = None
    exercise: str | None = None
    task: str | None = None
    step: str | None = None


@app.get("/")
def root():
    return {
        "message": "CloudLabs AI Proctor API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "answer": f"I received your question: {request.user_message}",
        "lab_id": request.lab_id,
        "lab_name": request.lab_name,
        "exercise": request.exercise,
        "task": request.task,
        "step": request.step
    }