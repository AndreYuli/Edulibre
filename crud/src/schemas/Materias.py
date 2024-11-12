# src/schemas/materia.py
from pydantic import BaseModel

class MateriaBase(BaseModel):
    nombre: str

class MateriaCreate(MateriaBase):
    pass

class MateriaUpdate(MateriaBase):
    pass

class Materia(MateriaBase):
    id: int

    class Config:
        from_attributes = True