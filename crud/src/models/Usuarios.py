from sqlalchemy import Column, Integer, DateTime, CheckConstraint, Text
from datetime import datetime
from src.db.base_class import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(Integer, unique=True, nullable=False)
    edad = Column(Integer, CheckConstraint('edad >= 0'), nullable=True)
    nombre = Column(Text, nullable=False)
    correo = Column(Text, unique=True, nullable=False)
    contrasena_hash = Column(Text, nullable=False)
    rol = Column(Text, CheckConstraint("rol IN ('Estudiante', 'Administrador')"), nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)