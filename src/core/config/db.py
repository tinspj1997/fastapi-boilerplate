# app/db.py
import os
import uuid
from src.core.artifacts.constants.default import DefaultConfig
from sqlalchemy import create_engine, Text, BigInteger
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    Mapped,
    mapped_column,
)


engine = create_engine(
    DefaultConfig.DATABASE_URL,
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
