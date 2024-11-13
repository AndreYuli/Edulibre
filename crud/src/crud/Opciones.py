from sqlalchemy.orm import Session
from models import Opcion
from src.schemas.Opciones import OpcionCreate, OpcionUpdate

def get_opcion(db: Session, opcion_id: int):
    return db.query(Opcion).filter(Opcion.id == opcion_id).first()

def get_opciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Opcion).offset(skip).limit(limit).all()

def create_opcion(db: Session, opcion: OpcionCreate):
    db_opcion = Opcion(**opcion.dict())
    db.add(db_opcion)
    db.commit()
    db.refresh(db_opcion)
    return db_opcion

def update_opcion(db: Session, opcion_id: int, opcion: OpcionUpdate):
    db_opcion = db.query(Opcion).filter(Opcion.id == opcion_id).first()
    if db_opcion:
        for key, value in opcion.dict().items():
            setattr(db_opcion, key, value)
        db.commit()
        db.refresh(db_opcion)
    return db_opcion

def delete_opcion(db: Session, opcion_id: int):
    db_opcion = db.query(Opcion).filter(Opcion.id == opcion_id).first()
    if db_opcion:
        db.delete(db_opcion)
        db.commit()
    return db_opcion
