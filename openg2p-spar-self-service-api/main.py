#!/usr/bin/env python3

# ruff: noqa: I001

from openg2p_spar_self_service_api.app import Initializer as SparInitializer
from openg2p_fastapi_common.ping import PingInitializer

main_init = SparInitializer()
PingInitializer()

main_init.main()
