from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from contextlib import asynccontextmanager
from src.core.config.db import engine
from src.core.config.logging import setup_logging
from src.core.middleware import log_requests
from src.app import router as app_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    print("Starting up...")
    setup_logging()
    yield
    print("DB Engine disposing...")
    print(engine.pool.checkedin())
    print(engine.pool.checkedout())
    await engine.dispose()
    print("DB Engine disposed.")


app = FastAPI(
    title="FastAPI Boilerplate",
    description="A boilerplate for FastAPI projects",
    version="0.1.0",
    lifespan=lifespan,
)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        return await log_requests(request, call_next)


app.add_middleware(LoggingMiddleware)
app.include_router(app_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
