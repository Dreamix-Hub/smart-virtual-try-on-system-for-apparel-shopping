import logging

def setup_logger() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger("Smart virtual try-on system")

logger = setup_logger()