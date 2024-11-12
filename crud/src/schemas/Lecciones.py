from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LeccionBase(BaseModel):
    curso_id: int
    titulo: str
    contenido: str

class LeccionCreate(LeccionBase):
    pass

class LeccionUpdate(LeccionBase):
    pass

class Leccion(LeccionBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True