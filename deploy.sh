#!/bin/bash
# ═══════════════════════════════════════════════════════════
# FFAng Deploy Script
#
# FROM YOUR IDE / LOCAL MACHINE:
#   chmod +x deploy.sh
#   ./deploy.sh build    → build + push image to Docker Hub
#
# ON EC2:
#   ./deploy.sh ec2      → pull + restart container
#   ./deploy.sh setup    → first-time EC2 setup (stop nginx, etc.)
#
# OR just copy-paste the commands below manually.
# ═══════════════════════════════════════════════════════════

set -e

IMAGE="sharaavakian/FFang:latest"
CONTAINER="FFang-app"

# Load .env if it exists
[ -f .env ] && export $(grep -v '^#' .env | xargs)

# ─── build: build image and push to Docker Hub ───────────
build() {
  echo "==> Building $IMAGE ..."
  docker build -t "$IMAGE" .

  echo "==> Pushing $IMAGE to Docker Hub..."
  docker push "$IMAGE"

  echo "✓ Done. Image is live on Docker Hub."
  echo ""
  echo "Now run on EC2:"
  echo "  ./deploy.sh ec2"
  echo "  — or paste the docker run command manually."
}

# ─── ec2: pull latest image and restart container ────────
ec2() {
  echo "==> Pulling latest image..."
  docker pull "$IMAGE"

  echo "==> Removing old container (if any)..."
  docker rm -f "$CONTAINER" 2>/dev/null || true

  echo "==> Starting container..."
  docker run -d \
    --name "$CONTAINER" \
    --restart unless-stopped \
    -p 80:80 \
    -p 443:443 \
    -v /etc/letsencrypt:/etc/letsencrypt:ro \
    -v ffang_media:/app/media \
    -v ffang_db:/app/db \
    -e DJANGO_SECRET_KEY="${DJANGO_SECRET_KEY:?DJANGO_SECRET_KEY must be set in .env}" \
    -e ALLOWED_HOSTS="${ALLOWED_HOSTS:-FFang.com,www.FFang.com}" \
    -e DJANGO_DEBUG="${DJANGO_DEBUG:-False}" \
    -e DATABASE_URL="${DATABASE_URL:-}" \
    -e CORS_ORIGINS="${CORS_ORIGINS:-https://FFang.com}" \
    "$IMAGE"

  echo "✓ Container started."
  echo ""
  echo "Logs: docker logs -f $CONTAINER"
  echo "Exec: docker exec -it $CONTAINER /bin/bash"
}

# ─── setup: first-time EC2 preparation ──────────────────
setup() {
  echo "==> First-time EC2 setup..."

  # Stop and disable host nginx so it doesn't compete on port 80/443
  sudo systemctl stop nginx 2>/dev/null || true
  sudo systemctl disable nginx 2>/dev/null || true
  echo "✓ Host nginx stopped and disabled."

  # Remove all existing containers
  docker rm -f $(docker ps -aq) 2>/dev/null || true
  echo "✓ Old containers removed."

  # Free up ports just in case
  sudo fuser -k 80/tcp 2>/dev/null || true
  sudo fuser -k 443/tcp 2>/dev/null || true
  echo "✓ Ports 80 and 443 freed."

  # Verify
  echo ""
  echo "Port status:"
  sudo ss -tulpn | grep -E ':80|:443' || echo "  (ports are free)"

  echo ""
  echo "✓ Setup complete. Now run: ./deploy.sh ec2"
}

# ─── superuser: create django admin user inside container ─
superuser() {
  docker exec -it "$CONTAINER" python manage.py createsuperuser
}

# ─── logs: tail container logs ───────────────────────────
logs() {
  docker logs -f "$CONTAINER"
}

# ─── shell: open shell inside container ──────────────────
shell() {
  docker exec -it "$CONTAINER" /bin/bash
}

# ─── manage: run any manage.py command ───────────────────
manage() {
  docker exec -it "$CONTAINER" python manage.py "$@"
}

# ─── status: show container status ───────────────────────
status() {
  echo "==> Container:"
  docker ps -a --filter "name=$CONTAINER" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
  echo ""
  echo "==> Port check:"
  sudo ss -tulpn | grep -E ':80|:443' || echo "  (no process on 80/443)"
}

# ─── Command dispatcher ───────────────────────────────────
case "${1:-help}" in
  build)     build ;;
  ec2)       ec2 ;;
  setup)     setup ;;
  superuser) superuser ;;
  logs)      logs ;;
  shell)     shell ;;
  manage)    shift; manage "$@" ;;
  status)    status ;;
  *)
    echo "FFAng Deploy Script"
    echo ""
    echo "Usage: ./deploy.sh <command>"
    echo ""
    echo "Commands:"
    echo "  build      — build Docker image and push to Docker Hub"
    echo "  ec2        — pull latest image and restart on EC2"
    echo "  setup      — first-time EC2 setup (stop nginx, free ports)"
    echo "  superuser  — create Django admin user inside container"
    echo "  logs       — tail container logs"
    echo "  shell      — open bash inside container"
    echo "  manage ... — run manage.py command inside container"
    echo "  status     — show container and port status"
    ;;
esac
