import threading
import websocket
import json
from db import set_data
import logging

logging.basicConfig(level=logging.INFO)


class BaseHandler:
    WS_URL = None

    def __init__(self, pair=None):
        self.pair = pair or []

    def on_message(self, ws, message):
        logging.info(message)

    def on_error(self, ws, error):
        logging.error(error)

    def on_close(self, ws):
        logging.info(f"### {self.__class__.__name__} connection closed ###")

    def on_open(self, ws):
        logging.info(f"### {self.__class__.__name__} connected ###")

    def create_connect(self):
        ws = websocket.WebSocketApp(
            self.WS_URL,
            on_message=self.on_message,
            on_error=self.on_message,
            on_close=self.on_message,
        )
        ws.on_open = self.on_open
        wst = threading.Thread(target=ws.run_forever)
        wst.start()


class Binance(BaseHandler):
    WS_URL = 'wss://stream.binance.com:9443/ws/!bookTicker'
    # WS_URL = 'wss://stream.binance.com:9443/ws/ethusdt@bookTicker/btcusdc@bookTicker/btcc@bookTicker'

    def on_message(self, ws, message):
        resp = json.loads(message)
        price = round((float(resp['a']) + float(resp['b'])) / 2, 6)
        set_data(self.__class__.__name__, resp['s'], price)


class Kraken(BaseHandler):
    WS_URL = "wss://ws.kraken.com/"

    def on_message(self, ws, message):
        resp = json.loads(message)
        price = round((float(resp[1]['a'][0]) + float(resp[1]['b'][0])) / 2, 6)
        pair = resp[-1].replace('/', '')
        set_data(self.__class__.__name__, pair, price)

    def on_open(self, ws):
        msg = {
            "event": "subscribe",
            "pair": ["XBT/USD", "XBT/EUR", "ETH/USD", "ETH/EUR", 'BTC/USDC', 'ETH/USDT'],
            "subscription": {"name": "ticker"}
        }
        ws.send(json.dumps(msg))
