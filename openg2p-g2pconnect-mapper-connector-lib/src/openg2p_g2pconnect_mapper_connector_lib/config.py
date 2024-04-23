from openg2p_fastapi_common.config import Settings as BaseSettings
from pydantic_settings import SettingsConfigDict


from . import __version__


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="spar_core_", env_file=".env", extra="allow"
    )

    openapi_title: str = "SPAR Self Service API"
    openapi_description: str = """
    SPAR Self Service API
    ***********************************
    Further details goes here
    ***********************************
    """
    openapi_version: str = __version__

    db_dbname: str = "openg2p_spar_db"
