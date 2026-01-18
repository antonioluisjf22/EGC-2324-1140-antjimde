#!/bin/bash
set -e

cd decide

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar migraciones
python manage.py migrate --noinput

echo "Build completado exitosamente"
