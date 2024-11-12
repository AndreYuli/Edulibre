from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExamenBase(BaseModel):
    curso_id: int
    titulo: str
    preguntas: str

class ExamenCreate(ExamenBase):
    pass

class ExamenUpdate(ExamenBase):
    pass

class Examen(ExamenBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True