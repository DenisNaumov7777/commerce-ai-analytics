"""
Application configuration settings using Pydantic Settings.
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Main settings class. Reads environment variables.
    """
    PROJECT_NAME: str = "Commerce AI Analytics"
    VERSION: str = "1.0.0"

    # Watson NLP Service Configuration
    WATSON_URL: str = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    WATSON_HEADERS: dict = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

settings = Settings()
