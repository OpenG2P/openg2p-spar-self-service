from functools import cached_property
from typing import Any, Dict, List, Optional

from openg2p_g2pconnect_mapper_lib.client import (
    MapperLinkClient,
    MapperResolveClient,
    MapperUnlinkClient,
    MapperUpdateClient,
)
from openg2p_spar_mapper_interface_lib.interface import MapperInterface
from openg2p_spar_mapper_interface_lib.response import MapperResponse

from .config import Settings
from .helper import MapperConnectorHelper

_config = Settings.get_config()


class MapperConnector(MapperInterface):
    @cached_property
    def helper(self) -> MapperConnectorHelper:
        return MapperConnectorHelper.get_component()

    @cached_property
    def link_client(self) -> MapperLinkClient:
        return MapperLinkClient.get_component()

    @cached_property
    def unlink_client(self) -> MapperUnlinkClient:
        return MapperUnlinkClient.get_component()

    @cached_property
    def resolve_client(self) -> MapperResolveClient:
        return MapperResolveClient.get_component()

    @cached_property
    def update_client(self) -> MapperUpdateClient:
        return MapperUpdateClient.get_component()

    async def link(
        self,
        id: str,
        fa: str,
        name: Optional[str],
        phone_number: Optional[str],
        additional_info: Optional[List[Dict[str, Any]]],
    ) -> MapperResponse:
        request = await self.helper.construct_link_request(id, fa, name, phone_number, additional_info)
        response = await self.link_client.link_request(request)
        return await self.helper.construct_mapper_response_link(response)

    async def unlink(self, id: str) -> MapperResponse:
        request = await self.helper.construct_unlink_request(id)
        response = await self.unlink_client.unlink_request(request)
        return await self.helper.construct_mapper_response_unlink(response)

    async def resolve(self, id: str) -> MapperResponse:
        request = await self.helper.construct_resolve_request(id)
        response = await self.resolve_client.resolve_request(request)
        return await self.helper.construct_mapper_response_resolve(response)

    async def update(
        self,
        id: str,
        fa: str,
        name: Optional[str],
        phone_number: Optional[str],
        additional_info: Optional[List[Dict[str, Any]]],
    ) -> MapperResponse:
        request = await self.helper.construct_update_request(id, fa, name, phone_number, additional_info)
        response = await self.update_client.update_request(request)
        return await self.helper.construct_mapper_response_update(response)
