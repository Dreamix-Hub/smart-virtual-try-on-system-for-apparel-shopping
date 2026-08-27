import threading
import uuid
from datetime import datetime, timezone
from typing import Optional

from models.schemas import JobStatus
class JobStore:
    """
    Simple thread-safe in-memory job store factory.
    """

    def __init__(self):
        self._jobs: dict[str, dict] = {}
        self._lock = threading.Lock()

    def create_job(self) -> str:
        job_id = str(uuid.uuid4())
        with self._lock:
            self._jobs[job_id] = {
                "job_id": job_id,
                "status": JobStatus.PENDING,
                "result_url": None,
                "error": None,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }
        return job_id

    def get_job(self, job_id: str) -> Optional[dict]:
        with self._lock:
            job = self._jobs.get(job_id)
            return dict(job) if job else None

    def update_status(
        self,
        job_id: str,
        status: JobStatus,
        result_url: Optional[str] = None,
        error: Optional[str] = None,
    ) -> None:
        with self._lock:
            if job_id not in self._jobs:
                raise KeyError(f"Job {job_id} not found")
            self._jobs[job_id]["status"] = status
            self._jobs[job_id]["updated_at"] = datetime.now(timezone.utc).isoformat()
            if result_url is not None:
                self._jobs[job_id]["result_url"] = result_url
            if error is not None:
                self._jobs[job_id]["error"] = error

    def delete_job(self, job_id: str) -> None:
        with self._lock:
            self._jobs.pop(job_id, None)


# Single shared instance — imported wherever job state is needed
job_store = JobStore()