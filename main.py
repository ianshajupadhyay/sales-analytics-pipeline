from python.ingestion.loader import load_raw_data
from python.ingestion.validator import validate_raw_data

def main():
    validate_raw_data()
    raw_data = load_raw_data()
    print(f"Loaded {len(raw_data)} datasets")

if __name__ == "__main__":
    main()