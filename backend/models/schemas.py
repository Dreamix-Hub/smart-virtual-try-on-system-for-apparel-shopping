from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from uuid import UUID
class ImageUploadResponse(BaseModel):
    self_url: str
    garment_url: str


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"

class Category(str, Enum):
    KURTA = "kurta"
    SHALWAR_KAMEEZ = "shalwar_kameez"
    WAISTCOAT = "waistcoat"
    SHARWANI = "sharwani"

class JobResponse(BaseModel):
    job_id: UUID
    status: JobStatus
    result_url: str | None = None
    error: str | None = None
    created_at: datetime
    updated_at: datetime