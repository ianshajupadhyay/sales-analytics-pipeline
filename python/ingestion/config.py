from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
STAGING_DATA_DIR = DATA_DIR / "staging"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "sales_analytics"
DB_USER = "postgres"
DB_PASSWORD = "2901"

CHUNK_SIZE = 65536

REQUIRED_FILES = [
    'olist_customers_dataset.csv',
    'olist_geolocation_dataset.csv',
    'olist_order_items_dataset.csv',
    'olist_order_payments_dataset.csv',
    'olist_order_reviews_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_products_dataset.csv',
    'olist_sellers_dataset.csv',
    'product_category_name_translation.csv'
    ]