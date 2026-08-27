from fastapi import APIRouter, UploadFile, status, Form

from common import SuccessResponse
from models.schemas import JobResponse, JobStatus

from services.cloudinary_service import image_upload
from services.image_processor import read_file_size, standardize_dimension
from services.ml_client import ml_service

from starlette.concurrency import run_in_threadpool
from PIL import UnidentifiedImageError
from common.image_exception import InvalidImageFileFormatException, ImageUploadFailedException

from jobs.job_store import job_store
from common.job_exceptions import JobNotFoundException
from fastapi.background import BackgroundTasks

from uuid import UUID

router = APIRouter()


@router.post('/upload-images', response_model=SuccessResponse[JobResponse], status_code=status.HTTP_202_ACCEPTED)
async def upload_image(
    self_image: UploadFile,
    garment_image: UploadFile,
    background_tasks: BackgroundTasks,
    category: str = Form(...),
): 
    # read and validate file size, should be <5MB
    self_content = await read_file_size(self_image)  
    garment_content = await read_file_size(garment_image) 
    
    # convert image to standard dimension 768x1024
    try:
        new_self = await run_in_threadpool(standardize_dimension, self_content)  
        new_garment = await run_in_threadpool(standardize_dimension, garment_content)
    except UnidentifiedImageError:
        raise InvalidImageFileFormatException()
    
    # Create Job First (So we have the ID ready)
    job_id = job_store.create_job()
    
    # Upload to Cloudinary
    try:
        self_url = await image_upload(file_bytes=new_self, folder="tryon/self")
        garment_url = await image_upload(file_bytes=new_garment, folder="tryon/garment")
    except Exception as e:
        job_store.update_status(job_id=job_id, status=JobStatus.FAILED, error="Image upload failed")  # update the job_store to failed 
        raise ImageUploadFailedException()
    
    # Queue Background Task
    # after the job_id is returned to the frontend ml_service run in background and send data to /api/generate inference
    # and if response is 200 than update the status to PROCESSING which show now ml inference received and will start working on it
    background_tasks.add_task(  
        ml_service,
        job_id=job_id,
        self_url=self_url,
        garment_url=garment_url,
        category=category
    )
    
    return SuccessResponse(
        data=JobResponse.model_validate(job_store.get_job(job_id))
    )

@router.get('/{job_id}/status', response_model=SuccessResponse[JobResponse])
async def check_job_status(job_id: UUID):
    job = job_store.get_job(job_id=job_id)
    
    if job is None:
        raise JobNotFoundException()
    
    return SuccessResponse(
        data=JobResponse.model_validate(job)
    )