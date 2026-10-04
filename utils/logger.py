from pathlib import Path

from loguru import logger


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger.add(
    LOG_DIR / "api_automation.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
)

__all__ = ["logger"]