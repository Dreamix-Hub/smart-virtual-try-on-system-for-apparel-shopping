import cloudinary
import cloudinary.uploader

from fastapi import UploadFile

from config import settings

cloudinary_config = cloudinary.config(
    cloud_name=settings.CLOUD_NAME,
    api_key=settings.API_KEY.get_secret_value(),
    api_secret=settings.API_SECRET.get_secret_value(),
    secure=True
)

async def image_upload(file_bytes: UploadFile, folder: str) -> str:
    """ upload image to cloudinary and return its url """
    image_url = cloudinary.uploader.upload(
        file=file_bytes.file,
        folder=folder,
        resource_type='image'
    )
    
    return image_url['secure_url']