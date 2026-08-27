from core.base_exception import AppException
from fastapi import status

class JobNotFoundException(AppException):
    def __init__(self) -> None:
        super().__init__(
            msg="Invalid job id or job not found",
            code='JOB_NOT_FOUND',
            status_code=status.HTTP_400_BAD_REQUEST
        )