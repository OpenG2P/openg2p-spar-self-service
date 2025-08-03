from enum import Enum
from typing import Any

from pydantic import BaseModel


class StatusEnum(Enum):
    rcvd = "rcvd"
    pdng = "pdng"
    succ = "succ"
    rjct = "rjct"


class MapperErrorCode(Enum):
    rjct_reference_id_invalid = "rjct.reference_id.invalid"
    rjct_reference_id_duplicate = "rjct.reference_id.duplicate"
    rjct_timestamp_invalid = "rjct.timestamp.invalid"
    rjct_id_invalid = "rjct.id.invalid"
    rjct_fa_invalid = "rjct.fa.invalid"
    rjct_name_invalid = "rjct.name.invalid"
    rjct_mobile_number_invalid = "rjct.mobile_number.invalid"
    rjct_unknown_retry = "rjct.unknown.retry"
    rjct_other_error = "rjct.other.error"


class MapperResponse(BaseModel):
    id: str | None = None
    fa: str | None = None
    name: str | None = None
    phone_number: str | None = None
    account_provider_info: Any | None = None
    additional_info: list[dict] | None = None
    status: str | None = None
    mapper_error_code: str | None = None
    mapper_error_message: str | None = None
