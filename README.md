# Tableros API

API RESTful para gestionar tableros eléctricos utilizando FastAPI y SQLModel siguiendo una arquitectura MVC orientada a servicios.

## Requisitos

- Python 3.11 o superior
- Poetry o pip (este proyecto usa `requirements.txt`)

## Configuración local

1. Crear y activar un entorno virtual.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Copiar el archivo `.env.example` a `.env` y ajustar valores si es necesario.
4. Ejecutar el servidor en modo desarrollo:
   ```bash
   uvicorn app.main:app --reload
   ```

## Arquitectura

- `app/models`: Definiciones SQLModel (capa **Model**).
- `app/schemas`: Esquemas Pydantic/SQLModel para validaciones.
- `app/repositories`: Acceso a datos (CRUD sobre SQLModel).
- `app/services`: Lógica de negocio (**Controller** dentro del patrón MVC adaptado a servicios REST).
- `app/controllers`: Routers de FastAPI que exponen la API (**View** hacia el consumidor HTTP).

## Endpoints principales

- `POST /tableros/`
- `GET /tableros/`
- `GET /tableros/{tablero_id}`
- `PUT /tableros/{tablero_id}`
- `DELETE /tableros/{tablero_id}`

Consultar `http://localhost:8000/docs` para probar mediante la documentación interactiva de FastAPI.

## Despliegue en Render

1. Subir el repositorio a GitHub.
2. Revisar y adaptar `render.yaml` (ajustar nombre del servicio, región o plan).
3. Conectar el repositorio a Render y desplegar usando "Blueprint".
4. Render creará una base de datos PostgreSQL gratis (`tableros-db`); la variable `DATABASE_URL` se inyectará automáticamente.
5. Asegurarse de ejecutar migraciones/tareas adicionales si se agregan nuevas tablas en el futuro.


