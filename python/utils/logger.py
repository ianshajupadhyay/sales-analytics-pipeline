import logging

def get_logger(name:str) -> logging.Logger:
    """
    Create and return a configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(name)s | "
            "%(levelname)s | "
            "%(funcName)s | "
            "Line %(lineno)d | "
            "%(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        file_handler = logging.FileHandler(
            "logs/pipeline.log",
            mode = 'a',
            encoding= 'utf-8'
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    return logger