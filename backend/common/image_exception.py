from core.base_exception import AppException
from config import settings

from fastapi import status

class LargeImageFileSizeException(AppException):
    def __init__(self) -> None:
        super().__init__(
            msg=f"Image size should be less than {settings.max_image_upload_size_bytes // (1024 * 1024)}MB",
            code="FILE_SIZE_IS_TOO_LARGE",
            status_code=status.HTTP_400_BAD_REQUEST
        )

class InvalidImageFileFormatException(AppException):
    def __init__(self) -> None:
        super().__init__(
            msg="Invalid image file. Please upload a valid image (JPEG, PNG, GIF, WebP).",
            code="INVALID_FILE_FORMAT",
            status_code=status.HTTP_400_BAD_REQUEST
        )