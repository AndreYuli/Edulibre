from sqlalchemy import Column, Integer, String
from src.db.base_class import Base

class Grado(Base):
    __tablename__ = "grados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)