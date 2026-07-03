# CloudLabs AI Proctor Architecture

## Overview

CloudLabs AI Proctor is an AI-powered virtual lab assistant that provides real-time troubleshooting and contextual guidance for CloudLabs hands-on labs. The system combines Azure OpenAI with a knowledge base search engine to generate accurate, context-aware responses for learners while capturing analytics and feedback for continuous improvement.

---

## High-Level Architecture

```
                    +-------------------------+
                    |     React Frontend      |
                    |  (CloudLabs AI Proctor) |
                    +-----------+-------------+
                                |
                                | REST API
                                |
                    +-----------v-------------+
                    |     FastAPI Backend     |
                    +-----------+-------------+
                                |
        +-----------+-----------+-----------+-----------+
        |           |           |           |           |
        |           |           |           |           |
+-------v----+ +----v-----+ +---v----+ +----v-----+ +---v------+
| Azure      | | Search   | |Session | |Analytics | |Feedback  |
| OpenAI     | | Service  | |Service | | Logger   | | Service  |
+------------+ +----------+ +--------+ +----------+ +----------+
                     |
                     |
              +------v------+
              | Knowledge   |
              | Base (.md)  |
              +-------------+
```

---

## Components

### React Frontend

- Chat interface
- Quick Help shortcuts
- Lab context display
- Feedback collection
- Real-time communication with backend

---

### FastAPI Backend

The backend exposes REST APIs for:

- Chat
- Search
- Feedback
- Analytics
- Session management
- Health monitoring

---

### Azure OpenAI

Azure OpenAI generates troubleshooting responses using retrieved lab documentation and current user context.

---

### Knowledge Base

The knowledge base consists of Markdown documents containing:

- Lab guides
- Common issues
- Troubleshooting steps
- Azure portal guidance
- Microsoft Fabric documentation

---

### Analytics Engine

Analytics records:

- User conversations
- Search confidence
- Feedback ratings
- Session statistics
- Frequently occurring issues

---

### Feedback Module

Users can rate responses as:

- 👍 Helpful
- 👎 Not Helpful

Feedback is stored for future model evaluation and knowledge base improvement.

---

## Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | React + Vite |
| Backend | FastAPI |
| AI | Azure OpenAI |
| Search | Markdown Knowledge Base |
| Analytics | JSON Logs |
| Deployment | Azure App Service |
| Containerization | Docker |
| Version Control | GitHub |

---

## Future Architecture Enhancements

- Vector database integration
- Retrieval-Augmented Generation (RAG)
- Azure AI Search
- Multi-user authentication
- Conversation history database
- Real-time monitoring dashboard
- Automated knowledge base ingestion
