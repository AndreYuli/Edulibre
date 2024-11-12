from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Resultado(Base):
    __tablename__ = "resultados"

    id = Column(Integer, primary_key=True, index=True)
    examen_id = Column(Integer, ForeignKey("examenes.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    puntaje = Column(Integer)
    fecha = Column(DateTime, default=datetime.utcnow)