from fastapi import FastAPI

from core.exceptions import register_exception_handlers
from routers.tryon import router

app = FastAPI()
register_exception_handlers(app)

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
    