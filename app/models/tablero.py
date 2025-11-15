import uuid
from typing import Optional

from sqlmodel import Field, SQLModel


class TableroElectrico(SQLModel, table=True):
    """Database model representing an electrical switchboard."""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    nombre: str = Field(max_length=255)
    ubicacion: str = Field(max_length=255)
    marca: Optional[str] = Field(default=None, max_length=255)
    capacidad_amperios: float = Field(gt=0)
    estado: str = Field(max_length=50)
    ano_fabricacion: int = Field(ge=1900, le=2100, description="Año de fabricación del tablero")
    ano_instalacion: int = Field(ge=1900, le=2100, description="Año de instalación del tablero")
