from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models import ChatRequest

from backend.services.classifier_service import classify_question
from backend.services.search_service import search_knowledge_base
from backend.services.ai_service import generate_response
from backend.services.session_service import (
    add_message,
    get_session,
    clear_session
)

from backend.utils.validators import validate_chat_request

from backend.routes import upload
from backend.routes import feedback
from backend.routes import escalate
from backend.routes import health
from backend.routes import chat as chat_routes
from backend.routes import admin


app = FastAPI(
    title="CloudLabs AI Proctor API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(escalate.router, prefix="/escalate", tags=["Escalation"])
app.include_router(health.router, prefix="/route-health", tags=["Health"])
app.include_router(chat_routes.router, prefix="/route-chat", tags=["Chat"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])


@app.get("/")
def root():
    return {
        "message": "CloudLabs AI Proctor API is running",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "name": "CloudLabs AI Proctor API",
        "version": "1.0.0",
        "status": "running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    validation = validate_chat_request(request.user_message)

    if not validation["valid"]:
        return {
            "error": validation["error"],
            "session_id": request.session_id
        }

    session_id = request.session_id or "default"

    add_message(session_id, "user", request.user_message)

    question_type = classify_question(request.user_message)

    kb_result = search_knowledge_base(
        request.user_message,
        question_type,
        request.lab_id
    )

    history = get_session(session_id)

    ai_answer = generate_response(
        request.user_message,
        kb_result["content"],
        history
    )

    add_message(session_id, "assistant", ai_answer)

    return {
        "session_id": session_id,
        "question_type": question_type,
        "answer": ai_answer,
        "source": kb_result["source"],
        "found": kb_result["found"],
        "score": kb_result.get("score", 0),
        "history": get_session(session_id),
        "lab_context": {
            "lab_id": request.lab_id,
            "lab_name": request.lab_name,
            "exercise": request.exercise,
            "task": request.task,
            "step": request.step
        }
    }


@app.delete("/session/{session_id}")
def delete_session(session_id: str):

    clear_session(session_id)

    return {
        "message": f"Session '{session_id}' cleared successfully."
    }