from .config import RAW_DATA_DIR, REQUIRED_FILES


def validate_raw_data():
    missing_files = [
                        x for x in REQUIRED_FILES
                          if not (RAW_DATA_DIR / x).exists()
                    ]
    if missing_files:
        raise FileNotFoundError(f"Validation failed.\n \
                                Missing files: {'\n-'.join(missing_files)}.\ \n \
                                Please ensure all required files are present in the raw data directory \n{RAW_DATA_DIR}.")
    return True
