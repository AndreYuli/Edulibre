from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from schemas import ResultadoSchema
from models import Resultado
from api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[ResultadoSchema])
def get_resultados(db: Session = Depends(get_db)):
    resultados = db.query(Resultado).all()
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron resultados")
    return resultados

@router.post("/", response_model=ResultadoSchema)
def create_resultado(resultado: ResultadoSchema, db: Session = Depends(get_db)):
    db_resultado = Resultado(examen_id=resultado.examen_id, usuario_id=resultado.usuario_id, puntaje=resultado.puntaje)
    db.add(db_resultado)
    db.commit()
    db.refresh(db_resultado)
    return db_resultado

@router.put("/{id}", response_model=ResultadoSchema)
def update_resultado(id: int, resultado: ResultadoSchema, db: Session = Depends(get_db)):
    db_resultado = db.query(Resultado).filter(Resultado.id == id).first()
    if not db_resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    db_resultado.examen_id = resultado.examen_id
    db_resultado.usuario_id = resultado.usuario_id
    db_resultado.puntaje = resultado.puntaje
    db.commit()
    db.refresh(db_resultado)
    return db_resultado

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_resultado(id: int, db: Session = Depends(get_db)):
    resultado = db.query(Resultado).filter(Resultado.id == id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    db.delete(resultado)
    db.commit()
    return