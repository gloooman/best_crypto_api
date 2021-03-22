import logging

from ws import IMPL_MAP

logging.basicConfig(level=logging.DEBUG)

for exchange, handler in IMPL_MAP.items():
    handler().create_connect()
    logging.info(f'Start handler: {exchange}')