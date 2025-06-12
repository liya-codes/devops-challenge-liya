from fastapi import APIRouter
from app.config import DOCKERHUB_URL, GITHUB_PROJECT

router = APIRouter()

# create router
@router.get(
    "/health",
    summary="Get Health Status",
    description="Get the health status of the application."
)

def health():
    # return the json as requested in the assigment
    return { 
        "container": DOCKERHUB_URL,
        "project":   GITHUB_PROJECT,
        "status":    "healthy",
    }
