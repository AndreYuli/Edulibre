from typing import Optional, List
from sqlalchemy.orm import Session
from src.models.Usuarios import Usuario
from src.schemas.Usuarios import UsuarioCreate, UsuarioUpdate
from passlib.context import CryptContext
from datetime import datetime, timedelta
from src.core.config import settings
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_usuarios(db: Session, skip: int = 0, limit: int = 10) -> List[Usuario]:
    return db.query(Usuario).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuario_by_correo(db: Session, correo: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def create_usuario(db: Session, usuario: UsuarioCreate) -> Usuario:
    hashed_password = get_password_hash(usuario.contrasena)
    db_usuario = Usuario(
        cedula=usuario.cedula,
        edad=usuario.edad,
        nombre=usuario.nombre,
        correo=usuario.correo,
        contrasena_hash=hashed_password,
        rol=usuario.rol,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate) -> Optional[Usuario]:
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        for key, value in usuario.dict(exclude_unset=True).items():
            if key == "contrasena":
                value = get_password_hash(value)
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int) -> Optional[Usuario]:
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

def authenticate_user(db: Session, cedula: str, password: str) -> Optional[Usuario]:
    user = db.query(Usuario).filter(Usuario.cedula == cedula).first()
    if not user:
        return None
    if not verify_password(password, user.contrasena_hash):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def validate_password(password: str) -> bool:
    return (len(password) >= 8 and 
            any(c.isdigit() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.islower() for c in password) and 
            any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))
    