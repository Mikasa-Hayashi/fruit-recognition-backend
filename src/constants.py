import os

DATABASE_URL: str = os.getenv('DATABASE_URL', None)

MODEL_PATH: str = os.getenv('MODEL_PATH', None)


if DATABASE_URL is None:
    raise ValueError('DATABASE_URL is not set in environment variables')

if MODEL_PATH is None:
    raise ValueError('MODEL_PATH is not set in environment variables')