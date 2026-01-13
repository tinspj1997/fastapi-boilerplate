# app/db.py
import os
import uuid

from sqlalchemy import create_engine, Text, BigInteger
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    Mapped,
    mapped_column,
)

# -----------------------------
# Base for ORM models
# -----------------------------
class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=True
    )
    uuid: Mapped[str] = mapped_column(
        Text, unique=True, default=lambda: str(uuid.uuid4())
    )


# -----------------------------
# Sync Engine
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=300,   # 5 minutes
    pool_pre_ping=True,
)

# -----------------------------
# Sync Session Factory
# -----------------------------
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)
