from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RespuestaBase(BaseModel):
    usuario_id: int
    pregunta_id: int
    texto_respuesta: Optional[str] = None
    es_correcta: bool

class RespuestaCreate(RespuestaBase):
    pass

class RespuestaUpdate(RespuestaBase):
    pass

class RespuestaSchema(RespuestaBase):
    id: int
    fecha: Optional[datetime] = None

    class Config:
        from_attributes = True