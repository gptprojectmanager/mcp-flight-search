"""
Logging configuration for MCP Flight Search.
"""
import logging
import sys
from rich.logging import RichHandler

def setup_logging(use_rich=True):
    """Configure and set up logging for the application.
    
    Args:
        use_rich: If False, uses basic logging to stderr (for stdio mode)
    """
    if use_rich:
        # Rich logging for HTTP mode
        logging.basicConfig(
            level=logging.DEBUG,
            format="| %(levelname)-8s | %(name)s | %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S]",
            handlers=[RichHandler(rich_tracebacks=True)],
            force=True
        )
    else:
        # Basic logging to stderr for stdio mode (don't contaminate stdout)
        logging.basicConfig(
            level=logging.WARNING,  # Reduced verbosity for stdio
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[logging.StreamHandler(sys.stderr)],
            force=True
        )

    logger = logging.getLogger("flight_search")
    # Silence noisy third-party loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.error").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.ERROR)
    logging.getLogger("mcp.server").setLevel(logging.ERROR)
    
    return logger

# Create the logger instance for import by other modules  
logger = setup_logging() 