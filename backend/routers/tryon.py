from fastapi import APIRouter, UploadFile

from common import SuccessResponse
from models.schemas import ImageUploadResponse, JobResponse, JobStatus

from services.cloudinary_service import image_upload
from services.image_processor import read_file_size, standardize_dimension
from services.ml_client import ml_service

from starlette.concurrency import run_in_threadpool
from PIL import UnidentifiedImageError
from common.image_exception import InvalidImageFileFormatException

from jobs.job_store import job_store
from fastapi.background import BackgroundTasks

router = APIRouter()


@router.post('/upload-images', response_model=SuccessResponse[JobResponse])
async def upload_image(
    self_image: UploadFile,
    garment_image: UploadFile,
    category: str,
    background_tasks: BackgroundTasks,
): 
    self_content = await read_file_size(self_image)  # read and validate file size, should be <5MB
    garment_content = await read_file_size(garment_image) 
    
    try:
        new_self = await run_in_threadpool(standardize_dimension, self_content)  # convert image to standard dimension 768x1024
    except UnidentifiedImageError:
        raise InvalidImageFileFormatException()
    
    try:
        new_garment = await run_in_threadpool(standardize_dimension, garment_content)
    except UnidentifiedImageError:
        raise InvalidImageFileFormatException()
    
    self_url = await image_upload(  # upload image to cloudinary
        file_bytes=new_self,
        folder="tryon/self",
    )
    
    garment_url = await image_upload(
        file_bytes=new_garment,
        folder='tryon/garment',
    )
    
    job_id = job_store.create_job()  # create a job
    
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