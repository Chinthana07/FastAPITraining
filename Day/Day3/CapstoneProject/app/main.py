from fastapi import FastAPI

from app.config import settings
from app.database import ping_database
from app.routers import users 
from app.routers import categories
from app.routers import tickets
from app.routers import comments
from app.routers import attachments
from app.routers import audit_logs

app = FastAPI(title=settings.APP_NAME)

app.include_router(users.router)
app.include_router(categories.router)
app.include_router(tickets.router)
app.include_router(comments.router)
app.include_router(attachments.router)
app.include_router(audit_logs.router)

@app.on_event("startup")
def on_startup() -> None:
    if not ping_database():
        raise RuntimeError("could not connect to MongoDB")
    print(f"[standard]connected to MongoDB. App:{settings.APP_NAME}")

@app.get("/", tags=["Health"])
def health_check():
    return{"status":"ok", "app":settings.APP_NAME}

