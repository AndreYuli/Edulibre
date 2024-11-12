# src/models/curso.py
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    materia_id = Column(BigInteger, ForeignKey('materias.id', ondelete='SET NULL'), nullable=False)
    nombre = Column(String, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)