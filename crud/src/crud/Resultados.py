from sqlalchemy.orm import Session
from src.models.Resultados import Resultado
from src.schemas.Resultados import ResultadoCreate, ResultadoUpdate

def get_resultado(db: Session, resultado_id: int):
    return db.query(Resultado).filter(Resultado.id == resultado_id).first()

def get_resultados(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Resultado).offset(skip).limit(limit).all()

def create_resultado(db: Session, resultado: ResultadoCreate):
    db_resultado = Resultado(**resultado.dict())
    db.add(db_resultado)
    db.commit()
    db.refresh(db_resultado)
    return db_resultado

def update_resultado(db: Session, resultado_id: int, resultado: ResultadoUpdate):
    db_resultado = db.query(Resultado).filter(Resultado.id == resultado_id).first()
    if db_resultado:
        for key, value in resultado.dict().items():
            setattr(db_resultado, key, value)
        db.commit()
        db.refresh(db_resultado)
    return db_resultado

def delete_resultado(db: Session, resultado_id: int):
    db_resultado = db.query(Resultado).filter(Resultado.id == resultado_id).first()
    if db_resultado:
        db.delete(db_resultado)
        db.commit()
    return db_resultado