from fastapi import FastAPI
from pymongo import AsyncMongoClient
app = FastAPI()
client = AsyncMongoClient("mongodb://localhost:27012/")
db=client["college"]

#select collection
students_collection = db["student"]
@app.get("/")
async def home():
    return {
        "message":"FastAPI with MongoDB is running"
    }

@app.get("/health")
async def health():
    result = await db.command("ping")
    return {"mongodb":"Connected", "ping":result["ok"]}

    