from fastapi import FastAPI
from app.routes import secret

app = FastAPI()

# app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(secret.router)


@app.get("/")
def root():
    return {"message": "Welcome liya's devops challenge"}
