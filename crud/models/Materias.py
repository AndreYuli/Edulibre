from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    
    cursos = relationship("Curso", back_populates="materia")

