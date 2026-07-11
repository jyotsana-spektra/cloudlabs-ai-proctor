import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "Brainy API"
    APP_VERSION = "1.0.0"

    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")

    KNOWLEDGE_BASE_PATH = "knowledge-base"
    ANALYTICS_EVENTS_PATH = "analytics/events.json"
    ANALYTICS_FEEDBACK_PATH = "analytics/feedback.json"

    # Internet fallback used when a troubleshooting/lab question has no
    # strong match in the local knowledge base.
    ENABLE_WEB_SEARCH = os.getenv("ENABLE_WEB_SEARCH", "true").lower() == "true"
    WEB_SEARCH_TIMEOUT = float(os.getenv("WEB_SEARCH_TIMEOUT", "6"))


settings = Settings()