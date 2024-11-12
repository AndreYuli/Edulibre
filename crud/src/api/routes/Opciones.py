from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas import OpcionSchema
from models import Opcion
from api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[OpcionSchema])
def get_opciones(db: Session = Depends(get_db)):
    opciones = db.query(Opcion).all()
    if not opciones:
        raise HTTPException(status_code=404, detail="No se encontraron opciones")
    return opciones

@router.post("/", response_model=OpcionSchema)
def create_opcion(opcion: OpcionSchema, db: Session = Depends(get_db)):
    db_opcion = Opcion(pregunta_id=opcion.pregunta_id, texto_opcion=opcion.texto_opcion, es_correcta=opcion.es_correcta)
    db.add(db_opcion)
    db.commit()
    db.refresh(db_opcion)
    return db_opcion

@router.put("/{id}", response_model=OpcionSchema)
def update_opcion(id: int, opcion: OpcionSchema, db: Session = Depends(get_db)):
    db_opcion = db.query(Opcion).filter(Opcion.id == id).first()
    if not db_opcion:
        raise HTTPException(status_code=404, detail="Opción no encontrada")
    db_opcion.pregunta_id = opcion.pregunta_id
    db_opcion.texto_opcion = opcion.texto_opcion
    db_opcion.es_correcta = opcion.es_correcta
    db.commit()
    db.refresh(db_opcion)
    return db_opcion

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_opcion(id: int, db: Session = Depends(get_db)):
    opcion = db.query(Opcion).filter(Opcion.id == id).first()
    if not opcion:
        raise HTTPException(status_code=404, detail="Opción no encontrada")
    db.delete(opcion)
    db.commit()
    return
