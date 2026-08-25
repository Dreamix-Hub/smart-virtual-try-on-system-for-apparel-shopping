from pydantic import BaseModel

class BackendImagesUrlRequest(BaseModel):
    self_url: str
    garment_url: str
    category: str
    
class TryOnResultResponse(BaseModel):
    result_url: str