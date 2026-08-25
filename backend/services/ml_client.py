import requests
from config import settings

async def ml_service(self_url: str, garment_url: str, category: str):
    """ pass data to ml_service inference """
    
    response = requests.post(
        url=f"{settings.ML_SERVICE_URL}/api/generate",    # 123.0.0.1:8001/generate
        json={
            "self_url": self_url,
            "garment_url": garment_url,
            "category": category
        }
    )
    
    return response.status_code