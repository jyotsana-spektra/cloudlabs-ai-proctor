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


settings = Settings()