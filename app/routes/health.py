from fastapi import APIRouter
from app.config import DOCKERHUB_URL, GITHUB_PROJECT

router = APIRouter()


@router.get(
    "/health",
    summary="Get Health Status",
    description="Get the health status of the application."
)
def health():
    return {
        "container": DOCKERHUB_URL,
        "project":   GITHUB_PROJECT,
        "status":    "healthy",
    }
