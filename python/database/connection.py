import psycopg
from python.utils.logger import get_logger

from python.ingestion.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

logger = get_logger(__name__)

class PostgresConnection:
    def __init__(self):
        self.host = DB_HOST
        self.port= DB_PORT
        self.db_name = DB_NAME
        self.user = DB_USER
        self.password = DB_PASSWORD
    def connect(self):

        try :
            logger.info("Establishing connection to Postgres database")
            conn = psycopg.connect(
                host = self.host,
                port = self.port,
                dbname = self.db_name,
                user = self.user,
                password = self.password
            )
            logger.info("Connection established")
        except Exception:
            logger.exception("Failed to connect to Postgres")
            raise
        return conn


