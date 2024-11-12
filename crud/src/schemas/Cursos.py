# src/schemas/curso.py
from pydantic import BaseModel
from datetime import datetime

class CursoBase(BaseModel):
    materia_id: int
    nombre: str

class CursoCreate(CursoBase):
    pass

class CursoUpdate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True