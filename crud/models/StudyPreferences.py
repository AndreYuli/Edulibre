from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class StudyPreference(Base):
    __tablename__ = "study_preferences"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"), nullable=False)
    preferencia = Column(String(20), nullable=False)

    usuario = relationship("Usuario", back_populates="study_preferences")  # Adjust based on your User model
