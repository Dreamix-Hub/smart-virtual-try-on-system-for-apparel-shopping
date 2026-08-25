from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.base_exception import AppException

from common.responses import (
    ErrorResponse,
    ErrorDetail,
)

def register_exception_handlers(app: FastAPI):

 
    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
):
        response = ErrorResponse(
        error=ErrorDetail(
            code=exc.code,
            message=exc.message,
        )
    )
        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(),
    )
        
    @app.exception_handler(Exception)
    async def unexpected_exception_handler(
        request: Request,
        exc: Exception,
    ):
        response = ErrorResponse(
            error=ErrorDetail(
                code="INTERNAL_SERVER_ERROR",
                message="Something went wrong.",
            )
        )
        return JSONResponse(
            status_code=500,
            content=response.model_dump(),
        )