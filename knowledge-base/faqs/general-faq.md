# General FAQ

## Overview

General questions related to CloudLabs AI Proctor.

---

## Frequently Asked Questions

### What is CloudLabs AI Proctor?

CloudLabs AI Proctor is an AI-powered assistant that helps learners troubleshoot issues and complete CloudLabs lab exercises.

---

### How does the AI answer questions?

The assistant combines Azure OpenAI with a curated knowledge base to generate contextual responses.

---

### Can the AI understand lab context?

Yes. It uses the current lab, exercise, task, and conversation history.

---

### Does the AI remember previous questions?

Yes. Conversation history is maintained within the active session.

---

### Does the AI access the Internet?

No. Responses are based primarily on the configured knowledge base and Azure OpenAI.

---

### Can the AI upload documents?

The backend supports knowledge base ingestion for supported document formats.

---

### Is feedback collected?

Yes. Users can rate responses as Helpful or Not Helpful.

---

### What analytics are captured?

- Chat events
- Feedback
- Confidence scores
- Knowledge source usage

---

### Can the AI escalate issues?

Yes. Unresolved issues can be logged for review.

---

### Is my conversation stored?

Session history is maintained during the active session. Long-term storage can be added in future versions.

---

### Can multiple users use the AI simultaneously?

Yes. Each session is managed independently.

---

### Does the AI support Microsoft Fabric?

Yes.

---

### Does it support Azure?

Yes.

---

### Does it support Power Platform?

Knowledge can be extended to support Power Platform labs.

---

### Is the project open for future enhancements?

Yes. The architecture is designed to support additional AI capabilities.