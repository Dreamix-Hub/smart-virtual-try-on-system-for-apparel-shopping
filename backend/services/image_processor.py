from config import settings
from common.image_exception import LargeImageFileSizeException

from PIL import Image
from io import BytesIO

async def read_file_size(file) -> bytes:
    content = await file.read()  # read file content
    
    if len(content) > settings.max_image_upload_size_bytes:
        raise LargeImageFileSizeException()

    # Reset pointer so the same UploadFile can be consumed by Cloudinary upload.
    await file.seek(0)
    
    return content  # return image bytes

def standardize_dimension(content: bytes, target_w=768, target_h=1024) -> bytes:
    """ convert the image to standard 768x1024 required by our models """
    with Image.open(BytesIO(content)) as img:
        # Resize to exact dimensions (768x1024)
        # This stretches or shrinks to fit exactly
        resized_img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)

        output = BytesIO()
        output_format = img.format or "PNG"
        resized_img.save(output, format=output_format)
        return output.getvalue()