from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    cedula: int
    edad: Optional[int] = None
    nombre: str
    correo: EmailStr
    rol: str

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(UsuarioBase):
    contrasena: Optional[str] = None

class UsuarioInDBBase(UsuarioBase):
    id: int
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    class Config:
        from_attributes = True

class Usuario(UsuarioInDBBase):
    pass

class UsuarioInDB(UsuarioInDBBase):
    contrasena_hash: str

class ForgotPasswordRequest(BaseModel):
    correo: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    nueva_contrasena: str