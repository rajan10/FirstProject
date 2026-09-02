from sqlmodel import create_engine
import os

BASE_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(BASE_DIR, "app.db")
DATABASE_URL = f"sqlite:///{DB_FILE}"


def get_engine():
    # echo=False to keep logs cleaner; change to True for SQL debugging
    return create_engine(DATABASE_URL, echo=False)
