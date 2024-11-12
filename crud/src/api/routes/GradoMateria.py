# src/api/routes/grado_materia.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.GradoMateria import GradoMateriaCreate, GradoMateriaUpdate, GradoMateria
from src.crud.GradoMateria import get_grado_materia, get_grado_materias, create_grado_materia, update_grado_materia, delete_grado_materia
from src.api.deps import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[GradoMateria])
def read_grado_materias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    grado_materias = get_grado_materias(db, skip=skip, limit=limit)
    return grado_materias

@router.post("/", response_model=GradoMateria)
def create_new_grado_materia(grado_materia: GradoMateriaCreate, db: Session = Depends(get_db)):
    return create_grado_materia(db=db, grado_materia=grado_materia)

@router.put("/{grado_materia_id}", response_model=GradoMateria)
def update_existing_grado_materia(grado_materia_id: int, grado_materia: GradoMateriaUpdate, db: Session = Depends(get_db)):
    db_grado_materia = update_grado_materia(db=db, grado_materia_id=grado_materia_id, grado_materia=grado_materia)
    if not db_grado_materia:
        raise HTTPException(status_code=404, detail="GradoMateria not found")
    return db_grado_materia

@router.delete("/{grado_materia_id}", response_model=GradoMateria)
def delete_existing_grado_materia(grado_materia_id: int, db: Session = Depends(get_db)):
    db_grado_materia = delete_grado_materia(db=db, grado_materia_id=grado_materia_id)
    if not db_grado_materia:
        raise HTTPException(status_code=404, detail="GradoMateria not found")
    return db_grado_materia