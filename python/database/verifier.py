from python.utils.logger import get_logger
from python.ingestion.config import STAGING_DATA_DIR
import pandas as pd
logger = get_logger(__name__)

def data_verify(conn, stage_data):
    """
    Verify number of rows from database and dataframe
    """
    cursor = conn.cursor()
    try:
        for table_name in stage_data.keys():
            csv_rows = len(stage_data[table_name])
            query = f"select count(*) from staging.{table_name}"
            cursor.execute(query) 
            db_rows = cursor.fetchone()[0]
            if csv_rows == db_rows:
                logger.info(f"{table_name} row count verified");
            else:
                logger.error(f"Rows count mismatch {table_name}")
                raise ValueError(
                    f"Verification failed for {table_name}."
                    f"Expected rows count {csv_rows} found to be {db_rows}"
                )
    finally:
        cursor.close()

