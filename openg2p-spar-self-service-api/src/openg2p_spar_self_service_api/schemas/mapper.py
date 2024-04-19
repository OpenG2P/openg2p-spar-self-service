from .request import SparRequest
from .response import SparResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class BaseFa(BaseModel):
    level_id: int
    level_name: str
    level_code: str
    parent_level_id: int
    level_value_id: str
    strategy_id: Optional[int]
    level_value_name: str
    level_value_code: str
    sub_fa: Optional[object]


class Fa(BaseFa):
    sub_fa: Optional[BaseFa]


class LinkRequestPayload(BaseModel):
    id: str
    fa: Fa
    name: Optional[str]
    phone_number: Optional[str]
    additional_info: Optional[List[Dict[str, Any]]]


class LinkRequest(SparRequest):
    request_payload: object


class LinkResponsePayload(BaseModel):
    id: str
    fa: Fa
    name: Optional[str]
    phone_number: Optional[str]
    additional_info: Optional[List[Dict[str, Any]]]


class LinkResponse(SparResponse):
    response_payload: LinkResponsePayload
