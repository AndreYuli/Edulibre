from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PreguntaBase(BaseModel):
    leccion_id: int
    texto_pregunta: str
    tipo_pregunta: str

class PreguntaCreate(PreguntaBase):
    pass

class PreguntaUpdate(PreguntaBase):
    pass

class Pregunta(PreguntaBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True