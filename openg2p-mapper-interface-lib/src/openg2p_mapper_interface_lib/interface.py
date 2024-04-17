from .response import MapperResponse
from typing import Optional, List, Dict, Any


class MapperInterface:
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
        raise NotImplementedError()

    async def unlink(self, id: str) -> MapperResponse:
        raise NotImplementedError()

    async def resolve(self, id: str) -> MapperResponse:
        raise NotImplementedError()

    async def update(
        self,
        id: str,
        fa: str,
        name: Optional[str],
        phone_number: Optional[str],
        additional_info: Optional[List[Dict[str, Any]]],
    ) -> MapperResponse:
        raise NotImplementedError()
