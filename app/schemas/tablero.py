import uuid
from typing import Optional

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class TableroElectricoBase(SQLModel):
    nombre: str = Field(
        min_length=3,
        max_length=255,
        description="Nombre descriptivo del tablero eléctrico",
        examples=["Tablero Piso 1 - Ala Norte", "Panel Principal Edificio A"],
    )
    ubicacion: str = Field(
        min_length=3,
        max_length=255,
        description="Ubicación física del tablero",
        examples=["Sala de máquinas, Sótano 1", "Oficina 203, Piso 2"],
    )
    marca: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Marca del fabricante",
        examples=["Schneider Electric", "ABB", "Siemens"],
    )
    capacidad_amperios: float = Field(
        gt=0,
        description="Capacidad en amperios del tablero",
        examples=[100, 200, 400],
    )
    estado: str = Field(
        min_length=3,
        max_length=50,
        description="Estado operativo actual del tablero",
        examples=["Operativo", "Mantenimiento", "Fuera de Servicio"],
    )
    ano_fabricacion: int = Field(
        ge=1900,
        le=2100,
        description="Año de fabricación del tablero",
        examples=[2020, 2021, 2022],
    )
    ano_instalacion: int = Field(
        ge=1900,
        le=2100,
        description="Año de instalación del tablero",
        examples=[2021, 2022, 2023],
    )


class TableroElectricoCreate(TableroElectricoBase):
    """
    Schema para crear un nuevo tablero eléctrico.
    
    Todos los campos son obligatorios excepto 'marca'.
    El ID será generado automáticamente por el sistema.
    """
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "nombre": "Tablero Piso 1 - Ala Norte",
                    "ubicacion": "Sala de máquinas, Sótano 1",
                    "marca": "Schneider Electric",
                    "capacidad_amperios": 200,
                    "estado": "Operativo",
                    "ano_fabricacion": 2020,
                    "ano_instalacion": 2021,
                }
            ]
        }
    )


class TableroElectricoRead(TableroElectricoBase):
    """
    Schema para leer un tablero eléctrico existente.
    
    Incluye todos los campos del tablero más su ID único.
    """
    
    id: uuid.UUID = Field(description="Identificador único del tablero (UUID)")
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "nombre": "Tablero Piso 1 - Ala Norte",
                    "ubicacion": "Sala de máquinas, Sótano 1",
                    "marca": "Schneider Electric",
                    "capacidad_amperios": 200,
                    "estado": "Operativo",
                    "ano_fabricacion": 2020,
                    "ano_instalacion": 2021,
                }
            ]
        },
    )


class TableroElectricoUpdate(SQLModel):
    """
    Schema para actualizar un tablero eléctrico existente.
    
    Todos los campos son opcionales. Solo se actualizarán los campos proporcionados.
    """
    
    nombre: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=255,
        description="Nuevo nombre del tablero",
    )
    ubicacion: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=255,
        description="Nueva ubicación del tablero",
    )
    marca: Optional[str] = Field(
        default=None,
        max_length=255,
        description="Nueva marca del tablero",
    )
    capacidad_amperios: Optional[float] = Field(
        default=None,
        gt=0,
        description="Nueva capacidad en amperios",
    )
    estado: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Nuevo estado del tablero",
    )
    ano_fabricacion: Optional[int] = Field(
        default=None,
        ge=1900,
        le=2100,
        description="Nuevo año de fabricación",
    )
    ano_instalacion: Optional[int] = Field(
        default=None,
        ge=1900,
        le=2100,
        description="Nuevo año de instalación",
    )
    
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "estado": "Mantenimiento",
                    "capacidad_amperios": 250,
                }
            ]
        }
    )
