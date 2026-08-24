from fastapi import APIRouter, UploadFile

from common import SuccessResponse
from models.schemas import ImageUploadResponse

from services.cloudinary_service import image_upload
from services.image_processor import read_file_size

router = APIRouter()


@router.post('/upload-images', response_model=SuccessResponse[ImageUploadResponse])
async def upload_image(
    self_image: UploadFile,
    garment_image: UploadFile,
    category: str
): 
    self_content = await read_file_size(self_image)
    garment_content = await read_file_size(garment_image) 
        
    self_url = await image_upload(
        file_bytes=self_image,
        folder="tryon/self",
    )
    
    garment_url = await image_upload(
        file_bytes=garment_image,
        folder='tryon/garment',
    )
    
    return SuccessResponse(
        data=ImageUploadResponse(self_url=self_url, garment_url=garment_url)
    )