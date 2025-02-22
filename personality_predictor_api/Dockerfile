FROM python:3.9-slim

RUN pip install --upgrade pip
RUN pip install torch
RUN pip install transformers uvicorn fastapi pydantic
# Set the working directory
WORKDIR /app

COPY models/ ./models/
COPY personality_predictor/ ./personality_predictor/
COPY setup.py ./


RUN pip install .
COPY main.py ./

# Expose the API port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]