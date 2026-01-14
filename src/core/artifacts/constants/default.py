from enum import StrEnum
import os

class DefaultConfig(StrEnum):
    """Default configuration constants."""
    
    # Default database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_wBZkhxi16FYR@ep-jolly-snow-ahst6lcn-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
    
    # JWT Authentication configuration
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = "30"