from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas import PreguntaSchema
from models import Pregunta
from api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[PreguntaSchema])
def get_preguntas(db: Session = Depends(get_db)):
    preguntas = db.query(Pregunta).all()
    if not preguntas:
        raise HTTPException(status_code=404, detail="No se encontraron preguntas")
    return preguntas

@router.post("/", response_model=PreguntaSchema)
def create_pregunta(pregunta: PreguntaSchema, db: Session = Depends(get_db)):
    db_pregunta = Pregunta(leccion_id=pregunta.leccion_id, texto_pregunta=pregunta.texto_pregunta, tipo_pregunta=pregunta.tipo_pregunta)
    db.add(db_pregunta)
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

@router.put("/{id}", response_model=PreguntaSchema)
def update_pregunta(id: int, pregunta: PreguntaSchema, db: Session = Depends(get_db)):
    db_pregunta = db.query(Pregunta).filter(Pregunta.id == id).first()
    if not db_pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    db_pregunta.leccion_id = pregunta.leccion_id
    db_pregunta.texto_pregunta = pregunta.texto_pregunta
    db_pregunta.tipo_pregunta = pregunta.tipo_pregunta
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pregunta(id: int, db: Session = Depends(get_db)):
    pregunta = db.query(Pregunta).filter(Pregunta.id == id).first()
    if not pregunta:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    db.delete(pregunta)
    db.commit()
    return