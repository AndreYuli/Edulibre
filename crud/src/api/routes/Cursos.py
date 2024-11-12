# src/api/routes/curso.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.schemas.Cursos import CursoCreate, CursoUpdate, Curso
from src.crud.Cursos import get_cursos, get_cursos, create_curso, update_curso, delete_curso
from src.api.deps import get_db
from typing import List

router = APIRouter()
@router.get("/", response_model=List[Curso])
def read_cursos(
    skip: int = 0,
    limit: int = 10,
    materia_id: int = Query(None),
    db: Session = Depends(get_db)
):
    cursos = get_cursos(db, skip=skip, limit=limit, materia_id=materia_id)
    return cursos

@router.post("/", response_model=Curso)
def create_new_curso(curso: CursoCreate, db: Session = Depends(get_db)):
    return create_curso(db=db, curso=curso)

@router.put("/{curso_id}", response_model=Curso)
def update_existing_curso(curso_id: int, curso: CursoUpdate, db: Session = Depends(get_db)):
    db_curso = update_curso(db=db, curso_id=curso_id, curso=curso)
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso not found")
    return db_curso

@router.delete("/{curso_id}", response_model=Curso)
def delete_existing_curso(curso_id: int, db: Session = Depends(get_db)):
    db_curso = delete_curso(db=db, curso_id=curso_id)
    if not db_curso:
        raise HTTPException(status_code=404, detail="Curso not found")
    return db_curso