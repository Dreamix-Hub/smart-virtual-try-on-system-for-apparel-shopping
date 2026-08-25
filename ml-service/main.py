from fastapi import FastAPI
from routers.generate import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.post('/')
async def root():
    return {
        "message": "ml-service working..."
    }