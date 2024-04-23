# ruff: noqa: E402


from .config import Settings

_config = Settings.get_config()
from openg2p_fastapi_common.app import Initializer as BaseInitializer
from openg2p_g2pconnect_mapper_lib.app import MapperLinkService
from .interface import MapperInterface


class Initializer(BaseInitializer):
    def initialize(self, **kwargs):
        super().initialize(**kwargs)
        MapperInterface()
        MapperLinkService()
