from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OpcionBase(BaseModel):
    pregunta_id: int
    texto_opcion: str
    es_correcta: bool

class OpcionCreate(OpcionBase):
    pass

class OpcionUpdate(OpcionBase):
    pass

class Opcion(OpcionBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True