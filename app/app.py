from fastapi import FastAPI
from app.routes import secret, health

app = FastAPI()

# app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(secret.router)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Welcome liya's devops challenge"}
