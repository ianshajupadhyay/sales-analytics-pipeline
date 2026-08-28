from pathlib import Path
import pandas as pd
from python.ingestion.config import STAGING_DATA_DIR

def _write_dataframe(df: pd.DataFrame, file_path: Path)-> None:
    df.to_csv(file_path, index= False)

def write_staging_data(stagedata: dict[str, pd.DataFrame]) -> None:
    staging_path = STAGING_DATA_DIR
    staging_path.mkdir( parents= True,exist_ok=True)
    for name, data in stagedata.items():
        file_path = staging_path / f"{name}.csv"
        _write_dataframe(data, file_path)