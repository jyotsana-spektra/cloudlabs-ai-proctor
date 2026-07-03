# CloudLabs AI Proctor Deployment Guide

## Overview

This guide explains how to deploy the CloudLabs AI Proctor application locally and to Azure.

---

# Prerequisites

Before deployment, ensure the following are installed:

- Python 3.11+
- Node.js 18+
- npm
- Git
- Azure Subscription
- Azure OpenAI Resource

---

# Project Structure

```
cloudlabs-ai-proctor/

├── backend/
├── frontend/
├── analytics/
├── knowledge-base/
├── deployments/
└── docs/
```

---

# Backend Deployment

Navigate to the project directory.

```bash
cd backend
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

Example:

```text
AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com/
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4.1-mini
AZURE_OPENAI_API_VERSION=2025-04-01-preview
```

Run the backend.

```bash
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

# Frontend Deployment

Navigate to the frontend.

```bash
cd frontend
```

Install packages.

```bash
npm install
```

Run the development server.

```bash
npm run dev -- --host 0.0.0.0
```

Frontend URL:

```
http://localhost:5173
```

---

# Docker Deployment

Build the Docker image.

```bash
docker build -t cloudlabs-ai-proctor -f deployments/Dockerfile .
```

Run the container.

```bash
docker run -p 8000:8000 cloudlabs-ai-proctor
```

---

# Azure App Service Deployment

The repository includes a GitHub Actions workflow:

```
deployments/appservice-deploy.yml
```

Deployment steps:

1. Create an Azure App Service.
2. Configure the required environment variables.
3. Add the App Service publish profile to GitHub Secrets.
4. Trigger the deployment workflow.

---

# Environment Variables

| Variable | Description |
|----------|-------------|
| AZURE_OPENAI_ENDPOINT | Azure OpenAI endpoint |
| AZURE_OPENAI_API_KEY | Azure OpenAI API key |
| AZURE_OPENAI_DEPLOYMENT_NAME | Deployment name |
| AZURE_OPENAI_API_VERSION | API version |

---

# Verification

After deployment:

- Backend starts successfully.
- Swagger UI is accessible.
- Frontend connects to the backend.
- Chat endpoint returns AI responses.
- Feedback is saved successfully.
- Analytics events are logged.

---

# Troubleshooting

If the backend fails to start:

- Verify environment variables.
- Check Azure OpenAI credentials.
- Ensure port 8000 is available.
- Review application logs for detailed errors.
