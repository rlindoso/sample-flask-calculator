from dataclasses import dataclass
from typing import List

from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

@dataclass
class LocalError:
    title: str
    detail: str

@dataclass
class HandleBody:
    errors: List[LocalError]

@dataclass
class HandleError:
    status_code: int
    body: HandleBody

def handle_errors(error: Exception) -> HandleError:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):

        local_error= LocalError(title=error.name, detail=error.message)
        handle_body = HandleBody(errors=[local_error])
        handle_error = HandleError(status_code=error.status_code, body=handle_body)

        return handle_error
    
    local_error= LocalError(title="Server Error", detail=str(error))
    handle_body = HandleBody(errors=[local_error])
    handle_error = HandleError(status_code=500, body=handle_body)

    return handle_error
    