import requests
from config import settings
from jobs.job_store import job_store, JobStatus
from uuid import UUID

async def ml_service(job_id: UUID, self_url: str, garment_url: str, category: str):
    """ pass data to ml_service inference """
    
    response = requests.post(
        url=f"{settings.ML_SERVICE_URL}/api/generate",    # 123.0.0.1:8001/generate
        json={
            "self_url": self_url,
            "garment_url": garment_url,
            "category": category
        }
    )
    
    if response.status_code == 200:
        job_store.update_status(job_id=job_id, status=JobStatus.PROCESSING)
    else:
        job_store.update_status(job_id=job_id, status=JobStatus.FAILED, error=str(response.status_code))