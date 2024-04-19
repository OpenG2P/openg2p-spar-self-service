from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class ResponseHeader(BaseModel):
    pass


class ResponseStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"


class ResponsePagination(BaseModel):
    current_page: Optional[int] = None
    page_size: Optional[int] = None
    total_elements: Optional[int] = None


class SparResponse(BaseModel):
    response_header: Optional[ResponseHeader] = None
    response_status: ResponseStatus
    response_message: Optional[str] = None
    response_pagination: Optional[ResponsePagination] = ResponsePagination()
    response_payload: Optional[object] = None
