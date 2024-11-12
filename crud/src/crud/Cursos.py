from sqlalchemy.orm import Session
from src.models.Cursos import Curso
from src.schemas.Cursos import CursoCreate, CursoUpdate

def get_cursos(db: Session, skip: int = 0, limit: int = 10, materia_id: int = None):
    query = db.query(Curso)
    if materia_id:
        query = query.filter(Curso.materia_id == materia_id)
    return query.offset(skip).limit(limit).all()

def create_curso(db: Session, curso: CursoCreate):
    db_curso = Curso(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

def update_curso(db: Session, curso_id: int, curso: CursoUpdate):
    db_curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if db_curso:
        for key, value in curso.dict().items():
            setattr(db_curso, key, value)
        db.commit()
        db.refresh(db_curso)
    return db_curso

def delete_curso(db: Session, curso_id: int):
    db_curso = db.query(Curso).filter(Curso.id == curso_id).first()
    if db_curso:
        db.delete(db_curso)
        db.commit()
    return db_curso