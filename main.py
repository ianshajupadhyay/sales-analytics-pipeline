from python.ingestion.loader import load_raw_data
from python.ingestion.validator import validate_raw_data
from python.transformation.transform import transform_raw_data

def main():
    validate_raw_data()
    raw_data = load_raw_data()
    print(f"Loaded {len(raw_data)} raw datasets")
    transformed_data = transform_raw_data(raw_data)
    for name, data in transformed_data.items():
        print(f"transformed {name}")
    

if __name__ == "__main__":
    main()