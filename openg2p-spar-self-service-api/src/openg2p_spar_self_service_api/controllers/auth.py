import logging

from openg2p_fastapi_auth.controllers.auth_controller import AuthController as BaseAuthController

from ..config import Settings
from ..models.login_provider import LoginProvider

_config = Settings.get_config()
_logger = logging.getLogger(_config.logging_default_logger_name)


class AuthController(BaseAuthController):
    async def get_login_provider_db_by_iss(self, iss: str) -> LoginProvider:
        if _config.login_providers_list:
            lp_fields = LoginProvider.__mapper__.columns.keys()
            for lp in _config.login_providers_list:
                if iss == lp.get("iss"):
                    return LoginProvider(
                        **{lp_key: lp_val for lp_key, lp_val in lp.items() if lp_key in lp_fields}
                    )
            return None
        if await LoginProvider.table_exists_cached():
            return await LoginProvider.get_login_provider_from_iss(iss)
        return None
