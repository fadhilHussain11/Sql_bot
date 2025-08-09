from pathlib import Path
import sqlite3
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine


def configure():
    db_file_path = (Path(__file__).parent/"../data/olist.sqlite").absolute()
    print(db_file_path)
    cre = lambda:sqlite3.connect(f"file:{db_file_path}?mode=ro",uri=True)
    return SQLDatabase(create_engine("sqlite://",creator=cre))
