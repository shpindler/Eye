import logging


def setup_logger(
    logger_name: str, log_file: str, level: int = logging.INFO
) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Create file handler to log messages to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create console handler to print messages to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    logger = setup_logger("vulnerability_scanner", "vulnerability_scanner.log")
    logger.info("This is an info message.")
    logger.error("This is an error message.")
