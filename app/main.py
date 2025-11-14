from fastapi import FastAPI
from app.api import users, items

app = FastAPI(
    title="Intermediate FastAPI Project",
    description="A sample of modular FastAPI app with basic CRUD, models, dependencies, config, and tests."
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/")
def health():
    return {"status": "ok"}