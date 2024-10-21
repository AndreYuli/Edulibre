from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(Integer, unique=True, index=True)
    edad = Column(Integer, nullable=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contraseña = Column(String, nullable=False)
    rol = Column(String, CheckConstraint("rol IN ('Estudiante', 'Administrador')"), nullable=False)