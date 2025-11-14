from fastapi import Request
from loguru import logger
import time

async def log_requests(request: Request, call_next):
    """Middleware: Log requests like 📥 GET / → 200 (0.05s)."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    logger.info(
        f"📥 {request.method} {request.url.path} → {response.status_code} ({process_time:.2f}s)"
    )
    return response