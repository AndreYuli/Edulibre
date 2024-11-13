# In crud/src/crud/Preguntas.py
from sqlalchemy.orm import Session
from src.models.Preguntas import Pregunta as PreguntaModel  # SQLAlchemy model
from src.schemas.Preguntas import Pregunta as PreguntaSchema  # Pydantic model

def get_pregunta(db: Session, pregunta_id: int):
    """Retrieve a single Pregunta by ID."""
    return db.query(PreguntaModel).filter(PreguntaModel.id == pregunta_id).first()

def get_preguntas(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve a list of Preguntas with pagination."""
    return db.query(PreguntaModel).offset(skip).limit(limit).all()

def create_pregunta(db: Session, pregunta: PreguntaSchema):
    """Create a new Pregunta."""
    db_pregunta = PreguntaModel(
        leccion_id=pregunta.leccion_id,
        texto=pregunta.texto,
        tipo=pregunta.tipo
    )
    db.add(db_pregunta)
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

def update_pregunta(db: Session, pregunta_id: int, pregunta: PreguntaSchema):
    """Update an existing Pregunta."""
    db_pregunta = db.query(PreguntaModel).filter(PreguntaModel.id == pregunta_id).first()
    if db_pregunta:
        db_pregunta.leccion_id = pregunta.leccion_id
        db_pregunta.texto = pregunta.texto
        db_pregunta.tipo = pregunta.tipo
        db.commit()
        db.refresh(db_pregunta)
    return db_pregunta

def delete_pregunta(db: Session, pregunta_id: int):
    """Delete a Pregunta by ID."""
    db_pregunta = db.query(PreguntaModel).filter(PreguntaModel.id == pregunta_id).first()
    if db_pregunta:
        db.delete(db_pregunta)
        db.commit()
    return db_pregunta