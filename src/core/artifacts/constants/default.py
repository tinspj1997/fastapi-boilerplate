from enum import StrEnum
import os

class DefaultConfig(StrEnum):
    """Default configuration constants."""
    
    # Default database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://neondb_owner:npg_wBZkhxi16FYR@ep-jolly-snow-ahst6lcn-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")