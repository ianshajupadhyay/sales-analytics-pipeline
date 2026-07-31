from python.ingestion.config import CHUNK_SIZE
from python.utils.logger import get_logger

logger = get_logger(__name__)

class PostgresLoader:
    def __init__(self, conn):
        self.conn = conn
    def truncate_table(self, table_name):
        cursor = self.conn.cursor()
        query = f"TRUNCATE TABLE {table_name}"
        cursor.execute(query)

    def load(self, file_path, table_name):
        cursor = self.conn.cursor()
        
        try:
            with open(file_path,"r",encoding='utf-8') as file:
                logger.info(f"Loading data {file_path}")

                with cursor.copy(f"""COPY {table_name} FROM STDIN WITH ( FORMAT CSV, HEADER) """) as copy:
                    data = file.read(CHUNK_SIZE)
                    while data:
                        copy.write(data)
                        data = file.read(CHUNK_SIZE)        
                self.conn.commit()
                logger.info(f"Successfully loaded {file_path} into {table_name}")
        except Exception:
            logger.exception(f"Loading data failed: {file_path} into {table_name}")
            self.conn.rollback()
            raise
        finally:
            cursor.close()

