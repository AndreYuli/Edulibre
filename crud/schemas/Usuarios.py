from pydantic import BaseModel, EmailStr
from typing import Literal

class UsuarioModel(BaseModel):
    cedula: int
    edad: int | None
    nombre: str
    email: EmailStr
    contraseña: str
    rol: Literal["Estudiante", "Administrador"]

    class Config:
        from_attributes = True

class UsuarioCreate(UsuarioModel):
    pass

class UsuarioResponse(UsuarioModel):
    id: int

    class Config:
        from_attributes = True 
