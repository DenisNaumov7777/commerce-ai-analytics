from fastapi.testclient import TestClient
from app.main import app

# Initialize the test client
client = TestClient(app)

def test_root():
    """
    Test the root endpoint to ensure the service is running.
    Should return 200 OK and a welcome message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "running" in response.json()["message"]

def test_emotion_joy_mock():
    """
    Test the 'Joy' emotion detection.
    In Mock Mode, the word 'happy' triggers the Joy response.
    """
    response = client.post("/api/v1/emotion", json={"text": "I am so happy today"})
    assert response.status_code == 200
    data = response.json()
    
    # Check if the dominant emotion is correctly identified as 'joy'
    assert data["dominant_emotion"] == "joy"
    assert data["emotions"]["joy"] > 0.8

def test_emotion_anger_mock():
    """
    Test the 'Anger' emotion detection.
    In Mock Mode, the word 'mad' triggers the Anger response.
    """
    response = client.post("/api/v1/emotion", json={"text": "I am really mad about this error"})
    assert response.status_code == 200
    data = response.json()
    
    # Check if the dominant emotion is correctly identified as 'anger'
    assert data["dominant_emotion"] == "anger"
    assert data["emotions"]["anger"] > 0.8

def test_invalid_input_empty():
    """
    Test how the API handles empty input.
    It should gracefully return a 200 OK with None or handle it via validation.
    Note: In our current logic, empty string returns 200 with None values or 400 depending on router logic.
    Let's check the validation error for empty string if Pydantic catches it, 
    OR the service logic returns empty response.
    """
    # Sending empty text
    response = client.post("/api/v1/emotion", json={"text": ""})
    
    # According to our Pydantic model (min_length=1), this should be a 422 Validation Error
    # OR if we handle it in services, it returns empty scores.
    # Let's see what happens. If Pydantic works, it is 422.
    assert response.status_code in [400, 422]
    