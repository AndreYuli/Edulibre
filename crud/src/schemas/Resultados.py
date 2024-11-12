from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ResultadoBase(BaseModel):
    examen_id: int
    usuario_id: int
    puntaje: int

class ResultadoCreate(ResultadoBase):
    pass

class ResultadoUpdate(ResultadoBase):
    pass

class Resultado(ResultadoBase):
    id: int
    fecha: Optional[datetime] = None

    class Config:
        from_attributes = True