# src/crud/materia.py
from sqlalchemy.orm import Session
from src.models.Materias import Materia

def get_materias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Materia).offset(skip).limit(limit).all()