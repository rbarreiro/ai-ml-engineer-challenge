import os
from fastapi import FastAPI
from fastapi import APIRouter
from pydantic import BaseModel

from transformers import pipeline

classifier = pipeline("text-classification", model="rbarreiro/my_mbti")

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


app = FastAPI()

app.include_router(router)