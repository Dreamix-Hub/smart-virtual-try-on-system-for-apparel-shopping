from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl


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


class Job(BaseModel):
    job_id: str
    status: JobStatus
    self_url: str
    garment_url: str
    category: Category
    result_url: str | None = None
    error: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))