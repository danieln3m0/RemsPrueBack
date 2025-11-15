from typing import List
from uuid import UUID

from sqlmodel import Session

from app.models.tablero import TableroElectrico
from app.repositories.tablero import (
    create_tablero,
    delete_tablero,
    get_tablero,
    list_tableros,
    update_tablero,
)
from app.schemas.tablero import (
    TableroElectricoCreate,
    TableroElectricoRead,
    TableroElectricoUpdate,
)


class TableroNotFoundError(Exception):
    """Raised when a requested tablero does not exist."""


def create(session: Session, tablero_in: TableroElectricoCreate) -> TableroElectricoRead:
    tablero = create_tablero(session, tablero_in)
    return TableroElectricoRead.model_validate(tablero, from_attributes=True)


def get_all(session: Session) -> List[TableroElectricoRead]:
    tableros = list_tableros(session)
    return [
        TableroElectricoRead.model_validate(tablero, from_attributes=True)
        for tablero in tableros
    ]


def get_by_id(session: Session, tablero_id: UUID) -> TableroElectricoRead:
    tablero = get_tablero(session, tablero_id)
    if tablero is None:
        raise TableroNotFoundError(f"Tablero {tablero_id} not found")
    return TableroElectricoRead.model_validate(tablero, from_attributes=True)


def update(
    session: Session,
    tablero_id: UUID,
    tablero_update: TableroElectricoUpdate,
) -> TableroElectricoRead:
    tablero = get_tablero(session, tablero_id)
    if tablero is None:
        raise TableroNotFoundError(f"Tablero {tablero_id} not found")
    updated = update_tablero(session, tablero, tablero_update)
    return TableroElectricoRead.model_validate(updated, from_attributes=True)


def delete(session: Session, tablero_id: UUID) -> None:
    tablero = get_tablero(session, tablero_id)
    if tablero is None:
        raise TableroNotFoundError(f"Tablero {tablero_id} not found")
    delete_tablero(session, tablero)
