from functools import cached_property
from typing import Annotated

from fastapi import Depends
from openg2p_fastapi_auth.dependencies import JwtBearerAuth
from openg2p_fastapi_auth.models.credentials import AuthCredentials
from openg2p_fastapi_common.controller import BaseController
from openg2p_spar_mapper_interface_lib.interface import MapperInterface

from ..config import Settings
from ..helpers import ResponseHelper, StrategyHelper
from ..schemas import (
    STRATEGY_ID_KEY,
    SelfServiceLinkRequest,
    SelfServiceLinkResponse,
    SelfServiceResolveResponse,
    SelfServiceUnlinkResponse,
    SelfServiceUpdateRequest,
    SelfServiceUpdateResponse,
    TestStrategyResponse,
)

_config = Settings.get_config()


class SelfServiceController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.router.prefix += ""
        self.router.tags += ["selfservice"]

        self.router.add_api_route(
            "/test_strategy",
            self.test_strategy,
            responses={200: {"model": TestStrategyResponse}},
            methods=["POST"],
        )
        self.router.add_api_route(
            "/link",
            self.link,
            responses={200: {"model": SelfServiceLinkResponse}},
            methods=["POST"],
        )
        self.router.add_api_route(
            "/update",
            self.update,
            responses={200: {"model": SelfServiceUpdateResponse}},
            methods=["POST"],
        )
        self.router.add_api_route(
            "/resolve",
            self.resolve,
            responses={200: {"model": SelfServiceResolveResponse}},
            methods=["POST"],
        )
        self.router.add_api_route(
            "/unlink",
            self.unlink,
            responses={200: {"model": SelfServiceUnlinkResponse}},
            methods=["POST"],
        )

    @cached_property
    def id_mapper_interface(self) -> MapperInterface:
        return MapperInterface.get_component()

    @cached_property
    def strategy_helper(self) -> StrategyHelper:
        return StrategyHelper.get_component()

    @cached_property
    def response_helper(self) -> ResponseHelper:
        return ResponseHelper.get_component()

    async def test_strategy(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
        self_service_link_request: SelfServiceLinkRequest,
    ) -> TestStrategyResponse:
        constructed_id = await self.strategy_helper.construct_id(auth)
        constructed_fa = await self.strategy_helper.construct_fa(self_service_link_request.request_payload.fa)

        return TestStrategyResponse(constructed_id=constructed_id, constructed_fa=constructed_fa)

    async def link(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
        self_service_link_request: SelfServiceLinkRequest,
    ) -> SelfServiceLinkResponse:
        constructed_id = await self.strategy_helper.construct_id(auth)
        constructed_fa = await self.strategy_helper.construct_fa(self_service_link_request.request_payload.fa)

        mapper_response = await self.id_mapper_interface.link(
            id=constructed_id,
            fa=constructed_fa,
            name=self_service_link_request.request_payload.name,
            phone_number=self_service_link_request.request_payload.phone_number,
            additional_info=[{STRATEGY_ID_KEY: self_service_link_request.request_payload.fa.strategy_id}],
        )

        return await self.response_helper.construct_link_response(mapper_response)

    async def update(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
        self_service_update_request: SelfServiceUpdateRequest,
    ) -> SelfServiceUpdateResponse:
        constructed_id = await self.strategy_helper.construct_id(auth)
        constructed_fa = await self.strategy_helper.construct_fa(
            self_service_update_request.request_payload.fa
        )
        mapper_response = await self.id_mapper_interface.update(
            id=constructed_id,
            fa=constructed_fa,
            name=self_service_update_request.request_payload.name,
            phone_number=self_service_update_request.request_payload.phone_number,
            additional_info=[{STRATEGY_ID_KEY: self_service_update_request.request_payload.fa.strategy_id}],
        )

        return await self.response_helper.construct_update_response(mapper_response)

    async def resolve(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
    ) -> SelfServiceResolveResponse:
        constructed_id = await self.strategy_helper.construct_id(auth)
        mapper_response = await self.id_mapper_interface.resolve(constructed_id)

        return await self.response_helper.construct_resolve_response(mapper_response)

    async def unlink(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
    ) -> SelfServiceUnlinkResponse:
        constructed_id = await self.strategy_helper.construct_id(auth)
        mapper_response = await self.id_mapper_interface.unlink(constructed_id)

        return await self.response_helper.construct_unlink_response(mapper_response)
