from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Respuesta(Base):
    __tablename__ = "respuestas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    pregunta_id = Column(Integer, ForeignKey("preguntas.id"))
    texto_respuesta = Column(Text, nullable=True)
    es_correcta = Column(Boolean)
    fecha = Column(DateTime, default=datetime.utcnow)