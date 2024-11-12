from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings
from src.api.routes.Usuarios import router as usuarios_router
from src.api.routes.StudyPreferences import router as study_preferences_router
from src.api.routes.Materias import router as materias_router
from src.api.routes.Grados import router as grados_router
from src.api.routes.Cursos import router as cursos_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Configure CORS
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router, prefix="/api/v1/usuarios", tags=["usuarios"])
app.include_router(study_preferences_router, prefix="/api/v1/study-preferences", tags=["study-preferences"])
app.include_router(grados_router, prefix="/api/v1/grados", tags=["grados"])
app.include_router(materias_router, prefix="/api/v1/materias", tags=["materias"])
app.include_router(cursos_router, prefix="/api/v1/cursos", tags=["cursos"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}