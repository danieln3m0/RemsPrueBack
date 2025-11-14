from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List
from uuid import UUID

from app.models.tablero import (
    TableroElectrico,
    TableroElectricoCreate,
    TableroElectricoRead,
    TableroElectricoUpdate
)
from app.database import get_session

router = APIRouter(prefix="/tableros", tags=["Tableros Eléctricos"])


@router.post("/", response_model=TableroElectricoRead, status_code=201)
def crear_tablero(
    tablero: TableroElectricoCreate,
    session: Session = Depends(get_session)
) -> TableroElectrico:
    """
    Crear un nuevo tablero eléctrico.
    
    - **nombre**: Nombre del tablero
    - **ubicacion**: Ubicación física del tablero
    - **marca**: Marca del tablero (opcional)
    - **capacidad_amperios**: Capacidad en amperios
    - **estado**: Estado actual (Operativo, Mantenimiento, Fuera de Servicio)
    - **ano_fabricacion**: Año de fabricación
    - **ano_instalacion**: Año de instalación
    """
    db_tablero = TableroElectrico.model_validate(tablero)
    session.add(db_tablero)
    session.commit()
    session.refresh(db_tablero)
    return db_tablero


@router.get("/", response_model=List[TableroElectricoRead])
def obtener_tableros(
    session: Session = Depends(get_session)
) -> List[TableroElectrico]:
    """
    Obtener todos los tableros eléctricos registrados.
    """
    statement = select(TableroElectrico)
    tableros = session.exec(statement).all()
    return tableros


@router.get("/{tablero_id}", response_model=TableroElectricoRead)
def obtener_tablero(
    tablero_id: UUID,
    session: Session = Depends(get_session)
) -> TableroElectrico:
    """
    Obtener un tablero eléctrico específico por su ID.
    """
    tablero = session.get(TableroElectrico, tablero_id)
    if not tablero:
        raise HTTPException(
            status_code=404,
            detail=f"Tablero con ID {tablero_id} no encontrado"
        )
    return tablero


@router.put("/{tablero_id}", response_model=TableroElectricoRead)
def actualizar_tablero(
    tablero_id: UUID,
    tablero_update: TableroElectricoUpdate,
    session: Session = Depends(get_session)
) -> TableroElectrico:
    """
    Actualizar un tablero eléctrico existente.
    
    Solo se actualizarán los campos proporcionados en el body de la petición.
    """
    db_tablero = session.get(TableroElectrico, tablero_id)
    if not db_tablero:
        raise HTTPException(
            status_code=404,
            detail=f"Tablero con ID {tablero_id} no encontrado"
        )
    
    # Actualizar solo los campos proporcionados
    tablero_data = tablero_update.model_dump(exclude_unset=True)
    for key, value in tablero_data.items():
        setattr(db_tablero, key, value)
    
    session.add(db_tablero)
    session.commit()
    session.refresh(db_tablero)
    return db_tablero


@router.delete("/{tablero_id}")
def eliminar_tablero(
    tablero_id: UUID,
    session: Session = Depends(get_session)
) -> dict:
    """
    Eliminar un tablero eléctrico por su ID.
    """
    tablero = session.get(TableroElectrico, tablero_id)
    if not tablero:
        raise HTTPException(
            status_code=404,
            detail=f"Tablero con ID {tablero_id} no encontrado"
        )
    
    session.delete(tablero)
    session.commit()
    return {"mensaje": "Tablero eliminado"}
