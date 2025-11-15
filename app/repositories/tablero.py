from typing import List, Optional
from uuid import UUID

from sqlmodel import Session, select

from app.models.tablero import TableroElectrico
from app.schemas.tablero import (
    TableroElectricoCreate,
    TableroElectricoUpdate,
)


def create_tablero(session: Session, tablero_in: TableroElectricoCreate) -> TableroElectrico:
    """Persist a new TableroElectrico entity."""

    tablero = TableroElectrico.from_orm(tablero_in)
    session.add(tablero)
    session.commit()
    session.refresh(tablero)
    return tablero


def list_tableros(session: Session) -> List[TableroElectrico]:
    """Return all stored tableros."""

    result = session.exec(select(TableroElectrico))
    return result.all()


def get_tablero(session: Session, tablero_id: UUID) -> Optional[TableroElectrico]:
    """Fetch a tablero by its identifier."""

    return session.get(TableroElectrico, tablero_id)


def update_tablero(
    session: Session,
    tablero: TableroElectrico,
    tablero_update: TableroElectricoUpdate,
) -> TableroElectrico:
    """Update an existing tablero with the provided payload."""

    update_data = tablero_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(tablero, key, value)
    session.add(tablero)
    session.commit()
    session.refresh(tablero)
    return tablero


def delete_tablero(session: Session, tablero: TableroElectrico) -> None:
    """Remove a tablero from the database."""

    session.delete(tablero)
    session.commit()
