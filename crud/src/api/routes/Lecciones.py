from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas import LeccionSchema
from models import Leccion
from api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[LeccionSchema])
def get_lecciones(db: Session = Depends(get_db)):
    lecciones = db.query(Leccion).all()
    if not lecciones:
        raise HTTPException(status_code=404, detail="No se encontraron lecciones")
    return lecciones

@router.post("/", response_model=LeccionSchema)
def create_leccion(leccion: LeccionSchema, db: Session = Depends(get_db)):
    db_leccion = Leccion(curso_id=leccion.curso_id, titulo=leccion.titulo, contenido=leccion.contenido)
    db.add(db_leccion)
    db.commit()
    db.refresh(db_leccion)
    return db_leccion

@router.put("/{id}", response_model=LeccionSchema)
def update_leccion(id: int, leccion: LeccionSchema, db: Session = Depends(get_db)):
    db_leccion = db.query(Leccion).filter(Leccion.id == id).first()
    if not db_leccion:
        raise HTTPException(status_code=404, detail="Lección no encontrada")
    db_leccion.curso_id = leccion.curso_id
    db_leccion.titulo = leccion.titulo
    db_leccion.contenido = leccion.contenido
    db.commit()
    db.refresh(db_leccion)
    return db_leccion

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_leccion(id: int, db: Session = Depends(get_db)):
    leccion = db.query(Leccion).filter(Leccion.id == id).first()
    if not leccion:
        raise HTTPException(status_code=404, detail="Lección no encontrada")
    db.delete(leccion)
    db.commit()
    return