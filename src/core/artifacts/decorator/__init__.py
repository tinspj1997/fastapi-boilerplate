from functools import wraps
from inspect import iscoroutinefunction
from loguru import logger
from src.core.config.db import SessionLocal, engine


def inject_db():
    """
    Decorator that injects a SQLAlchemy session.
    - Works for sync & async functions
    - Commits automatically
    - Rolls back on exception
    - Closes session safely
    """

    def decorator(func):
        if iscoroutinefunction(func):

            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                # Allow external session injection (tests / batch jobs)
                if kwargs.get("session") is not None:
                    return await func(*args, **kwargs)

                session = SessionLocal()
                try:
                    result = await func(*args, session=session, **kwargs)
                    session.commit()
                    return result
                except Exception:
                    session.rollback()
                    logger.exception("Async DB transaction failed")
                    raise
                finally:
                    session.close()
                    _log_pool_stats()

            return async_wrapper

        else:

            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                if kwargs.get("session") is not None:
                    return func(*args, **kwargs)

                session = SessionLocal()
                try:
                    result = func(*args, session=session, **kwargs)
                    session.commit()
                    return result
                except Exception:
                    session.rollback()
                    logger.exception("Sync DB transaction failed")
                    raise
                finally:
                    session.close()
                    _log_pool_stats()

            return sync_wrapper

    return decorator


def _log_pool_stats():
    """
    Debug-only pool stats.
    Safe to disable in production by log level.
    """
    pool = engine.pool
    logger.bind(component="db_pool").debug(
        f"checked_in={pool.checkedin()} | "
        f"checked_out={pool.checkedout()} | "
        f"size={pool.size()}"
    )
