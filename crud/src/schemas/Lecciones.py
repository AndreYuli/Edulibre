# In src/schemas/Lecciones.py
from pydantic import BaseModel

class Leccion(BaseModel):
    id: int
    title: str
    content: str