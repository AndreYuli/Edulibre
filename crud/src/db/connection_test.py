from sqlalchemy import create_engine
from src.core.config import settings

# Crear un motor de conexión
engine = create_engine(settings.DATABASE_URL)

# Función de prueba de conexión
def test_db_connection():
    try:
        with engine.connect() as connection:
            # Ejecuta una consulta simple, como obtener las primeras filas
            result = connection.execute("SELECT 1")
            print("Conexión exitosa:", result.scalar())
    except Exception as e:
        print("Error de conexión:", e)
