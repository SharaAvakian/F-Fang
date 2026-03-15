# ═══════════════════════════════════════════════════════════
# FFAng — Single-container image
# Contains: Python 3.11 + Django + Gunicorn + Nginx + supervisord
# Deploy with:
#   docker build -t sharaavakian/FFang:latest .
#   docker push sharaavakian/FFang:latest
# Run on EC2 with:
#   docker pull sharaavakian/FFang:latest && \
#   docker rm -f FFang-app && \
#   docker run -d --name FFang-app --restart unless-stopped \
#     -p 80:80 -p 443:443 \
#     -v /etc/letsencrypt:/etc/letsencrypt:ro \
#     -v ffang_media:/app/media \
#     -v ffang_db:/app/db \
#     -e DJANGO_SECRET_KEY=your-key \
#     -e ALLOWED_HOSTS=FFang.com,www.FFang.com \
#     -e DJANGO_DEBUG=False \
#     sharaavakian/FFang:latest
# ═══════════════════════════════════════════════════════════

FROM python:3.11-slim

# ─── System packages ─────────────────────────────────────
RUN apt-get update && apt-get install -y \
    nginx \
    supervisor \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ─── Python deps ─────────────────────────────────────────
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ─── App code ────────────────────────────────────────────
COPY . .

# ─── Static files (collected at build time) ──────────────
RUN python manage.py collectstatic --noinput

# ─── Nginx config ────────────────────────────────────────
COPY nginx_single.conf /etc/nginx/nginx.conf
# Remove default nginx site
RUN rm -f /etc/nginx/sites-enabled/default /etc/nginx/conf.d/default.conf

# ─── Supervisor config ───────────────────────────────────
COPY supervisord.conf /app/supervisord.conf
RUN mkdir -p /var/log/supervisor

# ─── Entrypoint ──────────────────────────────────────────
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ─── Non-root user for gunicorn only ─────────────────────
RUN adduser --disabled-password --gecos '' appuser \
    && chown -R appuser:appuser /app \
    && chown -R appuser:appuser /app/media 2>/dev/null || true

# ─── Volumes for persistent data ─────────────────────────
VOLUME ["/app/media", "/app/db"]

EXPOSE 80 443

ENTRYPOINT ["/entrypoint.sh"]
