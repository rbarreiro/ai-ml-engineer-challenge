import os
from fastapi import APIRouter
from pydantic import BaseModel

from transformers import pipeline

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "my_mbti", "checkpoint-5967")
classifier = pipeline("text-classification", model=MODEL_PATH)

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/predict")
async def predict_personality_type(text_input: TextInput):
    pred = classifier([text_input.text])
    
    return {
        "mbti_type": pred[0]["label"],
        "confidence": pred[0]["score"]
    }