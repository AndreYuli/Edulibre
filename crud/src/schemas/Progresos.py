from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProgresoBase(BaseModel):
    usuario_id: int
    leccion_id: int
    estado: str

class ProgresoCreate(ProgresoBase):
    pass

class ProgresoUpdate(ProgresoBase):
    pass

class Progreso(ProgresoBase):
    id: int
    fecha: Optional[datetime] = None

    class Config:
        from_attributes = True