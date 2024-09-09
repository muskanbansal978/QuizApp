from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

# Defines the Questions table with columns and metadata
class Questions(Base):
    __tablename__ = 'questions'  # Sets the table name in the database

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    choices = relationship('Choices',back_populates='question',cascade='all,delete-orphan')

# Defines the Choices table with columns and relationships
class Choices(Base):
    __tablename__ = 'choices'  # Sets the table name in the database

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Questions',back_populates='choices')
