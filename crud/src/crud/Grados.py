# src/crud/grado.py
from sqlalchemy.orm import Session
from src.models.Grados import Grado

def get_grados(db: Session, skip: int = 0, limit: int = 12):
    return db.query(Grado).offset(skip).limit(limit).all()