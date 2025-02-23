from fastapi.testclient import TestClient
from personality_predictor.api.app import app

client = TestClient(app)

def test_predict_mbti():
    response = client.post("/predict", json={"text": "I love deep conversations and thinking about abstract ideas."})
    assert response.status_code == 200
    assert "mbti_type" in response.json()
    assert "confidence" in response.json() 

def test_predict_mbti_invalid_input():
    response = client.post("/predict", json={"textr": ""})
    assert response.status_code != 200  