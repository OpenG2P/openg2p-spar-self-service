from typing import Any

from pydantic import BaseModel

from .dfsp import FaTypeEnum
from .request import SparRequest
from .response import SparResponse

STRATEGY_ID_KEY = "strategy_id"


class TestStrategyResponse(BaseModel):
    constructed_id: str
    constructed_fa: str


class KeyValuePair(BaseModel):
    key: str
    value: str


class Fa(BaseModel):
    strategy_id: int
    fa_type: FaTypeEnum


class BankAccountFa(Fa):
    bank_name: str
    bank_code: str
    branch_name: str
    branch_code: str
    account_number: str


class MobileWalletFa(Fa):
    wallet_provider_name: str
    wallet_provider_code: str
    mobile_number: str


class EmailWalletFa(Fa):
    wallet_provider_name: str
    wallet_provider_code: str
    email_address: str


class SelfServiceLinkRequestPayload(BaseModel):
    fa: BankAccountFa | MobileWalletFa | EmailWalletFa
    name: str | None = None
    phone_number: str | None = None
    additional_info: list[dict[str, Any]] | None = None


class SelfServiceLinkRequest(SparRequest):
    request_payload: SelfServiceLinkRequestPayload


class SelfServiceLinkResponsePayload(BaseModel):
    pass


class SelfServiceLinkResponse(SparResponse):
    response_payload: SelfServiceLinkResponsePayload


class SelfServiceUpdateRequestPayload(BaseModel):
    fa: BankAccountFa | MobileWalletFa | EmailWalletFa
    name: str | None = None
    phone_number: str | None = None
    additional_info: list[dict[str, Any]] | None = None


class SelfServiceUpdateRequest(SparRequest):
    request_payload: SelfServiceUpdateRequestPayload


class SelfServiceUpdateResponsePayload(BaseModel):
    pass


class SelfServiceUpdateResponse(SparResponse):
    response_payload: SelfServiceUpdateResponsePayload


class SelfServiceResolveRequestPayload(BaseModel):
    pass  # Blank Request


class SelfServiceResolveRequest(SparRequest):
    request_payload: SelfServiceResolveRequestPayload


class SelfServiceResolveResponsePayload(BaseModel):
    fa: dict | None = None
    name: str | None = None
    phone_number: str | None = None
    additional_info: list[dict[str, Any]] | None = None


class SelfServiceResolveResponse(SparResponse):
    response_payload: SelfServiceResolveResponsePayload


class SelfServiceUnlinkRequestPayload(BaseModel):
    fa: BankAccountFa | MobileWalletFa | EmailWalletFa


class SelfServiceUnlinkRequest(SparRequest):
    request_payload: SelfServiceUnlinkRequestPayload


class SelfServiceUnlinkResponsePayload(BaseModel):
    pass  # Blank Response


class SelfServiceUnlinkResponse(SparResponse):
    response_payload: SelfServiceUnlinkResponsePayload
