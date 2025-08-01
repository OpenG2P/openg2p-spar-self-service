from pydantic import BaseModel


class RequestHeader(BaseModel):
    pass


class RequestPagination(BaseModel):
    request_page: int | None = None
    page_size: int | None = None


class SparRequest(BaseModel):
    request_header: RequestHeader
    request_pagination: RequestPagination
    request_payload: object
