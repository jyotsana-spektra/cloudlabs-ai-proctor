# CloudLabs AI Proctor Troubleshooting Guide

## Overview

This guide provides solutions for common issues encountered while developing, deploying, and using CloudLabs AI Proctor.

---

# Backend Issues

## Backend does not start

### Symptoms

- Uvicorn exits immediately
- Module import errors
- Missing dependencies

### Resolution

```bash
pip install -r requirements.txt
python -m uvicorn backend.main:app --reload
```

---

## Azure OpenAI Authentication Error

### Symptoms

```
Missing credentials
```

### Resolution

Verify the `.env` file contains:

```
AZURE_OPENAI_ENDPOINT
AZURE_OPENAI_API_KEY
AZURE_OPENAI_DEPLOYMENT_NAME
AZURE_OPENAI_API_VERSION
```

Restart the backend.

---

## Port 8000 Already in Use

Find the running process.

```bash
lsof -i :8000
```

Terminate it.

```bash
kill -9 <PID>
```

Restart the backend.

---

# Frontend Issues

## Frontend cannot connect to backend

Verify:

- Backend is running
- Port 8000 is public
- `frontend/src/services/api.js` points to the backend URL

---

## Blank React Screen

Run:

```bash
npm install
npm run dev
```

Check browser console for JavaScript errors.

---

# Knowledge Base Issues

## AI returns generic responses

Verify:

- Markdown files exist
- Search service is functioning
- Knowledge base path is correct

---

# Analytics Issues

## Events not logged

Verify:

```
analytics/events.json
```

exists and is writable.

---

## Feedback not stored

Verify:

```
analytics/feedback.json
```

exists and feedback API is functioning.

---

# Deployment Issues

- Verify environment variables.
- Verify Azure OpenAI deployment name.
- Ensure App Service startup command is correct.

---

# Recommended Debugging Order

1. Backend
2. Azure OpenAI
3. Search Service
4. Frontend
5. Analytics
6. Deployment