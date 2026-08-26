from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


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