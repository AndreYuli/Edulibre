from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.crud.Examenes import examen as crud_examen
from src.schemas.Examenes import ExamenCreate, Examen
from src.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=Examen)
def create_examen(examen: ExamenCreate, db: Session = Depends(get_db)):
    return crud_examen.create_examen(db=db, examen=examen)

@router.get("/{examen_id}", response_model=Examen)
def read_examen(examen_id: int, db: Session = Depends(get_db)):
    db_examen = crud_examen.get_examen(db, examen_id=examen_id)
    if db_examen is None:
        raise HTTPException(status_code=404, detail="Examen not found")
    return db_examen

@router.get("/", response_model=list[Examen])
def read_examenes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    examenes = crud_examen.get_examenes(db, skip=skip, limit=limit)
    return examenes

@router.put("/{examen_id}", response_model=Examen)
def update_examen(examen_id: int, examen: ExamenCreate, db: Session = Depends(get_db)):
    return crud_examen.update_examen(db=db, examen_id=examen_id, examen=examen)

@router.delete("/{examen_id}", response_model=Examen)
def delete_examen(examen_id: int, db: Session = Depends(get_db)):
    return crud_examen.delete_examen(db=db, examen_id=examen_id)