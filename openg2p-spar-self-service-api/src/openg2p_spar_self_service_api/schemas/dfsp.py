from .request import SparRequest
from .response import SparResponse
from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class LevelTypeEnum(Enum):
    BANK = "BANK"
    BRANCH = "BRANCH"
    ACCOUNT = "ACCOUNT"
    MOBILE_WALLET = "MOBILE_WALLET"
    MOBILE_NUMBER = "MOBILE_NUMBER"


class DfspLevelSchema(BaseModel):
    id: int
    name: str
    level_type: str
    parent: Optional[int] = None
    validation_regex: Optional[str] = None


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
