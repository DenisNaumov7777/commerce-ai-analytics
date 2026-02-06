"""
Pydantic models for request and response validation.
"""
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class EmotionRequest(BaseModel):
    """
    Schema for the incoming analysis request.
    """
    text: str = Field(..., min_length=1, description="Text content to be analyzed.")

class EmotionScores(BaseModel):
    """
    Schema representing the confidence scores for each emotion.
    """
    anger: Optional[float] = 0.0
    disgust: Optional[float] = 0.0
    fear: Optional[float] = 0.0
    joy: Optional[float] = 0.0
    sadness: Optional[float] = 0.0

class EmotionResponse(BaseModel):
    """
    Schema for the API response containing emotion scores and the dominant emotion.
    """
    emotions: EmotionScores
    dominant_emotion: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "emotions": {
                    "anger": 0.01,
                    "joy": 0.95,
                    "fear": 0.02,
                    "disgust": 0.01,
                    "sadness": 0.01
                },
                "dominant_emotion": "joy"
            }
        }
    )
