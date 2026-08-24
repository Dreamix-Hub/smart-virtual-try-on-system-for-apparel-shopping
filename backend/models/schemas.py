from pydantic import BaseModel, HttpUrl

class ImageUploadResponse(BaseModel):
    self_url: str
    garment_url: str