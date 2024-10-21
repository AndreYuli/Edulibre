from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from .Materias import Materia

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False)
    
    materia = relationship("Materia", back_populates="cursos")
