from typing import Any

from openg2p_fastapi_common.service import BaseService

from .response import MapperResponse


class MapperInterface(BaseService):
    async def link(
        self,
        id: str,
        fa: str,
        name: str | None = None,
        phone_number: str | None = None,
        additional_info: list[dict[str, Any]] | None = None,
    ) -> MapperResponse:
        raise NotImplementedError()

    async def unlink(self, id: str) -> MapperResponse:
        raise NotImplementedError()

    async def resolve(self, id: str) -> MapperResponse:
        raise NotImplementedError()

    async def update(
        self,
        id: str,
        fa: str,
        name: str | None = None,
        phone_number: str | None = None,
        additional_info: list[dict[str, Any]] | None = None,
    ) -> MapperResponse:
        raise NotImplementedError()
