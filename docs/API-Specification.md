# CloudLabs AI Proctor API Specification

## Overview

CloudLabs AI Proctor exposes RESTful APIs through a FastAPI backend to support AI-powered troubleshooting, feedback collection, analytics logging, health monitoring, and administrative operations.

---

# Base URL

```
http://localhost:8000
```

Production:

```
https://<app-name>.azurewebsites.net
```

---

# Authentication

Current MVP:

- No authentication required.

Future versions will support:

- Azure Active Directory
- OAuth 2.0
- JWT Authentication

---

# API Endpoints

## Health Check

### GET /health

Returns application health status.

### Response

```json
{
  "status": "healthy",
  "service": "CloudLabs AI Proctor"
}
```

---

## Chat

### POST /chat

Generates an AI troubleshooting response.

### Request

```json
{
  "session_id": "session-001",
  "user_message": "VM is not loading",
  "lab_id": "fabric",
  "lab_name": "Fabric IQ",
  "exercise": "Exercise 2",
  "task": "Task 3",
  "step": "Step 5"
}
```

### Response

```json
{
  "answer": "The VM may still be provisioning. Wait 2–3 minutes and refresh the lab.",
  "source": "knowledge-base/vm-loading.md",
  "score": 4.8
}
```

---

## Feedback

### POST /feedback

Stores user feedback for an AI response.

### Request

```json
{
  "session_id": "session-001",
  "user_message": "VM is not loading",
  "answer": "Wait 2–3 minutes.",
  "rating": 1
}
```

### Response

```json
{
  "message": "Feedback saved successfully."
}
```

---

### GET /feedback

Returns all stored feedback.

### Response

```json
[
  {
    "session_id": "session-001",
    "rating": 1
  }
]
```

---

## Upload

### POST /upload

Uploads Markdown documentation into the knowledge base.

### Supported Files

- Markdown (.md)
- Text (.txt)

### Response

```json
{
  "message": "Knowledge base updated."
}
```

---

## Admin

### GET /admin

Returns application statistics.

### Response

```json
{
  "total_sessions": 28,
  "total_feedback": 19,
  "average_rating": 4.6
}
```

---

## Escalation

### POST /escalate

Escalates unresolved issues to a human administrator.

### Request

```json
{
  "session_id": "session-001",
  "reason": "AI confidence too low"
}
```

### Response

```json
{
  "message": "Issue escalated successfully."
}
```

---

# HTTP Status Codes

| Code | Meaning |
|------|---------|
|200|Success|
|201|Created|
|400|Bad Request|
|401|Unauthorized|
|404|Resource Not Found|
|422|Validation Error|
|500|Internal Server Error|

---

# Error Response Format

```json
{
    "detail": "Validation failed."
}
```

---

# Interactive API Documentation

FastAPI automatically exposes Swagger UI.

```
/docs
```

Alternative OpenAPI documentation:

```
/redoc
```

---

# Future API Enhancements

- Authentication
- User profiles
- Conversation history
- Azure AI Search integration
- Streaming responses
- Batch knowledge ingestion
- Admin dashboard APIs
