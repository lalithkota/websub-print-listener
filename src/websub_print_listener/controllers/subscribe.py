import logging

from openg2p_fastapi_common.controller import BaseController

from ..config import Settings

_config = Settings.get_config()
_logger = logging.getLogger(_config.logging_default_logger_name)


class SubscribeController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.router.prefix += "/internal"
        self.router.tags += ["subscribe"]

        self.router.add_api_route(
            "/subscribe",
            self.post_subscribe,
            responses={200: {"description": "Subscribed"}},
            methods=["POST"],
        )
        self.router.add_api_route(
            "/unsubscribe",
            self.post_unsubscribe,
            responses={200: {"description": "Unsubscribed"}},
            methods=["POST"],
        )

    def post_subscribe(self):
        pass

    def post_unsubscribe(self):
        pass
