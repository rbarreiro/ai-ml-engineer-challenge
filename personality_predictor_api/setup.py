from setuptools import setup, find_packages

setup(
    name='personality_predictor',
    version='0.1.0',
    description='A FastAPI API for personality prediction',
    packages=find_packages(),  # Find packages in the 'src' directory
    install_requires=[
        'fastapi',
        'uvicorn',
        'transformers',
        'pydantic',
        'torch'
    ],
    package_data={'': ['../models/my_mbti/checkpoint-5967']},  # Include model checkpoint in the package
    
)