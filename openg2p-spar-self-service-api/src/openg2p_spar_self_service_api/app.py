# ruff: noqa: E402

from .config import Settings

_config = Settings.get_config()

import asyncio

from openg2p_fastapi_auth.controllers.oauth_controller import OAuthController
from openg2p_fastapi_common.app import Initializer as BaseInitializer

from .controllers.auth import AuthController
from .controllers.dfsp_controller import DfspController
from .controllers.selfservice_controller import SelfServiceController
from .helpers.response_helper import ResponseHelper
from .helpers.strategy_helper import StrategyHelper
from .models import DfspLevel, DfspLevelValue, LoginProvider, Strategy


class Initializer(BaseInitializer):
    def initialize(self, **kwargs):
        super().initialize(**kwargs)
        AuthController().post_init()
        OAuthController().post_init()
        DfspController().post_init()
        SelfServiceController().post_init()
        StrategyHelper()
        ResponseHelper()

    def migrate_database(self, args):
        super().migrate_database(args)

        async def migrate():
            await Strategy.create_migrate()
            await DfspLevel.create_migrate()
            await DfspLevelValue.create_migrate()
            await LoginProvider.create_migrate()

        asyncio.run(migrate())
