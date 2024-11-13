# In crud/src/schemas/Preguntas.py
from pydantic import BaseModel
from typing import Optional

class Pregunta(BaseModel):
    id: int
    leccion_id: int  # Match the field name
    texto: str  # Match the field name
    tipo: str  # Match the field name
    creado_en: Optional[str] = None  # Optional field for created timestamp