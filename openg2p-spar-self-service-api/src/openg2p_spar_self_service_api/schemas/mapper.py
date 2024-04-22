from .request import SparRequest
from .response import SparResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any


STRATEGY_ID_KEY = "strategy_id"


class KeyValuePair(BaseModel):
    key: str
    value: str


class Fa(BaseModel):
    level_id: int
    level_name: str
    level_code: str
    parent_level_id: int
    level_value_id: str
    strategy_id: Optional[int] = None
    level_value_name: str
    level_value_code: str
    sub_fa: Optional["Fa"] = None


class SelfServiceLinkRequestPayload(BaseModel):
    fa: Fa
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[Dict[str, Any]]] = None


class SelfServiceLinkRequest(SparRequest):
    request_payload: SelfServiceLinkRequestPayload


class SelfServiceLinkResponsePayload(BaseModel):
    id: str
    fa: Fa
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[Dict[str, Any]]] = None


class SelfServiceLinkResponse(SparResponse):
    response_payload: SelfServiceLinkResponsePayload


class SelfServiceUpdateRequestPayload(BaseModel):
    fa: Fa
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[Dict[str, Any]]] = None


class SelfServiceUpdateRequest(SparRequest):
    request_payload: SelfServiceUpdateRequestPayload


class SelfServiceUpdateResponsePayload(BaseModel):
    id: Optional[str] = None
    fa: Optional[Fa] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[Dict[str, Any]]] = None


class SelfServiceUpdateResponse(SparResponse):
    response_payload: SelfServiceUpdateResponsePayload


class SelfServiceResolveRequestPayload(BaseModel):
    pass  # Blank Request


class SelfServiceResolveRequest(SparRequest):
    request_payload: SelfServiceResolveRequestPayload


class SelfServiceResolveResponsePayload(BaseModel):
    fa: Fa
    name: Optional[str] = None
    phone_number: Optional[str] = None
    additional_info: Optional[List[Dict[str, Any]]] = None


class SelfServiceResolveResponse(SparResponse):
    response_payload: SelfServiceResolveResponsePayload


class SelfServiceUnlinkRequestPayload(BaseModel):
    pass  # Blank Request


class SelfServiceUnlinkRequest(SparRequest):
    request_payload: SelfServiceUnlinkRequestPayload


class SelfServiceUnlinkResponsePayload(BaseModel):
    pass  # Blank Response


class SelfServiceUnlinkResponse(SparResponse):
    response_payload: SelfServiceUnlinkResponsePayload
