from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.schemas.tablero import (
    TableroElectricoCreate,
    TableroElectricoRead,
    TableroElectricoUpdate,
)
from app.services.tablero_service import TableroNotFoundError, create, delete, get_all, get_by_id, update

router = APIRouter(prefix="/tableros", tags=["Tableros"])


@router.post(
    "/",
    response_model=TableroElectricoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo tablero eléctrico",
    description="Crea un nuevo tablero eléctrico con los datos proporcionados. El ID se genera automáticamente.",
    response_description="El tablero eléctrico creado con su ID único",
)
def create_tablero(
    tablero_in: TableroElectricoCreate,
    session: Session = Depends(get_session),
) -> TableroElectricoRead:
    """
    Crear un nuevo tablero eléctrico.
    
    - **nombre**: Nombre descriptivo del tablero (mínimo 3 caracteres)
    - **ubicacion**: Ubicación física del tablero (mínimo 3 caracteres)
    - **marca**: Marca del fabricante (opcional)
    - **capacidad_amperios**: Capacidad en amperios (mayor a 0)
    - **estado**: Estado actual del tablero (ej: "Operativo", "Mantenimiento", "Fuera de Servicio")
    - **ano_fabricacion**: Año de fabricación (entre 1900 y 2100)
    - **ano_instalacion**: Año de instalación (entre 1900 y 2100)
    """
    return create(session, tablero_in)


@router.get(
    "/",
    response_model=List[TableroElectricoRead],
    summary="Listar todos los tableros eléctricos",
    description="Obtiene una lista completa de todos los tableros eléctricos registrados en el sistema.",
    response_description="Lista de todos los tableros eléctricos",
)
def list_tableros(session: Session = Depends(get_session)) -> List[TableroElectricoRead]:
    """
    Obtener todos los tableros eléctricos.
    
    Retorna un array con todos los tableros registrados, incluyendo todos sus datos y IDs.
    Si no hay tableros registrados, retorna un array vacío.
    """
    return get_all(session)


@router.get(
    "/{tablero_id}",
    response_model=TableroElectricoRead,
    summary="Obtener un tablero específico",
    description="Busca y retorna un tablero eléctrico específico por su ID único.",
    response_description="El tablero eléctrico solicitado",
    responses={
        404: {
            "description": "Tablero no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Tablero <id> not found"}
                }
            },
        }
    },
)
def get_tablero(
    tablero_id: UUID,
    session: Session = Depends(get_session),
) -> TableroElectricoRead:
    """
    Obtener un tablero eléctrico por su ID.
    
    - **tablero_id**: ID único del tablero (formato UUID)
    
    Retorna el tablero con todos sus datos si existe, o un error 404 si no se encuentra.
    """
    try:
        return get_by_id(session, tablero_id)
    except TableroNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put(
    "/{tablero_id}",
    response_model=TableroElectricoRead,
    summary="Actualizar un tablero eléctrico",
    description="Actualiza los datos de un tablero existente. Solo los campos proporcionados serán actualizados.",
    response_description="El tablero eléctrico actualizado",
    responses={
        404: {
            "description": "Tablero no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Tablero <id> not found"}
                }
            },
        }
    },
)
def update_tablero(
    tablero_id: UUID,
    tablero_update: TableroElectricoUpdate,
    session: Session = Depends(get_session),
) -> TableroElectricoRead:
    """
    Actualizar un tablero eléctrico existente.
    
    - **tablero_id**: ID único del tablero a actualizar (formato UUID)
    
    Puede actualizar cualquier combinación de los siguientes campos:
    - **nombre**: Nuevo nombre del tablero
    - **ubicacion**: Nueva ubicación
    - **marca**: Nueva marca
    - **capacidad_amperios**: Nueva capacidad
    - **estado**: Nuevo estado
    - **ano_fabricacion**: Nuevo año de fabricación
    - **ano_instalacion**: Nuevo año de instalación
    
    Los campos no incluidos en la petición permanecerán sin cambios.
    """
    try:
        return update(session, tablero_id, tablero_update)
    except TableroNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/{tablero_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un tablero eléctrico",
    description="Elimina permanentemente un tablero eléctrico del sistema.",
    response_description="Confirmación de eliminación",
    responses={
        200: {
            "description": "Tablero eliminado exitosamente",
            "content": {
                "application/json": {
                    "example": {"mensaje": "Tablero eliminado"}
                }
            },
        },
        404: {
            "description": "Tablero no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Tablero <id> not found"}
                }
            },
        },
    },
)
def delete_tablero(tablero_id: UUID, session: Session = Depends(get_session)) -> dict:
    """
    Eliminar un tablero eléctrico.
    
    - **tablero_id**: ID único del tablero a eliminar (formato UUID)
    
    Esta operación es permanente y no se puede deshacer.
    Retorna un mensaje de confirmación si la eliminación fue exitosa.
    """
    try:
        delete(session, tablero_id)
    except TableroNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return {"mensaje": "Tablero eliminado"}
