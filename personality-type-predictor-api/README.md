# FILE: /personality-type-predictor-api/personality-type-predictor-api/README.md
# **Personality Type Predictor API**  

## **Overview**  
This project implements a machine learning-powered API that predicts a user’s MBTI personality type based on text input. The API is built using FastAPI and is designed to demonstrate an end-to-end system, including data processing, model training, API development, containerization, and CI/CD automation.

## **Project Structure**  
```
personality-type-predictor-api
├── src
│   ├── api                # Contains API-related code
│   │   ├── __init__.py
│   │   ├── main.py        # Entry point for the API application
│   │   └── routes.py      # Defines API routes
│   ├── model              # Contains model training and prediction logic
│   │   ├── __init__.py
│   │   ├── train.py       # Logic for training the ML model
│   │   └── predict.py     # Logic for making predictions
│   ├── utils              # Contains utility functions
│   │   ├── __init__.py
│   │   └── preprocess.py   # Text preprocessing functions
│   └── tests              # Contains unit tests
│       ├── __init__.py
│       └── test_api.py    # Tests for API endpoints
├── Dockerfile              # Dockerfile for containerization
├── .github
│   └── workflows
│       └── ci.yml         # CI/CD pipeline configuration
├── requirements.txt        # Project dependencies
└── .gitignore              # Files and directories to ignore
```

## **Setup Instructions**  
1. Clone the repository:  
   `git clone <repository-url>`

2. Navigate to the project directory:  
   `cd personality-type-predictor-api`

3. Install the required dependencies:  
   `pip install -r requirements.txt`

4. Run the API locally:  
   `uvicorn src.api.main:app --reload`

## **Usage**  
To get predictions from the API, send a POST request to the `/predict` endpoint with a JSON payload containing the text input.  
### Example Request:  
```
POST /predict
Content-Type: application/json

{
  "text": "I love deep conversations and thinking about abstract ideas."
}
```

### Example Response:  
```
{
  "mbti_type": "INFJ",
  "confidence": 0.87
}
```

## **Docker**  
To build and run the application using Docker, execute the following commands:  
1. Build the Docker image:  
   `docker build -t personality-type-predictor-api .`

2. Run the Docker container:  
   `docker run -p 8000:8000 personality-type-predictor-api`

## **CI/CD**  
The project includes a CI/CD pipeline configured with GitHub Actions. It runs automated tests and builds the Docker image upon successful tests.

## **Contributing**  
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## **License**  
This project is licensed under the MIT License.