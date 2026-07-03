# CloudLabs AI Proctor Data Flow

## Overview

CloudLabs AI Proctor processes user queries through a Retrieval-Augmented Generation (RAG)-style workflow. The application combines Azure OpenAI with a curated knowledge base to generate contextual troubleshooting responses for CloudLabs learners.

---

## End-to-End Data Flow

```
User
  │
  │
  ▼
React Frontend
  │
  │ REST API Request
  ▼
FastAPI Backend
  │
  ├──────────────► Session Service
  │                    │
  │                    ▼
  │              Load Session Context
  │
  ├──────────────► Search Service
  │                    │
  │                    ▼
  │           Search Knowledge Base
  │
  ├──────────────► Classifier Service
  │                    │
  │                    ▼
  │         Identify Issue Category
  │
  ├──────────────► Azure OpenAI
  │                    │
  │                    ▼
  │          Generate AI Response
  │
  ├──────────────► Logger Service
  │                    │
  │                    ▼
  │           Save Analytics Events
  │
  ├──────────────► Feedback Service
  │                    │
  │                    ▼
  │          Store User Feedback
  │
  ▼
Return Response
  │
  ▼
React Frontend
```

---

## Processing Steps

### Step 1 – User Query

The learner enters a troubleshooting question using the CloudLabs AI Proctor chat interface.

Example:

```
VM is not loading.
```

---

### Step 2 – Session Context

The backend loads the active lab session, including:

- Lab Name
- Exercise
- Task
- Step
- Previous conversation history

This provides context-aware assistance throughout the lab.

---

### Step 3 – Knowledge Search

The Search Service searches the local knowledge base to identify the most relevant documentation.

Typical sources include:

- Lab guides
- Troubleshooting documents
- Azure documentation
- Microsoft Fabric guidance

The highest-scoring result is selected.

---

### Step 4 – Issue Classification

The classifier identifies the category of the issue.

Examples include:

- VM Issues
- Login Problems
- Azure Portal Errors
- Data Agent Issues
- Lab Validation Failures

---

### Step 5 – AI Response Generation

Azure OpenAI receives:

- User question
- Retrieved knowledge
- Session context

The model generates a contextual troubleshooting response.

---

### Step 6 – Analytics Logging

Each interaction records:

- Timestamp
- User query
- Retrieved source
- Confidence score
- Response time
- Session identifier

These analytics support reporting and future improvements.

---

### Step 7 – Feedback Collection

Users can rate AI responses as:

- 👍 Helpful
- 👎 Not Helpful

Feedback is stored for quality evaluation and continuous knowledge base improvement.

---

## Data Storage

The MVP stores information using lightweight JSON files.

| Data | Storage |
|------|---------|
| Events | analytics/events.json |
| Feedback | analytics/feedback.json |
| Sessions | In-memory session service |
| Knowledge Base | Markdown files |

---

## Security Considerations

- Azure OpenAI credentials are stored using environment variables.
- API keys are never exposed to the frontend.
- Sensitive information is processed only by the backend.
- Communication between frontend and backend occurs through REST APIs.

---

## Future Enhancements

Future versions may include:

- Azure AI Search
- Vector embeddings
- Cosmos DB
- Azure Blob Storage
- User authentication
- Multi-tenant support
- Real-time monitoring
