from enum import Enum

from pydantic import BaseModel

from .request import SparRequest
from .response import SparResponse


class FaTypeEnum(Enum):
    BANK_ACCOUNT = "BANK_ACCOUNT"
    MOBILE_WALLET = "MOBILE_WALLET"
    EMAIL_WALLET = "EMAIL_WALLET"


class LevelTypeEnum(Enum):
    bank = "bank"
    branch = "branch"
    account = "account"
    mobile_wallet_provider = "mobile_wallet_provider"
    mobile_number = "mobile_number"
    email_wallet_provider = "email_wallet_provider"
    email_address = "email_address"


class InputTypeEnum(Enum):
    input = "input"
    select = "select"


class DfspLevelSchema(BaseModel):
    id: int
    name: str
    level_type: LevelTypeEnum
    input_type: InputTypeEnum | None = None
    parent: int | None = None
    validation_regex: str | None = None


class DfspLevelRequestPayload(BaseModel):
    parent: int | None = None


class DfspLevelRequest(SparRequest):
    request_payload: DfspLevelRequestPayload


class DfspLevelResponse(SparResponse):
    response_payload: list[DfspLevelSchema]


class DfspLevelValueSchema(BaseModel):
    id: int
    name: str
    code: str
    description: str | None = None
    parent: int | None = None
    level_id: int
    strategy_id: int | None = None


class DfspLevelValueRequestPayload(BaseModel):
    level_id: int | None = None
    parent: int | None = None


class DfspLevelValueRequest(SparRequest):
    request_payload: DfspLevelValueRequestPayload


class DfspLevelValueResponse(SparResponse):
    response_payload: list[DfspLevelValueSchema]
