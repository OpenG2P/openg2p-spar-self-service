from openg2p_g2pconnect_mapper_lib.config import Settings as BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="spar_selfservice_g2pconnect_", env_file=".env", extra="allow", env_nested_delimiter="__"
    )

    sender_id: str = ""
