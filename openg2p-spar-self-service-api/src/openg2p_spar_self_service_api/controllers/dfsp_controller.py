from typing import List

from openg2p_fastapi_common.controller import BaseController
from fastapi import Depends, Query

from ..schemas import (
    DfspLevelResponse,
    DfspLevelSchema,
    DfspLevelRequest,
    DfspLevelValueRequest,
    DfspLevelValueSchema,
    DfspLevelValueResponse,
    ResponseStatus,
)
from ..models import DfspLevel, DfspLevelValue


class DfspController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.router.prefix += "/dfsp"
        self.router.tags += ["dfsp"]

        self.router.add_api_route(
            "/getLevels",
            self.get_dfsp_level,
            responses={200: {"model": DfspLevelResponse}},
            methods=["POST"],
        )
        self.router.add_api_route(
            "/getLevelValues",
            self.get_dfsp_level_values,
            responses={200: {"model": DfspLevelValueResponse}},
            methods=["POST"],
        )

    async def get_dfsp_level(
        self,
        dfsp_level_request: DfspLevelRequest,
    ) -> DfspLevelResponse:

        results = await DfspLevel.get_level(
            parent=dfsp_level_request.request_payload.parent
        )
        dfsp_level_schemas: List[DfspLevelSchema] = [
            DfspLevelSchema.model_validate(result) for result in results
        ]
        return DfspLevelResponse(
            response_status=ResponseStatus.SUCCESS, response_payload=dfsp_level_schemas
        )

    async def get_dfsp_level_values(
        self,
        dfsp_level_value_request: DfspLevelValueRequest,
    ):

        result = await DfspLevelValue.get_level_values(
            parent=dfsp_level_value_request.request_payload.parent
        )
        dfsp_level_value_schemas: List[DfspLevelValueSchema] = [
            DfspLevelValueSchema.model_validate(res) for res in result
        ]
        return DfspLevelValueResponse(
            response_status=ResponseStatus.SUCCESS,
            response_payload=dfsp_level_value_schemas,
        )
