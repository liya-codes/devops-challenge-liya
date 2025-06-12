from fastapi import FastAPI
from app.routes import secret, health

app = FastAPI()

# add the routes so the fastapi app
app.include_router(secret.router)
app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "Welcome liya's devops challenge"}
