
## 1. Prerequisites
| Tool | Version | Install |
|------|---------|---------|
| Docker | 24+ | <https://docs.docker.com/get-docker/> |
| Docker Compose | v2 | ships with Docker Desktop |
| Python | 3.11 | `pyenv install 3.11.3` (dev only) |

---

## 2. Quick start

```bash
git clone https://github.com/<org>/<repo>.git
cd <repo>

# Build & launch everything
docker compose up --build -d


# 1. Health-check route ─ should return "healthy"
curl -s http://localhost:5000/health | jq .

#expected outcode

{
  "container":$DOCKERHUB_URL
  "project": $GITHUB_PROJECT ,
  "status": "healthy"
}

# 2. Get secret key - returns secret key
curl -s http://localhost:5000/secret


{
  "secret_code": "xyz123"   // ← example; your value depends on code_name
}