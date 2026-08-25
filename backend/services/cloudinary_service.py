import cloudinary
import cloudinary.uploader

from io import BytesIO
from typing import Union

from fastapi import UploadFile

from config import settings

cloudinary_config = cloudinary.config(
    cloud_name=settings.CLOUD_NAME,
    api_key=settings.API_KEY.get_secret_value(),
    api_secret=settings.API_SECRET.get_secret_value(),
    secure=True
)

async def image_upload(file_bytes: Union[UploadFile, bytes], folder: str) -> str:
    """Upload image bytes or UploadFile to Cloudinary and return its URL."""

    upload_source = file_bytes.file if isinstance(file_bytes, UploadFile) else BytesIO(file_bytes)

    image_url = cloudinary.uploader.upload(
        file=upload_source,
        folder=folder,
        resource_type='image'
    )
    
    return image_url['secure_url']