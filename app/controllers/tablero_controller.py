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


@router.post("/", response_model=TableroElectricoRead, status_code=status.HTTP_201_CREATED)
def create_tablero(
    tablero_in: TableroElectricoCreate,
    session: Session = Depends(get_session),
) -> TableroElectricoRead:
    return create(session, tablero_in)


@router.get("/", response_model=List[TableroElectricoRead])
def list_tableros(session: Session = Depends(get_session)) -> List[TableroElectricoRead]:
    return get_all(session)


@router.get("/{tablero_id}", response_model=TableroElectricoRead)
def get_tablero(
    tablero_id: UUID,
    session: Session = Depends(get_session),
) -> TableroElectricoRead:
    try:
        return get_by_id(session, tablero_id)
    except TableroNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{tablero_id}", response_model=TableroElectricoRead)
def update_tablero(
    tablero_id: UUID,
    tablero_update: TableroElectricoUpdate,
    session: Session = Depends(get_session),
) -> TableroElectricoRead:
    try:
        return update(session, tablero_id, tablero_update)
    except TableroNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{tablero_id}", status_code=status.HTTP_200_OK)
def delete_tablero(tablero_id: UUID, session: Session = Depends(get_session)) -> dict:
    try:
        delete(session, tablero_id)
    except TableroNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return {"mensaje": "Tablero eliminado"}
