from fastapi import APIRouter, UploadFile

from common import SuccessResponse
from models.schemas import ImageUploadResponse

from services.cloudinary_service import image_upload
from services.image_processor import read_file_size, standardize_dimension
from services.ml_client import ml_service

from starlette.concurrency import run_in_threadpool
from PIL import UnidentifiedImageError
from common.image_exception import InvalidImageFileFormatException


router = APIRouter()


@router.post('/upload-images', response_model=SuccessResponse[ImageUploadResponse])
async def upload_image(
    self_image: UploadFile,
    garment_image: UploadFile,
    category: str
): 
    self_content = await read_file_size(self_image)  # read and validate file size, should be <5MB
    garment_content = await read_file_size(garment_image) 
    
    try:
        new_self = await run_in_threadpool(standardize_dimension, self_content)  # convert image to standard dimension 768x1024
    except UnidentifiedImageError:
        raise InvalidImageFileFormatException()
    
    try:
        new_garment = await run_in_threadpool(standardize_dimension, garment_content)
    except UnidentifiedImageError:
        raise InvalidImageFileFormatException()
    
    
    self_url = await image_upload(  # upload image to cloudinary
        file_bytes=new_self,
        folder="tryon/self",
    )
    
    garment_url = await image_upload(
        file_bytes=new_garment,
        folder='tryon/garment',
    )
    
    # will send validated and resized images to ml_service inference
    response = await ml_service(self_url=self_url, garment_url=garment_url, category=category)
    
    return SuccessResponse(
        data=ImageUploadResponse(self_url=self_url, garment_url=garment_url)
    )