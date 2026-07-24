from .config import RAW_DATA_DIR, REQUIRED_FILES
import pandas as pd


def load_raw_data():
    """Loads all required datasets into memory and return them as a dict of pandas DataFrame"""
    raw_data: dict[str, pd.DataFrame] = {}
    for file in REQUIRED_FILES:
        file_path = RAW_DATA_DIR / file
        key = file.removeprefix('olist_').removesuffix('_dataset.csv').removesuffix('.csv')
        try:
            raw_data[key] = pd.read_csv(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File Missing {file}. Please check into the raw data directory {RAW_DATA_DIR}")

    return raw_data