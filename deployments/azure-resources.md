# Azure Resources

The CloudLabs AI Proctor MVP uses the following Azure resources:

## Azure OpenAI / Foundry

Used for generating AI troubleshooting responses.

Required environment variables:

- AZURE_OPENAI_ENDPOINT
- AZURE_OPENAI_API_KEY
- AZURE_OPENAI_DEPLOYMENT_NAME
- AZURE_OPENAI_API_VERSION

## Azure App Service

Recommended for hosting the FastAPI backend.

Backend start command:

```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
