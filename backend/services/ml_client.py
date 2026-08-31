import httpx
from config import settings
from jobs.job_store import job_store, JobStatus


async def ml_service(job_id: str, self_url: str, garment_url: str, category: str):
    """Pass data to ML inference. Immediately sets status to PROCESSING, 
    then updates to DONE with result_url or FAILED upon completion.
    """
    
    # Immediately mark the job as PROCESSING so polling endpoints see it right away
    job_store.update_status(job_id=job_id, status=JobStatus.PROCESSING)
    
    # Use non-blocking httpx AsyncClient instead of requests
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            response = await client.post(
                url=f"{settings.ML_SERVICE_URL}/api/generate",
                json={
                    "self_url": self_url,
                    "garment_url": garment_url,
                    "category": category
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                result_url = data.get("result_url")
                
                # Mark job as DONE once ML inference completes
                job_store.update_status(
                    job_id=job_id, 
                    status=JobStatus.DONE, 
                    result_url=result_url
                )
                return result_url
            else:
                job_store.update_status(
                    job_id=job_id, 
                    status=JobStatus.FAILED, 
                    error=f"HTTP {response.status_code}: {response.text}"
                )
                return None
                
        except Exception as e:
            job_store.update_status(
                job_id=job_id, 
                status=JobStatus.FAILED, 
                error=str(e)
            )
            return None