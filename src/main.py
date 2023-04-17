from utils.logger import setup_logger

logger = setup_logger("Eye", "../logs/scanner.log")


if __name__ == "__main__":
    logger.info("Starting vulnerability scanner...")

    # Run your vulnerability scanner and report generation code here

    logger.info("Vulnerability scanner finished.")
