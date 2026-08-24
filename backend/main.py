from fastapi import FastAPI

from routers.tryon import router

app = FastAPI()

app.include_router(router, tags=['upload-images'], prefix='/api')


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
    