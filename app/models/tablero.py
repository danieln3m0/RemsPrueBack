from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional


class TableroElectricoBase(SQLModel):
    """Modelo base para Tablero Eléctrico con campos comunes"""
    nombre: str = Field(..., description="Nombre del tablero eléctrico")
    ubicacion: str = Field(..., description="Ubicación del tablero")
    marca: Optional[str] = Field(default=None, description="Marca del tablero")
    capacidad_amperios: float = Field(..., gt=0, description="Capacidad en amperios")
    estado: str = Field(..., description="Estado del tablero (Operativo, Mantenimiento, Fuera de Servicio)")
    ano_fabricacion: int = Field(..., ge=1900, le=2100, description="Año de fabricación")
    ano_instalacion: int = Field(..., ge=1900, le=2100, description="Año de instalación")


class TableroElectrico(TableroElectricoBase, table=True):
    """Modelo de tabla para Tablero Eléctrico en la base de datos"""
    __tablename__ = "tableros_electricos"
    
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        description="Identificador único del tablero"
    )


class TableroElectricoCreate(TableroElectricoBase):
    """Modelo para crear un nuevo Tablero Eléctrico (sin ID)"""
    pass


class TableroElectricoUpdate(SQLModel):
    """Modelo para actualizar un Tablero Eléctrico (todos los campos opcionales)"""
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    marca: Optional[str] = None
    capacidad_amperios: Optional[float] = Field(default=None, gt=0)
    estado: Optional[str] = None
    ano_fabricacion: Optional[int] = Field(default=None, ge=1900, le=2100)
    ano_instalacion: Optional[int] = Field(default=None, ge=1900, le=2100)


class TableroElectricoRead(TableroElectricoBase):
    """Modelo para leer un Tablero Eléctrico (con ID)"""
    id: UUID
