from fastapi import APIRouter, HTTPException
from src.model.predict import predict_mbti

router = APIRouter()

@router.post("/predict")
async def predict_personality_type(text: dict):
    if "text" not in text:
        raise HTTPException(status_code=400, detail="Text input is required")
    
    mbti_type, confidence = predict_mbti(text["text"])
    
    return {
        "mbti_type": mbti_type,
        "confidence": confidence
    }