# In crud/src/api/routes/Preguntas.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.Preguntas import Pregunta as PreguntaSchema  # Pydantic model
from src.models.Preguntas import Pregunta as PreguntaModel  # SQLAlchemy model
from src.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[PreguntaSchema])  # Use Pydantic model for response
def get_preguntas(db: Session = Depends(get_db)):
    preguntas = db.query(PreguntaModel).all()  # Use SQLAlchemy model for DB query
    if not preguntas:
        raise HTTPException(status_code=404, detail="No se encontraron preguntas")
    return preguntas

@router.post("/", response_model=PreguntaSchema)  # Use Pydantic model for response
def create_pregunta(pregunta: PreguntaSchema, db: Session = Depends(get_db)):
    db_pregunta = PreguntaModel(leccion_id=pregunta.leccion_id, texto=pregunta.texto, tipo=pregunta.tipo)
    db.add(db_pregunta)
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

@router.put("/{id}", response_model=PreguntaSchema)  # Use Pydantic model for response
def update_pregunta(id: int, pregunta: PreguntaSchema, db: Session = Depends(get_db)):
    db_pregunta = db.query(PreguntaModel).filter(PreguntaModel.id == id).first()  # Use SQLAlchemy model
    if not db_pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    db_pregunta.leccion_id = pregunta.leccion_id
    db_pregunta.texto = pregunta.texto
    db_pregunta.tipo = pregunta.tipo
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pregunta(id: int, db: Session = Depends(get_db)):
    pregunta = db.query(PreguntaModel).filter(PreguntaModel.id == id).first()  # Use SQLAlchemy model
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    db.delete(pregunta)
    db.commit()
    return  # No content to return