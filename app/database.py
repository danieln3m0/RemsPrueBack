from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os

# URL de la base de datos
# Para producción en Render, usa PostgreSQL; para desarrollo local, usa SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tableros.db")

# Render usa postgres:// pero SQLAlchemy requiere postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configurar connect_args solo para SQLite
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Crear el engine de la base de datos
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=True  # Mostrar las queries SQL en la consola (útil para desarrollo)
)


def create_db_and_tables():
    """
    Crear todas las tablas en la base de datos.
    Esta función debe ser llamada al iniciar la aplicación.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Generador de sesiones de base de datos para ser usado como dependencia en FastAPI.
    
    Yields:
        Session: Sesión de SQLModel para realizar operaciones en la base de datos
    """
    with Session(engine) as session:
        yield session
