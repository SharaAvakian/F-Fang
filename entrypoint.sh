#!/bin/sh
set -e

echo "==> Running migrations..."
python manage.py migrate --noinput

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "==> Starting services (Nginx + Gunicorn via supervisord)..."
exec supervisord -c /app/supervisord.conf
