from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    knowledge_level = Column(String)  # e.g., beginner, intermediate, advanced
    subject = Column(String)  # e.g., Mechanical Engineering
    misconceptions = Column(Text)  # Stores misconceptions identified

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    question = Column(Text)
    response = Column(Text)
    context = Column(Text)
