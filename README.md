# Salud Vital Ltda. – EVA2 Backend (DRF + Templates + PostgreSQL)

Proyecto guía listo para implementar los criterios de la evaluación.

## Entorno virtual
```bash
python -m venv eva2
source eva2/bin/activate  # Linux/Mac
# o en Windows (PowerShell):
# .\eva2\Scripts\Activate.ps1
```

## Instalación
```bash
pip install -r requirements.txt
cp .env.example .env
```

Edita `.env` con tus credenciales de PostgreSQL.

## Base de datos PostgreSQL
Crea una BD, por ejemplo:
```sql
CREATE DATABASE salud_vital;
CREATE USER salud_user WITH PASSWORD 'salud_pass';
ALTER ROLE salud_user SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE salud_vital TO salud_user;
```

## Migraciones y carga de datos
```bash
python manage.py migrate
python manage.py loaddata initial_data.json
python manage.py createsuperuser
python manage.py runserver
```

## Rutas principales
- Admin: `/admin/`
- Documentación Swagger: `/docs/`
- Redoc: `/redoc/`
- API raíz: `/api/`
- Endpoints por entidad: `/api/<entidad>/`
- Vistas HTML (CRUD): `/web/<entidad>/...`

## Criterios de la rúbrica cubiertos
- Entorno virtual `eva2` ✔
- Comentarios en bloque en módulos y clases ✔
- Estructura de proyecto coherente ✔
- Modelo de datos + relaciones en PostgreSQL ✔
- CRUD completo por entidad (HTML y API) ✔
- Carga de BD con datos realistas (fixture) ✔
- Mejoras (CHOICES + nuevas tablas adicionales) ✔
- Templates fuera del admin con footer requeridos ✔
- Documentación navegable de la API (Swagger/Redoc) ✔
- Filtros y búsquedas con `django-filter` ✔
- Uso de PostgreSQL y conexión ✔
- Rutas y endpoints API + web ✔
- Footer con nombre/sección/año ✔
- Nombres coherentes del proyecto y app ✔
