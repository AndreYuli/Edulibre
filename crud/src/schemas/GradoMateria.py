# src/schemas/grado_materia.py
from pydantic import BaseModel

class GradoMateriaBase(BaseModel):
    grado_id: int
    materia_id: int

class GradoMateriaCreate(GradoMateriaBase):
    pass

class GradoMateriaUpdate(GradoMateriaBase):
    pass

class GradoMateria(GradoMateriaBase):
    id: int

    class Config:
        from_attributes = True