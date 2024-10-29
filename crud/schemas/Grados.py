from pydantic import BaseModel

class GradoSchema(BaseModel):
    id: int
    nombre: str
    numero: int

    class Config:
        from_attributes = True