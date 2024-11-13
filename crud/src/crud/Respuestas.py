from sqlalchemy.orm import Session
from src.models.Respuestas import Respuesta
from src.schemas.Respuestas import RespuestaCreate, RespuestaUpdate

def get_respuesta(db: Session, respuesta_id: int):
    return db.query(Respuesta).filter(Respuesta.id == respuesta_id).first()

def get_respuestas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Respuesta).offset(skip).limit(limit).all()

def create_respuesta(db: Session, respuesta: RespuestaCreate):
    db_respuesta = Respuesta(**respuesta.dict())
    db.add(db_respuesta)
    db.commit()
    db.refresh(db_respuesta)
    return db_respuesta

def update_respuesta(db: Session, respuesta_id: int, respuesta: RespuestaUpdate):
    db_respuesta = db.query(Respuesta).filter(Respuesta.id == respuesta_id).first()
    if db_respuesta:
        for key, value in respuesta.dict().items():
            setattr(db_respuesta, key, value)
        db.commit()
        db.refresh(db_respuesta)
    return db_respuesta

def delete_respuesta(db: Session, respuesta_id: int):
    db_respuesta = db.query(Respuesta).filter(Respuesta.id == respuesta_id).first()
    if db_respuesta:
        db.delete(db_respuesta)
        db.commit()
    return db_respuesta