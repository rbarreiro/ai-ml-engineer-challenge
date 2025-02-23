from setuptools import setup, find_packages

setup(
    name='personality_predictor',
    version='0.1.0',
    description='A FastAPI API for personality prediction',
    packages=find_packages(), 
    install_requires=[
        'fastapi',
        'uvicorn',
        'transformers',
        'pydantic',
        'torch'
    ],
    
)