from functools import wraps
from src.core.config.db import AsyncSessionLocal

def connect_db(commit=True):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with AsyncSessionLocal() as session:
                try:
                    result = await func(*args, session=session, **kwargs)
                    if commit:
                        await session.commit()
                    return result
                except Exception:
                    await session.rollback()
                    raise
        return wrapper
    return decorator
