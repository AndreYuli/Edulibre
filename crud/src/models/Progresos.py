from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Progreso(Base):
    __tablename__ = "progresos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    leccion_id = Column(Integer, ForeignKey("lecciones.id"))
    estado = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)