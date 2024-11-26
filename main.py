#!/usr/bin/env python3

# ruff: noqa: I001

from websub_print_listener.app import Initializer
from openg2p_fastapi_common.ping import PingInitializer

main_init = Initializer()
PingInitializer()

main_init.main()
