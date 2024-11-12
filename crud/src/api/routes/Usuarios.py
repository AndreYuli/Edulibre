import secrets
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.Usuarios import UsuarioCreate, Usuario, ForgotPasswordRequest, ResetPasswordRequest, UsuarioUpdate
from src.api.deps import get_db
from src.crud.Usuarios import (
    get_usuarios, create_usuario, authenticate_user, create_access_token,
    update_usuario, delete_usuario, get_usuario, get_usuario_by_correo, validate_password, get_password_hash
)
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta
from src.core.config import settings

router = APIRouter()

password_reset_tokens = {}

@router.get("/", response_model=List[Usuario])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = get_usuarios(db, skip=skip, limit=limit)
    return usuarios

@router.post("/", response_model=Usuario)
def create_new_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if not validate_password(usuario.contrasena):
        raise HTTPException(status_code=400, detail="La contraseña no cumple con los requisitos de seguridad")
    if get_usuario_by_correo(db, usuario.correo):
        raise HTTPException(status_code=400, detail="El correo electrónico ya está registrado")
    return create_usuario(db=db, usuario=usuario)

@router.put("/{usuario_id}", response_model=Usuario)
def update_existing_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = update_usuario(db=db, usuario_id=usuario_id, usuario=usuario)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.delete("/{usuario_id}", response_model=Usuario)
def delete_existing_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = delete_usuario(db=db, usuario_id=usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect correo or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/forgot-password")
async def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = get_usuario_by_correo(db, request.correo)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Genera un token único
    token = secrets.token_urlsafe(32)
    
    # Almacena el token con un tiempo de expiración (30 minutos)
    password_reset_tokens[token] = {
        "user_id": user.id,
        "expiry": datetime.utcnow() + timedelta(minutes=30)
    }
    
    # Crea un enlace que dirija a la página de restablecimiento de contraseña en tu frontend
    reset_link = f"http://localhost:5173/reset-password?token={token}"
    return {
        "message": "Password reset token generated",
        "reset_link": reset_link
    }   

@router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    token_data = password_reset_tokens.get(request.token)
    if not token_data:
        raise HTTPException(status_code=400, detail="Invalid token")
    
    if datetime.utcnow() > token_data["expiry"]:
        del password_reset_tokens[request.token]
        raise HTTPException(status_code=400, detail="Token has expired")
    
    user = get_usuario(db, token_data["user_id"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = get_password_hash(request.nueva_contrasena)
    user.contrasena_hash = hashed_password
    db.commit()

    del password_reset_tokens[request.token]
    
    return {"message": "Password has been reset successfully"}