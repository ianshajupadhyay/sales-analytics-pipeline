from python.ingestion.loader import load_raw_data
from python.ingestion.validator import validate_raw_data
from python.transformation.transform import transform_raw_data
from python.staging.transform import stage_raw_data
from python.staging.writer import write_staging_data
from python.database.loader import PostgresLoader
from python.database.connection import PostgresConnection
from python.utils.logger import get_logger
from python.ingestion.config import STAGING_DATA_DIR
from python.database.verifier import data_verify

logger = get_logger(__name__)
def main():
    logger.info("Starting Sales Analytics pipeline")
    validate_raw_data()
    raw_data = load_raw_data()
    print(f"Loaded {len(raw_data)} raw datasets")
    transformed_data = transform_raw_data(raw_data)
    stage_data = stage_raw_data(transformed_data)
    print(f"Staged {len(stage_data)} transformed datasets")
    write_staging_data(stage_data)
    print("Data staged")
    connection = PostgresConnection()
    conn = connection.connect()
    loader = PostgresLoader(conn)
    try:
        for table_name in stage_data.keys():
            loader.truncate_table(f"staging.{table_name}")
            loader.load(
                file_path=f"{STAGING_DATA_DIR}/{table_name}.csv",
                table_name=f"staging.{table_name}"
            )
        data_verify(conn, stage_data)
    finally:
        conn.close()
        logger.info("Database connection closed.")
    
    

if __name__ == "__main__":
    main()