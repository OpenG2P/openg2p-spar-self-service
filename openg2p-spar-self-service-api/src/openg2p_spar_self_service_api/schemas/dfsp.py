from .request import SparRequest
from .response import SparResponse
from pydantic import BaseModel
from typing import Optional, List


class DfspLevelSchema(BaseModel):
    id: int
    name: str
    code: str
    parent: Optional[int]
    validation_regex: Optional[str]


class DfspLevelRequestPayload(BaseModel):
    parent: Optional[int]


class DfspLevelRequest(SparRequest):
    request_payload: DfspLevelRequestPayload


class DfspLevelResponse(SparResponse):
    response_payload: List[DfspLevelSchema]


class DfspLevelValueSchema(BaseModel):
    id: int
    name: str
    code: str
    parent: Optional[int]
    level_id: int
    strategy_id: Optional[int]


class DfspLevelValueRequestPayload(BaseModel):
    level_id: Optional[int]
    parent: Optional[int]


class DfspLevelValueRequest(SparRequest):
    request_payload: DfspLevelValueRequestPayload


class DfspLevelValueResponse(SparResponse):
    response_payload: List[DfspLevelValueSchema]
