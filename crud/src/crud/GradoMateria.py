# src/crud/grado_materia.py
from sqlalchemy.orm import Session
from src.models.GradoMateria import GradoMateria
from src.schemas.GradoMateria import GradoMateriaCreate, GradoMateriaUpdate

def get_grado_materia(db: Session, grado_materia_id: int):
    return db.query(GradoMateria).filter(GradoMateria.id == grado_materia_id).first()

def get_grado_materias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(GradoMateria).offset(skip).limit(limit).all()

def create_grado_materia(db: Session, grado_materia: GradoMateriaCreate):
    db_grado_materia = GradoMateria(**grado_materia.dict())
    db.add(db_grado_materia)
    db.commit()
    db.refresh(db_grado_materia)
    return db_grado_materia

def update_grado_materia(db: Session, grado_materia_id: int, grado_materia: GradoMateriaUpdate):
    db_grado_materia = db.query(GradoMateria).filter(GradoMateria.id == grado_materia_id).first()
    if db_grado_materia:
        for key, value in grado_materia.dict().items():
            setattr(db_grado_materia, key, value)
        db.commit()
        db.refresh(db_grado_materia)
    return db_grado_materia

def delete_grado_materia(db: Session, grado_materia_id: int):
    db_grado_materia = db.query(GradoMateria).filter(GradoMateria.id == grado_materia_id).first()
    if db_grado_materia:
        db.delete(db_grado_materia)
        db.commit()
    return db_grado_materia