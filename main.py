from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.app import router as app_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    yield
    # Shutdown code here


app = FastAPI(
    title="FastAPI Boilerplate",
    description="A boilerplate for FastAPI projects",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(app_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
