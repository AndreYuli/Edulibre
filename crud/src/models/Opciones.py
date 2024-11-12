from sqlalchemy import Column, Integer, Text, Boolean, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Opcion(Base):
    __tablename__ = "opciones"

    id = Column(Integer, primary_key=True, index=True)
    pregunta_id = Column(Integer, ForeignKey("preguntas.id"))
    texto_opcion = Column(Text)
    es_correcta = Column(Boolean)
    created_at = Column(DateTime, default=datetime.utcnow)