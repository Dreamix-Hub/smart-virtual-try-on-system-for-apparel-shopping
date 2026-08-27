from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.exceptions import register_exception_handlers
from routers.tryon import router

app = FastAPI()
register_exception_handlers(app)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:5501",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:8000",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, tags=['upload-images'], prefix='/api/try-on')


@app.get('/')
async def root():
    return {
        'message': 'welcome to smart virtual try-on system'
    }


@app.get('/health')
async def health():
    return {
        'message': 'server running.....'
    }
    