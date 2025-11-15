# Guía de Despliegue en Render

## Preparación Completada ✅

Tu backend ya está configurado para Render con:
- ✅ `Procfile` - Comando de inicio
- ✅ `runtime.txt` - Versión de Python
- ✅ Base de datos PostgreSQL configurada
- ✅ Variables de entorno preparadas

## Pasos para Desplegar en Render

### 1. Sube tu código a GitHub

```bash
git init
git add .
git commit -m "Backend FastAPI listo para Render"
git branch -M main
git remote add origin https://github.com/danieln3m0/RemsPrueBack.git
git push -u origin main
```

### 2. Crear cuenta en Render

1. Ve a https://render.com
2. Regístrate con tu cuenta de GitHub
3. Autoriza a Render para acceder a tus repositorios

### 3. Crear Web Service

1. Click en **"New +"** → **"Web Service"**
2. Conecta tu repositorio `RemsPrueBack`
3. Configura:
   - **Name**: `tableros-electricos-api` (o el nombre que prefieras)
   - **Region**: Selecciona la región más cercana
   - **Branch**: `main`
   - **Root Directory**: (dejar vacío)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 4. Crear Base de Datos PostgreSQL

1. En el dashboard de Render, click **"New +"** → **"PostgreSQL"**
2. Configura:
   - **Name**: `tableros-db`
   - **Database**: `tableros`
   - **User**: (se genera automáticamente)
   - **Region**: Misma región que el Web Service
   - **Plan**: Free (o el que prefieras)
3. Click **"Create Database"**
4. Espera a que se cree (toma 1-2 minutos)

### 5. Conectar Web Service con la Base de Datos

1. Ve a tu Web Service
2. Click en **"Environment"** (en el menú lateral)
3. Click **"Add Environment Variable"**
4. Añade:
   - **Key**: `DATABASE_URL`
   - **Value**: Click en "Add from Service" → Selecciona tu base de datos PostgreSQL → Selecciona "Internal Database URL"
5. Click **"Save Changes"**

### 6. Desplegar

1. El servicio se desplegará automáticamente
2. Espera 3-5 minutos
3. Una vez completado, verás la URL de tu API: `https://tu-servicio.onrender.com`

## URLs de tu API Desplegada

```
API Base: https://tu-servicio.onrender.com
Documentación: https://tu-servicio.onrender.com/docs
ReDoc: https://tu-servicio.onrender.com/redoc
Health Check: https://tu-servicio.onrender.com/health
```

## Endpoints Disponibles

```
POST   /tableros/           - Crear tablero
GET    /tableros/           - Listar todos los tableros
GET    /tableros/{id}       - Obtener un tablero
PUT    /tableros/{id}       - Actualizar tablero
DELETE /tableros/{id}       - Eliminar tablero
```

## Probar la API

```bash
# Crear un tablero
curl -X POST "https://tu-servicio.onrender.com/tableros/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Tablero Principal",
    "ubicacion": "Planta Baja",
    "marca": "Schneider",
    "capacidad_amperios": 150,
    "estado": "Operativo",
    "ano_fabricacion": 2023,
    "ano_instalacion": 2024
  }'
```

## Notas Importantes

- 🆓 **Plan Free de Render**: El servicio se duerme después de 15 minutos sin uso. La primera petición puede tardar 30-60 segundos en despertar.
- 🔒 **HTTPS**: Render proporciona HTTPS automáticamente
- 🔄 **Auto-deploy**: Cada push a `main` despliega automáticamente
- 📊 **PostgreSQL Free**: 90 días gratis, luego $7/mes (o mantén SQLite en local)

## Variables de Entorno Configuradas

| Variable | Valor | Descripción |
|----------|-------|-------------|
| DATABASE_URL | (automático) | URL de PostgreSQL de Render |
| PORT | (automático) | Puerto asignado por Render |

## Solución de Problemas

### Si el despliegue falla:

1. Revisa los logs en Render Dashboard
2. Verifica que `requirements.txt` esté correcto
3. Asegúrate que `DATABASE_URL` esté configurada
4. Verifica que el `Procfile` exista

### Si la base de datos no conecta:

1. Usa "Internal Database URL" no "External"
2. Verifica que ambos servicios estén en la misma región
3. Reinicia el Web Service después de añadir `DATABASE_URL`

## Mantenimiento

Para actualizar tu API:

```bash
git add .
git commit -m "Actualización"
git push
```

Render desplegará automáticamente los cambios.
