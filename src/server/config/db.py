'''Import module'''
import os
import psycopg2
from psycopg2 import DatabaseError
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("DATABASE_URL")


def get_connection():
    '''Buat konek db'''
    try:
        return psycopg2.connect(url)
    except DatabaseError as err:
        raise err
