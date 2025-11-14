from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.database import create_db_and_tables
from app.routers import tableros


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestionar el ciclo de vida de la aplicación.
    Se ejecuta al iniciar y cerrar la aplicación.
    """
    # Código que se ejecuta al iniciar
    print("Iniciando aplicación...")
    create_db_and_tables()
    print("Base de datos inicializada")
    yield
    # Código que se ejecuta al cerrar (si es necesario)
    print("Cerrando aplicación...")


# Crear la aplicación FastAPI
app = FastAPI(
    title="API de Tableros Eléctricos",
    description="API RESTful para gestionar tableros eléctricos con FastAPI y SQLModel",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(tableros.router)


@app.get("/")
def read_root():
    """
    Endpoint raíz de bienvenida.
    """
    return {
        "mensaje": "Bienvenido a la API de Tableros Eléctricos",
        "documentacion": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
def health_check():
    """
    Endpoint para verificar el estado de la API.
    """
    return {"status": "ok", "mensaje": "API funcionando correctamente"}
