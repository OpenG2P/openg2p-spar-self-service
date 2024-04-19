from typing import Annotated, List, Optional
import orjson
from fastapi import Depends
from openg2p_fastapi_common.controller import BaseController
from openg2p_fastapi_common.errors import BaseAppException
from openg2p_mapper_interface_lib.interface import MapperInterface, MapperResponse

from ..schemas import LinkRequest, LinkResponse
from ..helpers import ResponseHelper


class SelfServiceController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._mapper_interface = MapperInterface.get_component()

        self.router.prefix += "/selfservice"
        self.router.tags += ["selfservice"]

        self.router.add_api_route(
            "/link",
            self.link,
            responses={200: {"model": LinkResponse}},
            methods=["POST"],
        )

    @property
    def id_mapper_interface(self):
        if not self._mapper_interface:
            self._mapper_interface = MapperInterface.get_component()
        return self._mapper_interface

    async def link(
        self,
        link_request: LinkRequest,
    ) -> LinkResponse:
        mapper_response: MapperResponse = await self.id_mapper_interface.link(
            link_request
        )
        link_response: LinkResponse = (
            ResponseHelper().get_component().construct_link_response(mapper_response)
        )

        return link_response
