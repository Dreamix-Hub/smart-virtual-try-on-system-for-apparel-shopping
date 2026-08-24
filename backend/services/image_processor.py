from config import settings
from common.image_exception import LargeImageFileSizeException

async def read_file_size(file) -> bytes:
    content = await file.read()  # read file content
    
    if len(content) > settings.max_image_upload_size_bytes:
        raise LargeImageFileSizeException()
    
    return content  # return image bytes