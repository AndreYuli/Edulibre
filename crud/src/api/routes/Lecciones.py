# In src/api/routes/Lecciones.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.Lecciones import Leccion as LeccionSchema  # Pydantic model
from src.models.Lecciones import Leccion as LeccionModel  # SQLAlchemy model
from src.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[LeccionSchema])  # Use Pydantic model for response
def get_lecciones(db: Session = Depends(get_db)):
    lecciones = db.query(LeccionModel).all()  # Use SQLAlchemy model for DB query
    if not lecciones:
        raise HTTPException(status_code=404, detail="No se encontraron lecciones")
    return lecciones

@router.post("/", response_model=LeccionSchema)  # Use Pydantic model for response
def create_leccion(leccion: LeccionSchema, db: Session = Depends(get_db)):
    db_leccion = LeccionModel(curso_id=leccion.curso_id, titulo=leccion.titulo, contenido=leccion.contenido)  # Use SQLAlchemy model
    db.add(db_leccion)
    db.commit()
    db.refresh(db_leccion)
    return db_leccion

@router.put("/{id}", response_model=LeccionSchema)  # Use Pydantic model for response
def update_leccion(id: int, leccion: LeccionSchema, db: Session = Depends(get_db)):
    db_leccion = db.query(LeccionModel).filter(LeccionModel.id == id).first()  # Use SQLAlchemy model
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
    leccion = db.query(LeccionModel).filter(LeccionModel.id == id).first()  # Use SQLAlchemy model
    if not leccion:
        raise HTTPException(status_code=404, detail="Lección no encontrada")
    db.delete(leccion)
    db.commit()
    return  # No content to return