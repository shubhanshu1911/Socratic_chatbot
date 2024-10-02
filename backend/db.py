from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
import os

# Database URL configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy Base
Base = declarative_base()

# Define a sample model (e.g., Student)
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    name = Column(String(50))
    knowledge_level = Column(String(50))

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Utility functions for database operations
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

# Create tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
