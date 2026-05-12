from fastapi import HTTPException
from .types.http_bad_request_error import HttpBadRequestError
from .types.http_not_found_error import HttpNotFoundError

def error_handler(exception: Exception) -> HTTPException:
    if isinstance(exception, HttpBadRequestError):
        raise HTTPException(status_code=exception.status_code, detail=exception.message)
    
    if isinstance(exception, HttpNotFoundError):
        raise HTTPException(status_code=exception.status_code, detail=exception.message)

    raise HTTPException(
        status_code=500,
        detail=exception
        # detail="Erro Inesperado ao processar!!!"
    )