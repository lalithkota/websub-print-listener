from openg2p_fastapi_common.config import Settings
from pydantic_settings import SettingsConfigDict

from . import __version__


class Settings(Settings):
    model_config = SettingsConfigDict(
        env_prefix="websub_print_", env_file=".env", extra="allow"
    )

    openapi_title: str = "Print WebSub Listener"
    openapi_description: str = """
    Print WebSub Listener
    ***********************************
    Further details goes here
    ***********************************
    """
    openapi_version: str = __version__
