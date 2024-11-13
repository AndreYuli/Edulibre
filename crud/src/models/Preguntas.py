from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class Pregunta(Base):
    __tablename__ = "preguntas"

    id = Column(Integer, primary_key=True, index=True)  # Use Integer for BIGSERIAL
    leccion_id = Column(Integer, ForeignKey("lecciones.id"), nullable=False)  # Foreign key
    texto = Column(Text, nullable=False)  # Match the field name and not null constraint
    tipo = Column(String, nullable=False)  # Match the field name and not null constraint
    creado_en = Column(DateTime, default=datetime.utcnow)  # Match the default value