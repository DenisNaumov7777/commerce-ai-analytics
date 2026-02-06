"""
Service layer for interacting with IBM Watson NLP API.
Handles external API calls and provides a fallback Mock mode.
"""
import httpx
from app.config import settings
from app.models import EmotionResponse, EmotionScores

async def analyze_emotion_async(text: str) -> EmotionResponse:
    """
    Asynchronously calls the IBM Watson NLP service to analyze the provided text.

    FALLBACK STRATEGY:
    If the Watson API is unreachable (e.g., running locally outside IBM network),
    this function switches to 'Mock Mode' and returns simulated data.
    This ensures the application remains functional for demonstration purposes.

    Args:
        text (str): The text to analyze.

    Returns:
        EmotionResponse: A structured object containing emotion scores and dominant emotion.
    """
    if not text.strip():
        return EmotionResponse(emotions=EmotionScores(), dominant_emotion=None)

    payload = {"raw_document": {"text": text}}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                settings.WATSON_URL,
                headers=settings.WATSON_HEADERS,
                json=payload,
                timeout=3.0
            )

            if response.status_code == 400:
                return EmotionResponse(emotions=EmotionScores(), dominant_emotion=None)

            response.raise_for_status()

            data = response.json()
            emotions_data = data["emotionPredictions"][0]["emotion"]
            dominant = max(emotions_data, key=emotions_data.get)

            return EmotionResponse(
                emotions=EmotionScores(**emotions_data),
                dominant_emotion=dominant
            )

        # pylint: disable=broad-exception-caught
        except Exception as e:
            print(f"⚠️ Watson API unreachable ({e}). Switching to MOCK data.")

            text_lower = text.lower()
            mock_scores = {
                "anger": 0.9 if "mad" in text_lower or "hate" in text_lower else 0.05,
                "joy": 0.9 if "happy" in text_lower or "glad" in text_lower else 0.05,
                "fear": 0.1,
                "disgust": 0.1,
                "sadness": 0.1
            }

            if max(mock_scores.values()) < 0.5:
                mock_scores["joy"] = 0.5

            dominant = max(mock_scores, key=mock_scores.get)

            return EmotionResponse(
                emotions=EmotionScores(**mock_scores),
                dominant_emotion=dominant
            )
