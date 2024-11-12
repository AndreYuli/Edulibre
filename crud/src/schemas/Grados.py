from pydantic import BaseModel

class GradoBase(BaseModel):
    nombre: str

class Grado(GradoBase):
    id: int

    class Config:
        from_attributes = True