from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.Progresos import ProgresoBase, ProgresoCreate, ProgresoUpdate, Progreso
from src.models import Progresos
from src.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[Progreso])
def get_progresos(db: Session = Depends(get_db)):
    progresos = db.query(Progresos).all()
    if not progresos:
        raise HTTPException(status_code=404, detail="No se encontraron progresos")
    return progresos

@router.post("/", response_model=Progreso)
def create_progreso(progreso: ProgresoCreate, db: Session = Depends(get_db)):
    db_progreso = Progresos(usuario_id=progreso.usuario_id, leccion_id=progreso.leccion_id, estado=progreso.estado)
    db.add(db_progreso)
    db.commit()
    db.refresh(db_progreso)
    return db_progreso

@router.put("/{id}", response_model=Progreso)
def update_progreso(id: int, progreso: ProgresoUpdate, db: Session = Depends(get_db)):
    db_progreso = db.query(Progresos).filter(Progresos.id == id).first()
    if not db_progreso:
        raise HTTPException(status_code=404, detail="Progreso no encontrado")
    db_progreso.usuario_id = progreso.usuario_id
    db_progreso.leccion_id = progreso.leccion_id
    db_progreso.estado = progreso.estado
    db.commit()
    db.refresh(db_progreso)
    return db_progreso

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_progreso(id: int, db: Session = Depends(get_db)):
    progreso = db.query(Progresos).filter(Progresos.id == id).first()
    if not progreso:
        raise HTTPException(status_code=404, detail="Progreso no encontrado")
    db.delete(progreso)
    db.commit()
    return