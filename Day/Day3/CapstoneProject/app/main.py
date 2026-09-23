from fastapi import FastAPI

from app.config import settings
from app.database import ping_database

app = FastAPI(title=settings.APP_NAME)

@app.on_event("startup")
def on_startup() -> None:
    if not ping_database():
        raise RuntimeError("could not connect to MongoDB")
    print(f"[standard]connected to MongoDB. App:{settings.APP_NAME}")

@app.get("/", tags=["Health"])
def health_check():
    return{"status":"ok", "app":settings.APP_NAME}
