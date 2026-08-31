import json
import uuid
from datetime import datetime, timezone
from typing import Optional

import redis

from config import settings 
from models.schemas import JobStatus
class JobStore:
    """
    Redis-backed job store. Survives process restarts / Render spin-down.
    Jobs auto-expire after JOB_TTL_SECONDS to avoid unbounded growth.
    """

    JOB_TTL_SECONDS = settings.job_ttl_seconds

    def __init__(self, redis_url: str):
        self._r = redis.from_url(redis_url, decode_responses=True)

    def _key(self, job_id: str) -> str:
        return f"job:{job_id}"

    def create_job(self) -> str:
        job_id = str(uuid.uuid4())
        job_data = {
            "job_id": job_id,
            "status": JobStatus.PENDING.value,
            "result_url": "",
            "error": "",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        self._r.set(self._key(job_id), json.dumps(job_data), ex=self.JOB_TTL_SECONDS)
        return job_id

    def get_job(self, job_id: str) -> Optional[dict]:
        raw = self._r.get(self._key(job_id))
        return json.loads(raw) if raw else None

    def update_status(
        self,
        job_id: str,
        status: JobStatus,
        result_url: Optional[str] = None,
        error: Optional[str] = None,
    ) -> None:
        job = self.get_job(job_id)
        if job is None:
            raise KeyError(f"Job {job_id} not found")

        job["status"] = status.value
        job["updated_at"] = datetime.now(timezone.utc).isoformat()
        if result_url is not None:
            job["result_url"] = result_url
        if error is not None:
            job["error"] = error

        # re-set with TTL refreshed so it doesn't expire mid-processing
        self._r.set(self._key(job_id), json.dumps(job), ex=self.JOB_TTL_SECONDS)

    def delete_job(self, job_id: str) -> None:
        self._r.delete(self._key(job_id))


# Single shared instance — imported wherever job state is needed
job_store = JobStore(redis_url=settings.REDIS_URL.get_secret_value())