from typing import Any

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
    helper: MapperConnectorHelper = MapperConnectorHelper.get_cached_component()
    link_client: MapperLinkClient = MapperLinkClient.get_cached_component()
    unlink_client: MapperUnlinkClient = MapperUnlinkClient.get_cached_component()
    resolve_client: MapperResolveClient = MapperResolveClient.get_cached_component()
    update_client: MapperUpdateClient = MapperUpdateClient.get_cached_component()

    async def link(
        self,
        id: str,
        fa: str,
        name: str | None = None,
        phone_number: str | None = None,
        additional_info: list[dict[str, Any]] | None = None,
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
        name: str | None = None,
        phone_number: str | None = None,
        additional_info: list[dict[str, Any]] = None,
    ) -> MapperResponse:
        request = await self.helper.construct_update_request(id, fa, name, phone_number, additional_info)
        response = await self.update_client.update_request(request)
        return await self.helper.construct_mapper_response_update(response)
