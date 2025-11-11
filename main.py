from fastapi import FastAPI
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    yield
    # Shutdown code here

app = FastAPI(
    title="FastAPI Boilerplate",
    description="A boilerplate for FastAPI projects",
    version="0.1.0",
    lifespan=lifespan
)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
