import uuid

from models.schemas import Category, Job, JobStatus

_jobs: dict[str, Job] = {}  # in-memory job store, keyed by job_id


def create_job(self_url: str, garment_url: str, category: Category) -> str:
    """Create a new job in 'pending' state and return its job_id."""
    job_id = str(uuid.uuid4())
    _jobs[job_id] = Job(
        job_id=job_id,
        status=JobStatus.PENDING,
        self_url=self_url,
        garment_url=garment_url,
        category=category,
    )
    return job_id


def get_job(job_id: str) -> Job | None:
    """Fetch a job by id. Returns None if it doesn't exist."""
    return _jobs.get(job_id)


def update_job(job_id: str, **fields) -> None:
    """Update one or more fields on an existing job (e.g. status, result_url)."""
    job = _jobs.get(job_id)
    if job is not None:
        for key, value in fields.items():
            setattr(job, key, value)