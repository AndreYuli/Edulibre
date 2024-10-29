from pydantic import BaseModel

class MateriaSchema(BaseModel):
    id: int
    nombre: str
    # Otros campos que ya tengas...

    class Config:
        from_attributes = True

class MateriaNombreSchema(BaseModel):
    nombre: str

    class Config:
        from_attributes = True