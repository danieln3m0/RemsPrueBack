# Backend FastAPI - Tableros Eléctricos

API RESTful para gestionar tableros eléctricos utilizando FastAPI y SQLModel.

## Características

- ✅ CRUD completo para tableros eléctricos
- ✅ Validación de datos con Pydantic/SQLModel
- ✅ Generación automática de UUID
- ✅ Base de datos SQLite con SQLModel
- ✅ Documentación automática con Swagger UI
- ✅ Soporte para CORS

## Requisitos

- Python 3.8 o superior
- pip

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en: `http://localhost:8000`

## Documentación de la API

Una vez que el servidor esté corriendo, puedes acceder a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Endpoints

### Tableros Eléctricos

- `POST /tableros/` - Crear un nuevo tablero
- `GET /tableros/` - Obtener todos los tableros
- `GET /tableros/{tablero_id}` - Obtener un tablero específico
- `PUT /tableros/{tablero_id}` - Actualizar un tablero
- `DELETE /tableros/{tablero_id}` - Eliminar un tablero

### Utilidad

- `GET /` - Endpoint de bienvenida
- `GET /health` - Verificar el estado de la API

## Modelo de Datos

### TableroElectrico

| Campo | Tipo | Requerido | Descripción |
|-------|------|-----------|-------------|
| id | UUID | Automático | Identificador único |
| nombre | String | Sí | Nombre del tablero |
| ubicacion | String | Sí | Ubicación física |
| marca | String | No | Marca del tablero |
| capacidad_amperios | Float | Sí | Capacidad en amperios (> 0) |
| estado | String | Sí | Estado actual |
| ano_fabricacion | Integer | Sí | Año de fabricación (1900-2100) |
| ano_instalacion | Integer | Sí | Año de instalación (1900-2100) |

## Ejemplo de Uso

### Crear un tablero

```bash
curl -X POST "http://localhost:8000/tableros/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Tablero Piso 1 - Ala Norte",
    "ubicacion": "Sala de máquinas, Sótano 1",
    "marca": "Schneider Electric",
    "capacidad_amperios": 100,
    "estado": "Operativo",
    "ano_fabricacion": 2020,
    "ano_instalacion": 2021
  }'
```

### Obtener todos los tableros

```bash
curl -X GET "http://localhost:8000/tableros/"
```

### Obtener un tablero específico

```bash
curl -X GET "http://localhost:8000/tableros/{tablero_id}"
```

### Actualizar un tablero

```bash
curl -X PUT "http://localhost:8000/tableros/{tablero_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "estado": "Mantenimiento"
  }'
```

### Eliminar un tablero

```bash
curl -X DELETE "http://localhost:8000/tableros/{tablero_id}"
```

## Estructura del Proyecto

```
RemsPrueBack/
├── app/
│   ├── __init__.py
│   ├── database.py          # Configuración de base de datos
│   ├── models/
│   │   ├── __init__.py
│   │   └── tablero.py       # Modelo TableroElectrico
│   └── routers/
│       ├── __init__.py
│       └── tableros.py      # Endpoints CRUD
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias
└── README.md               # Este archivo
```

## Base de Datos

El proyecto utiliza SQLite por defecto. La base de datos se crea automáticamente en `tableros.db` cuando se inicia la aplicación por primera vez.

## Validaciones

- **campos obligatorios**: nombre, ubicacion, capacidad_amperios, estado, ano_fabricacion, ano_instalacion
- **capacidad_amperios**: debe ser mayor que 0
- **ano_fabricacion y ano_instalacion**: deben estar entre 1900 y 2100
- **marca**: campo opcional
- **id**: se genera automáticamente como UUID

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **SQLModel**: ORM basado en SQLAlchemy y Pydantic
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **SQLite**: Base de datos embebida 
