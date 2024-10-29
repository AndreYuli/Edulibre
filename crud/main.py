# FastAPI y dependencias
from fastapi import FastAPI, HTTPException, Depends, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# SQLAlchemy
from sqlalchemy import create_engine, select, distinct
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

# Pydantic
from pydantic import BaseModel, EmailStr

# JWT
from jose import JWTError, jwt

# Fechas y secretos
from datetime import datetime, timedelta
import secrets
import os
import bcrypt

# Modelos y esquemas
from config import DATABASE_URL
from models.Usuarios import Usuario
from schemas.Usuarios import UsuarioModel, UsuarioCreate, UsuarioResponse
from models.Materias import Materia
from models.Grados import Grado
from models.Cursos import Curso
from schemas.Materias import MateriaSchema, MateriaNombreSchema
from schemas.Grados import GradoSchema
from schemas.Cursos import CursoSchema
from models.StudyPreferences import StudyPreference
from schemas.StudyPreferences import StudyPreferencesSchema

# Typing
from typing import List, Literal, Optional

# Logging
import logging

# Configuración de logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {
        "message": "Hello, this is my app"
    }
    
@app.get("/api/v1/usuarios", response_model=List[UsuarioModel])
def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@app.post("/api/v1/usuarios", response_model=UsuarioModel)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if not validate_password(usuario.contraseña):
        raise HTTPException(status_code=400, detail="Password does not meet security requirements")
    try:
        hashed_password = get_password_hash(usuario.contraseña)
        db_usuario = Usuario(
            cedula=usuario.cedula,
            edad=usuario.edad,
            nombre=usuario.nombre,
            email=usuario.email,
            contraseña=hashed_password,
            rol=usuario.rol,
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate entry or constraint violation")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

pwd_context = bcrypt
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def authenticate_user(db: Session, cedula: str, password: str):
    user = db.query(Usuario).filter(Usuario.cedula == cedula).first()
    if not user:
        return False
    if not verify_password(password, user.contraseña):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = db.query(Usuario).filter(Usuario.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    return user

# Rutas de autenticación y usuarios
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect cedula or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.cedula)},  # Convertimos la cédula a string
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

def hash_existing_passwords(db: Session):
    usuarios = db.query(Usuario).all()
    for usuario in usuarios:
        if not usuario.contraseña.startswith('$2b$'):  # Check if it's already a bcrypt hash
            hashed_password = get_password_hash(usuario.contraseña)
            usuario.contraseña = hashed_password
    db.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    init_db()
    db = SessionLocal()
    hash_existing_passwords(db)
    db.close()

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
password_reset_tokens = {}

@app.post("/api/forgot-password")
async def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == request.email).first()
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

@app.post("/api/reset-password")
async def reset_password(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    token_data = password_reset_tokens.get(request.token)
    if not token_data:
        raise HTTPException(status_code=400, detail="Invalid token")
    
    if datetime.utcnow() > token_data["expiry"]:
        del password_reset_tokens[request.token]
        raise HTTPException(status_code=400, detail="Token has expired")
    
    user = db.query(Usuario).filter(Usuario.id == token_data["user_id"]).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = get_password_hash(request.new_password)
    user.contraseña = hashed_password
    db.commit()

    del password_reset_tokens[request.token]
    
    return {"message": "Password has been reset successfully"}

def validate_password(password: str) -> bool:
    return (len(password) >= 8 and 
            any(c.isdigit() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.islower() for c in password) and 
            any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))

@app.get("/api/v1/materias", response_model=List[MateriaSchema])
def get_materias(grado_id: Optional[int] = Query(None, description="ID del grado para filtrar materias"), db: Session = Depends(get_db)):
    query = db.query(Materia)
    if grado_id is not None:
        query = query.filter(Materia.grado_id == grado_id)
    materias = query.all()
    if not materias:
        raise HTTPException(status_code=404, detail="No se encontraron materias")
    return materias

@app.get("/api/v1/materias/nombres", response_model=List[MateriaNombreSchema])
def get_nombres_materias(db: Session = Depends(get_db)):
    query = select(distinct(Materia.nombre)).order_by(Materia.nombre)
    result = db.execute(query)
    nombres_materias = [{"nombre": row[0]} for row in result]
    
    if not nombres_materias:
        raise HTTPException(status_code=404, detail="No se encontraron materias")
    return nombres_materias


@app.get("/api/v1/grados", response_model=List[GradoSchema])
def get_grados(db: Session = Depends(get_db)):
    query = select(Grado.id, Grado.nombre).order_by(Grado.id)
    result = db.execute(query)
    grados = [{"id": row.id, "nombre": row.nombre, "numero": row.id} for row in result]
    
    if not grados:
        raise HTTPException(status_code=404, detail="No se encontraron grados")
    return grados


        
@app.get("/api/v1/cursos", response_model=List[CursoSchema])
def get_cursos(db: Session = Depends(get_db)):
    cursos = db.query(Curso).all()
    if not cursos:
        # Log the number of courses found
        curso_count = db.query(Curso).count()
        print(f"Number of courses in database: {curso_count}")
        raise HTTPException(status_code=404, detail=f"No se encontraron cursos. Total en base de datos: {curso_count}")
    return cursos

@app.post("/api/v1/cursos", response_model=CursoSchema)
def create_curso(curso: CursoSchema, db: Session = Depends(get_db)):
    db_curso = Curso(nombre=curso.nombre, materia_id=curso.materia_id)
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

@app.put("/api/v1/cursos/{id}", response_model=CursoSchema)
def update_curso(id: int, curso: CursoSchema, db: Session = Depends(get_db)):
    db_curso = db.query(Curso).filter(Curso.id == id).first()
    db_curso.nombre = curso.nombre
    db_curso.materia_id = curso.materia_id
    db.commit()
    db.refresh(db_curso)    
    return db_curso

@app.delete("/api/v1/cursos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_curso(id: int, db: Session = Depends(get_db)):
    curso = db.query(Curso).filter(Curso.id == id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso not found")
    db.delete(curso)
    db.commit()
    return

@app.get("/api/v1/db-check")
def check_db_connection(db: Session = Depends(get_db)):
    try:
        # Try to execute a simple query
        result = db.execute("SELECT 1").scalar()
        return {"status": "Database connection successful", "result": result}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}
    
@app.post('/api/v1/user-preferences', response_model=StudyPreferencesSchema)
def save_user_preferences(study_preferences: StudyPreferencesSchema, db: Session = Depends(get_db)):
    logging.info(f"Received preferences: {study_preferences}")
    try:
        user_preferences = db.query(StudyPreference).filter(StudyPreference.usuario_id == study_preferences.usuario_id).first()
        if user_preferences:
            user_preferences.preferencia = study_preferences.preferencia
        else:
            user_preferences = StudyPreference(
                usuario_id=study_preferences.usuario_id,
                preferencia=study_preferences.preferencia
            )
        db.add(user_preferences)
        db.commit()
        db.refresh(user_preferences)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=409, detail="Conflict: User preference already exists")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return user_preferences



