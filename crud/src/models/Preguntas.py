from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Pregunta(Base):
    __tablename__ = "preguntas"

    id = Column(Integer, primary_key=True, index=True)
    leccion_id = Column(Integer, ForeignKey("lecciones.id"))
    texto_pregunta = Column(Text)
    tipo_pregunta = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)