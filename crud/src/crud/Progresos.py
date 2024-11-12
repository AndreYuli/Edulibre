from sqlalchemy.orm import Session
from models import Progresos
from schemas import ProgresoCreate, ProgresoUpdate

def get_progreso(db: Session, progreso_id: int):
    return db.query(Progresos).filter(Progresos.id == progreso_id).first()

def get_progresos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Progresos).offset(skip).limit(limit).all()

def create_progreso(db: Session, progreso: ProgresoCreate):
    db_progreso = Progresos(**progreso.dict())
    db.add(db_progreso)
    db.commit()
    db.refresh(db_progreso)
    return db_progreso

def update_progreso(db: Session, progreso_id: int, progreso: ProgresoUpdate):
    db_progreso = db.query(Progresos).filter(Progresos.id == progreso_id).first()
    if db_progreso:
        for key, value in progreso.dict().items():
            setattr(db_progreso, key, value)
        db.commit()
        db.refresh(db_progreso)
    return db_progreso

def delete_progreso(db: Session, progreso_id: int):
    db_progreso = db.query(Progresos).filter(Progresos.id == progreso_id).first()
    if db_progreso:
        db.delete(db_progreso)
        db.commit()
    return db_progreso