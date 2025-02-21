def predict_mbti(text, model, vectorizer):
    # Preprocess the input text
    processed_text = vectorizer.transform([text])
    
    # Make a prediction using the trained model
    prediction = model.predict(processed_text)
    
    # Get the confidence score
    confidence = model.predict_proba(processed_text).max()
    
    # Return the predicted MBTI type and confidence score
    return {
        "mbti_type": prediction[0],
        "confidence": confidence
    }