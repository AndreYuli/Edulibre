# src/api/routes/materia.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.Materias import Materia
from src.crud.Materias import get_materias
from src.api.deps import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Materia])
def read_materias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    materias = get_materias(db, skip=skip, limit=limit)
    return materias