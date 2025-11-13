# app/db.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, relationship
import os

# Base for ORM models
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Text, BigInteger
import uuid


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(
        Text, unique=True, default=lambda: str(uuid.uuid4())
    )


# Engine options suitable for production (tweak pool sizes to your infra)
engine = create_async_engine(
    os.getenv("ASYNC_DATABASE_URL"),
    echo=False,
    future=True,
    pool_size=10,       # tune for your environment
    max_overflow=20,    # tune for spiky loads
)

# async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
