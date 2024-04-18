from openg2p_fastapi_common.service import BaseService
from openg2p_mapper_interface_lib import MapperInterface, MapperResponse
from typing import Optional, List, Dict, Any

from openg2p_g2pconnect_mapper_lib.schemas import (
    LinkResponse,
    UnlinkResponse,
    UpdateResponse,
    ResolveResponse,
)
from openg2p_g2pconnect_mapper_lib.client import (
    MapperLinkService,
    MapperUnlinkService,
    MapperUpdateService,
    MapperResolveService,
)

from .helper import MapperConnectorHelper


class MapperConnector(BaseService, MapperInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def link(
        self,
        id: str,
        fa: str,
        name: Optional[str],
        phone_number: Optional[str],
        additional_info: Optional[List[Dict[str, Any]]],
    ) -> MapperResponse:
        mapper_connector_helper = MapperConnectorHelper.get_component()
        link_request_message = await mapper_connector_helper.construct_link_request(
            id, fa, name, phone_number, additional_info
        )
        link_response: LinkResponse = (
            await MapperLinkService.get_component().link_request(link_request_message)
        )
        mapper_response = await mapper_connector_helper.construct_mapper_response_link(
            link_response
        )
        return mapper_response

    async def unlink(self, id: str) -> MapperResponse:
        mapper_connector_helper = MapperConnectorHelper.get_component()
        unlink_request_message = await mapper_connector_helper.construct_unlink_request(
            id
        )
        unlink_response: (
            UnlinkResponse
        ) = await MapperUnlinkService.get_component().unlink_request(
            unlink_request_message
        )
        mapper_response = (
            await mapper_connector_helper.construct_mapper_response_unlink(
                unlink_response
            )
        )
        return mapper_response

    async def resolve(self, id: str) -> MapperResponse:
        mapper_connector_helper = MapperConnectorHelper.get_component()
        resolve_request_message = (
            await mapper_connector_helper.construct_resolve_request(id)
        )
        resolve_response: (
            ResolveResponse
        ) = await MapperResolveService.get_component().resolve_request(
            resolve_request_message
        )
        mapper_response = (
            await mapper_connector_helper.construct_mapper_response_resolve(
                resolve_response
            )
        )
        return mapper_response

    async def update(
        self,
        id: str,
        fa: str,
        name: Optional[str],
        phone_number: Optional[str],
        additional_info: Optional[List[Dict[str, Any]]],
    ) -> MapperResponse:
        mapper_connector_helper = MapperConnectorHelper.get_component()
        update_request_message = await mapper_connector_helper.construct_update_request(
            id, fa, name, phone_number, additional_info
        )
        update_response: (
            UpdateResponse
        ) = await MapperUpdateService.get_component().update_request(
            update_request_message
        )
        mapper_response = (
            await mapper_connector_helper.construct_mapper_response_update(
                update_response
            )
        )
        return mapper_response
