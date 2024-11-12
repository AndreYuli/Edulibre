from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas import RespuestaSchema
from models import Respuesta
from api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[RespuestaSchema])
def get_respuestas(db: Session = Depends(get_db)):
    respuestas = db.query(Respuesta).all()
    if not respuestas:
        raise HTTPException(status_code=404, detail="No se encontraron respuestas")
    return respuestas

@router.post("/", response_model=RespuestaSchema)
def create_respuesta(respuesta: RespuestaSchema, db: Session = Depends(get_db)):
    db_respuesta = Respuesta(usuario_id=respuesta.usuario_id, pregunta_id=respuesta.pregunta_id, texto_respuesta=respuesta.texto_respuesta, es_correcta=respuesta.es_correcta)
    db.add(db_respuesta)
    db.commit()
    db.refresh(db_respuesta)
    return db_respuesta

@router.put("/{id}", response_model=RespuestaSchema)
def update_respuesta(id: int, respuesta: RespuestaSchema, db: Session = Depends(get_db)):
    db_respuesta = db.query(Respuesta).filter(Respuesta.id == id).first()
    if not db_respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    db_respuesta.usuario_id = respuesta.usuario_id
    db_respuesta.pregunta_id = respuesta.pregunta_id
    db_respuesta.texto_respuesta = respuesta.texto_respuesta
    db_respuesta.es_correcta = respuesta.es_correcta
    db.commit()
    db.refresh(db_respuesta)
    return db_respuesta

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_respuesta(id: int, db: Session = Depends(get_db)):
    respuesta = db.query(Respuesta).filter(Respuesta.id == id).first()
    if not respuesta:
        raise HTTPException(status_code=404, detail="Respuesta no encontrada")
    db.delete(respuesta)
    db.commit()
    return