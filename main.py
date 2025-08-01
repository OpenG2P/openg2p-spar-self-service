#!/usr/bin/env python

# ruff: noqa: I001
from openg2p_spar_self_service_api.app import Initializer as SparInitializer
from openg2p_spar_g2pconnect_mapper_connector_lib.app import (
    Initializer as MapperConnectorInitializer,
)
from openg2p_fastapi_common.ping import PingInitializer

main_init = SparInitializer()
MapperConnectorInitializer()
PingInitializer()

app = main_init.return_app()

if __name__ == "__main__":
    main_init.main()
