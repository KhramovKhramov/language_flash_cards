from fastapi import FastAPI
from src.config import app_config

app = FastAPI(**app_config)