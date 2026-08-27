from fastapi import APIRouter
from models.schemas import TryOnResultResponse, BackendImagesUrlRequest
from services.image_downloader import download_image
from services.cloudinary_service import upload_result_image

router = APIRouter(prefix="/generate", tags=['Generate Try-on'])

import time

@router.post("", response_model=TryOnResultResponse)
async def generate_tryon(request: BackendImagesUrlRequest):
    
    self_image = await download_image(request.self_url)   # download images from cloudinary using passed secure_url
    garment_image = await download_image(request.garment_url)
    
    result_url = await upload_result_image(  # upload image to cloudinary and return it's secure url
        file_bytes=garment_image,
        folder='tryon/results'
    )
    
    time.sleep(10)
    
    return TryOnResultResponse(result_url=result_url)
