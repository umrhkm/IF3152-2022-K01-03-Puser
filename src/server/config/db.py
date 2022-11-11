import psycopg2
from psycopg2 import DatabaseError
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("DATABASE_URL")


def get_connection():
    try:
        return psycopg2.connect(url)
    except DatabaseError as err:
        raise err