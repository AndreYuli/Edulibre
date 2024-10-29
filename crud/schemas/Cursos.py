from pydantic import BaseModel

class CursoSchema(BaseModel):
    id: int
    nombre: str
    materia_id: int

    class Config:
        from_attributes = True