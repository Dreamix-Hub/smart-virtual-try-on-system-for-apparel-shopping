from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.generate import router

app = FastAPI()

origins = [
    "http://127.0.0.1:8000", # backend local uvicorn 
    "https://module-effort-finlike.ngrok-free.dev" # backend ngrok
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api", tags=['Generate Try-on']) # /api/generate router

@app.post('/')
async def root():
    return {
        "message": "ml-service working..."
    }