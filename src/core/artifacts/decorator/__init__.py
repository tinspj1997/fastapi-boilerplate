from functools import wraps
from src.core.config.db import engine,AsyncSessionLocal

def connect_db(commit=False):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with AsyncSessionLocal() as session:
                pool = engine.pool
                try:
                    result = await func(*args, session=session, **kwargs)
                    if commit:
                        await session.commit()
                    return result
                except Exception:
                    await session.rollback()
                    raise
                finally:
                    print("DB Closed for session:", session)
                    print(f"Idle connections : {pool.checkedin()}")
                    print(f"Active connections (in use): {pool.checkedout()}")
                    print(f"Total connections: {pool.size()}")
                    await session.close()    
        return wrapper
    return decorator
