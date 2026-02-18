import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db_settings = {
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "name": os.getenv("DB_NAME"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dialect": os.getenv("DIALECT"),
    "driver": os.getenv("DRIVER"),
}

DATABASE_URL = (
    f"{db_settings['dialect']}+{db_settings['driver']}://{db_settings['username']}:"
    f"{db_settings['password']}@{db_settings['host']}:{db_settings['port']}/{db_settings['name']}"
)
