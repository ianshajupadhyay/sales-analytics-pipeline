from python.ingestion.loader import load_raw_data
from python.ingestion.validator import validate_raw_data
from python.transformation.transform import transform_raw_data
from python.staging.transform import stage_raw_data
from python.staging.writer import write_staging_data
def main():
    validate_raw_data()
    raw_data = load_raw_data()
    print(f"Loaded {len(raw_data)} raw datasets")
    transformed_data = transform_raw_data(raw_data)
    stage_data = stage_raw_data(transformed_data)
    print(f"Staged {len(stage_data)} transformed datasets")
    write_staging_data(stage_data)
    print("Data staged")



if __name__ == "__main__":
    main()