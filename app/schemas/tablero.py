import uuid
from typing import Optional

from sqlmodel import Field, SQLModel


class TableroElectricoBase(SQLModel):
    nombre: str = Field(min_length=3, max_length=255)
    ubicacion: str = Field(min_length=3, max_length=255)
    marca: Optional[str] = Field(default=None, max_length=255)
    capacidad_amperios: float = Field(gt=0)
    estado: str = Field(min_length=3, max_length=50)
    ano_fabricacion: int = Field(ge=1900, le=2100)
    ano_instalacion: int = Field(ge=1900, le=2100)


class TableroElectricoCreate(TableroElectricoBase):
    pass


class TableroElectricoRead(TableroElectricoBase):
    id: uuid.UUID


class TableroElectricoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=3, max_length=255)
    ubicacion: Optional[str] = Field(default=None, min_length=3, max_length=255)
    marca: Optional[str] = Field(default=None, max_length=255)
    capacidad_amperios: Optional[float] = Field(default=None, gt=0)
    estado: Optional[str] = Field(default=None, min_length=3, max_length=50)
    ano_fabricacion: Optional[int] = Field(default=None, ge=1900, le=2100)
    ano_instalacion: Optional[int] = Field(default=None, ge=1900, le=2100)
