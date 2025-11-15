from fastapi import FastAPI

from app.controllers.tablero_controller import router as tablero_router
from app.core.config import settings
from app.core.database import init_db

app = FastAPI(
    title="API de Gestión de Tableros Eléctricos",
    description="""
    API RESTful para gestionar tableros eléctricos con operaciones CRUD completas.
    
    ## Funcionalidades
    
    * **Crear tableros**: Registre nuevos tableros eléctricos con todos sus detalles
    * **Listar tableros**: Obtenga todos los tableros registrados en el sistema
    * **Consultar tablero**: Busque un tablero específico por su ID
    * **Actualizar tablero**: Modifique los datos de un tablero existente
    * **Eliminar tablero**: Elimine un tablero del sistema
    
    ## Validaciones
    
    Todos los endpoints incluyen validaciones automáticas de:
    - Campos obligatorios
    - Tipos de datos correctos
    - Rangos válidos (años, capacidad, longitudes de texto)
    """,
    version="1.0.0",
    contact={
        "name": "Soporte API Tableros",
        "email": "soporte@tableros.com",
    },
    license_info={
        "name": "MIT",
    },
)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database metadata when the service boots."""

    init_db()


@app.get("/health", tags=["Health"])
def health_check() -> dict:
    return {"status": "ok"}


app.include_router(tablero_router)
