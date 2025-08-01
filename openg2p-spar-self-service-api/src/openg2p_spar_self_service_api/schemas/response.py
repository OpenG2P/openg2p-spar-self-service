from enum import Enum

from pydantic import BaseModel


class ResponseHeader(BaseModel):
    pass


class ResponseStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class ResponsePagination(BaseModel):
    current_page: int | None = None
    page_size: int | None = None
    total_elements: int | None = None


class SparResponse(BaseModel):
    response_header: ResponseHeader | None = None
    response_status: ResponseStatus
    response_error_code: str | None = None
    response_message: str | None = None
    response_pagination: ResponsePagination | None = ResponsePagination()
    response_payload: dict | None = None
