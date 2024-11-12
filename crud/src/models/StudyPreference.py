from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.db.base_class import Base

class StudyPreference(Base):
    __tablename__ = "preferenciasestudio"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    preferencia = Column(String, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)