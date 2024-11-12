# src/models/grado_materia.py
from sqlalchemy import Column, BigInteger, ForeignKey, UniqueConstraint
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class GradoMateria(Base):
    __tablename__ = "grado_materia"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    grado_id = Column(BigInteger, ForeignKey('grados.id', ondelete='CASCADE'), nullable=False)
    materia_id = Column(BigInteger, ForeignKey('materias.id', ondelete='CASCADE'), nullable=False)

    __table_args__ = (UniqueConstraint('grado_id', 'materia_id', name='_grado_materia_uc'),)

    grado = relationship('Grado', back_populates='grado_materias')
    materia = relationship('Materia', back_populates='grado_materias')