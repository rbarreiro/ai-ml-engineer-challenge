from sklearn.feature_extraction.text import CountVectorizer
import re

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def tokenize_and_vectorize(texts):
    cleaned_texts = [clean_text(text) for text in texts]
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(cleaned_texts)
    return vectors, vectorizer