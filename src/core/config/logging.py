from loguru import logger
from pathlib import Path

def setup_logging():
    """Quick Loguru setup: Console + rotating files."""
    Path("logs").mkdir(exist_ok=True)  # Make folder
    
    # Add file sink (rotates daily, keeps 7 days)
    logger.add(
        "logs/app_{time:YYYY-MM-DD}.log",
        rotation="1 day",
        retention="7 days",
        level="INFO"
    )
    # Console is already colorful—no extra code!
    
    logger.info("📝 Logging ready!")