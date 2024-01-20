from fastapi import FastAPI
from sqlalchemy.exc import NoResultFound

from src.config import app_config
from src.exceptions import sqlalchemy_not_found_exception_handler


app = FastAPI(**app_config)
app.add_exception_handler(
    NoResultFound,
    sqlalchemy_not_found_exception_handler,
)
