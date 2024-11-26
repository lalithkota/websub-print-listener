# ruff: noqa: E402

from .config import Settings

_config = Settings.get_config()

from openg2p_fastapi_common.app import Initializer

from .controllers.receive import InternalController
from .controllers.subscribe import SubscribeController
from .controllers.subscribe_confirm import SubscribeConfirmController


class Initializer(Initializer):
    def initialize(self, **kwargs):
        super().initialize()

        InternalController().post_init()
        SubscribeController().post_init()
        SubscribeConfirmController().post_init()
