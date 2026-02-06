"""
API routes for emotion analysis.
"""
from fastapi import APIRouter, HTTPException, status
from app.models import EmotionRequest, EmotionResponse
from app.services import analyze_emotion_async

router = APIRouter(prefix="/api/v1", tags=["Analytics"])

@router.post("/emotion", response_model=EmotionResponse)
async def detect_emotion(request: EmotionRequest):
    """
    Endpoint to analyze customer feedback text.

    - **text**: The string content to analyze.

    Returns structured emotion scores and the dominant emotion.
    Raises 400 Bad Request if the text is invalid or empty.
    """
    result = await analyze_emotion_async(request.text)

    if result.dominant_emotion is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid text! Please try again with valid input."
        )

    return result
