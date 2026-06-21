from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.classifier_service import classify_question
from backend.services.search_service import search_knowledge_base
from backend.services.ai_service import generate_response
from backend.services.session_service import add_message, get_session
from backend.services.session_service import add_message, get_session, clear_session

app = FastAPI(title="CloudLabs AI Proctor API")


class ChatRequest(BaseModel):
    user_message: str
    session_id: str | None = "default"

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
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    session_id = request.session_id or "default"

    # Save user message
    add_message(session_id, "user", request.user_message)

    # Classify question
    question_type = classify_question(request.user_message)

    # Search KB
    kb_result = search_knowledge_base(
        request.user_message,
        question_type
    )

    # Generate response
    ai_answer = generate_response(
        request.user_message,
        kb_result["content"]
    )

    # Save assistant response
    add_message(session_id, "assistant", ai_answer)

    return {
        "session_id": session_id,
        "question_type": question_type,
        "answer": ai_answer,
        "source": kb_result["source"],
        "found": kb_result["found"],
        "history": get_session(session_id),

        "lab_id": request.lab_id,
        "lab_name": request.lab_name,
        "exercise": request.exercise,
        "task": request.task,
        "step": request.step
    }

@app.delete("/session/{session_id}")
def delete_session(session_id: str):
    clear_session(session_id)
    return {
        "message": f"Session {session_id} cleared successfully"
    }

@app.get("/version")
def version():
    return {
        "name": "CloudLabs AI Proctor API",
        "version": "1.0.0",
        "status": "running"
    }