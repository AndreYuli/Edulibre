# src/api/routes/grado.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.Grados import Grado
from src.crud.Grados import get_grados
from src.api.deps import get_db
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Grado])
def read_grados(skip: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    grados = get_grados(db, skip=skip, limit=limit)
    return grados