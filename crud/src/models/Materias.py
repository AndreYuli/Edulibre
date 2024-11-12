# src/models/materia.py
from sqlalchemy import Column, Integer, String
from src.db.base_class import Base

class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, unique=True)