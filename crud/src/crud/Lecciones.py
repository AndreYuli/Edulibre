from sqlalchemy.orm import Session
from models import Leccion
from src.schemas.Lecciones import LeccionCreate, LeccionUpdate

def get_leccion(db: Session, leccion_id: int):
    return db.query(Leccion).filter(Leccion.id == leccion_id).first()

def get_lecciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Leccion).offset(skip).limit(limit).all()

def create_leccion(db: Session, leccion: LeccionCreate):
    db_leccion = Leccion(**leccion.dict())
    db.add(db_leccion)
    db.commit()
    db.refresh(db_leccion)
    return db_leccion

def update_leccion(db: Session, leccion_id: int, leccion: LeccionUpdate):
    db_leccion = db.query(Leccion).filter(Leccion.id == leccion_id).first()
    if db_leccion:
        for key, value in leccion.dict().items():
            setattr(db_leccion, key, value)
        db.commit()
        db.refresh(db_leccion)
    return db_leccion

def delete_leccion(db: Session, leccion_id: int):
    db_leccion = db.query(Leccion).filter(Leccion.id == leccion_id).first()
    if db_leccion:
        db.delete(db_leccion)
        db.commit()
    return db_leccion