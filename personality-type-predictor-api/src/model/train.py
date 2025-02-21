from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import joblib

def train_model(dataset_path):
    # Load the dataset
    data = pd.read_csv(dataset_path)

    # Preprocess the data
    X = data['text']
    y = data['type']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize the text data
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)

    # Train the model
    model = MultinomialNB()
    model.fit(X_train_vectorized, y_train)

    # Save the model and vectorizer
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

    return model, vectorizer

if __name__ == "__main__":
    train_model('path_to_mbti_dataset.csv')