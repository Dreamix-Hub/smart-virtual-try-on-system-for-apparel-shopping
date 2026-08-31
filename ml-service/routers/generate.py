from fastapi import APIRouter
from models.schemas import TryOnResultResponse, BackendImagesUrlRequest
from services.image_downloader import download_image
from services.cloudinary_service import upload_result_image
from services.preprocessor import preprocess_tryon_images, image_to_bytes   # NEW

router = APIRouter(prefix="/generate", tags=['Generate Try-on'])

import asyncio

@router.post("", response_model=TryOnResultResponse)
async def generate_tryon(request: BackendImagesUrlRequest):
    
    self_image = await download_image(request.self_url)  
    garment_image = await download_image(request.garment_url)

    images = preprocess_tryon_images(self_image, garment_image)   
    
    result_url = await upload_result_image(  
        file_bytes=image_to_bytes(images.garment_image),   # CHANGED — was: file_bytes=garment_image
        folder='tryon/results'
    )
    
    await asyncio.sleep(10) # testing
    
    return TryOnResultResponse(result_url=result_url)