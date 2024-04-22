from typing import Annotated
from fastapi import Depends
from openg2p_fastapi_common.controller import BaseController
from openg2p_mapper_interface_lib.interface import MapperInterface, MapperResponse
from openg2p_fastapi_auth.dependencies import JwtBearerAuth
from openg2p_fastapi_auth.models.credentials import AuthCredentials

from ..schemas import (
    SelfServiceLinkRequest,
    SelfServiceLinkResponse,
    SelfServiceUpdateRequest,
    SelfServiceUpdateResponse,
    SelfServiceResolveResponse,
    SelfServiceUnlinkResponse,
    STRATEGY_ID_KEY,
)
from ..helpers import ResponseHelper, StrategyHelper


class SelfServiceController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._mapper_interface = MapperInterface.get_component()

        self.router.prefix += "/selfservice"
        self.router.tags += ["selfservice"]

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

    @property
    def id_mapper_interface(self):
        if not self._mapper_interface:
            self._mapper_interface = MapperInterface.get_component()
        return self._mapper_interface

    async def link(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
        self_service_link_request: SelfServiceLinkRequest,
    ) -> SelfServiceLinkResponse:

        constructed_id = await StrategyHelper().get_component().construct_id(auth)
        constructed_fa = (
            await StrategyHelper()
            .get_component()
            .construct_fa(self_service_link_request.request_payload.fa)
        )

        mapper_response: MapperResponse = await self.id_mapper_interface.link(
            id=constructed_id,
            fa=constructed_fa,
            name=self_service_link_request.request_payload.name,
            phone_number=self_service_link_request.request_payload.phone_number,
            additional_info={
                STRATEGY_ID_KEY: self_service_link_request.request_payload.fa.strategy_id
            },
        )
        self_service_link_response: SelfServiceLinkResponse = (
            ResponseHelper().get_component().construct_link_response(mapper_response)
        )

        return self_service_link_response

    async def update(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
        self_service_update_request: SelfServiceUpdateRequest,
    ) -> SelfServiceUpdateResponse:
        constructed_id = await StrategyHelper().get_component().construct_id(auth)
        constructed_fa = (
            await StrategyHelper()
            .get_component()
            .construct_fa(self_service_update_request.request_payload.fa)
        )
        mapper_response: MapperResponse = await self.id_mapper_interface.update(
            id=constructed_id,
            fa=constructed_fa,
            name=self_service_update_request.request_payload.name,
            phone_number=self_service_update_request.request_payload.phone_number,
            additional_info={
                STRATEGY_ID_KEY: self_service_update_request.request_payload.fa.strategy_id
            },
        )
        self_service_update_response: SelfServiceUpdateResponse = (
            ResponseHelper().get_component().construct_update_response(mapper_response)
        )

        return self_service_update_response

    async def resolve(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
    ) -> SelfServiceResolveResponse:
        constructed_id = await StrategyHelper().get_component().construct_id(auth)
        mapper_response: MapperResponse = await self.id_mapper_interface.resolve(
            id=constructed_id
        )
        self_service_resolve_response: SelfServiceResolveResponse = (
            ResponseHelper().get_component().construct_resolve_response(mapper_response)
        )

        return self_service_resolve_response

    async def unlink(
        self,
        auth: Annotated[AuthCredentials, Depends(JwtBearerAuth())],
    ) -> SelfServiceUnlinkResponse:
        constructed_id = await StrategyHelper().get_component().construct_id(auth)
        mapper_response: MapperResponse = await self.id_mapper_interface.unlink(
            id=constructed_id
        )
        self_service_unlink_response: SelfServiceUnlinkResponse = (
            ResponseHelper().get_component().construct_unlink_response(mapper_response)
        )

        return self_service_unlink_response
