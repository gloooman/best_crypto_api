import threading
from pprint import pprint
import websocket
import json
from db import set_data

response = [
    324,
    {
        'a': ['54802.20000', 0, '0.99573065'],
        'b': ['54797.20000', 0, '0.00268922'],
        'c': ['54802.20000', '0.00426935'],
        'v': ['1766.49209202', '4586.48904564'],
        'p': ['55814.70730', '55709.97824'],
        't': [21156, 53737],
        'l': ['54405.00000', '52500.00000'],
        'h': ['57211.80000', '57211.80000'],
        'o': ['56891.10000', '55671.70000']
    },
    'ticker',
    'XBT/USD'
]

db = {}

WS_URL = "wss://ws.kraken.com/"


def on_message(ws, message):
    resp = json.loads(message)
    price = round((float(resp[1]['a'][0]) + float(resp[1]['b'][0])) / 2, 6)
    pair = resp[-1].replace('/', '')
    print(pair)
    set_data('Kraken', pair, price)


def on_error(ws, error):
    print(error)


def on_close(ws):
    pprint(db)
    print("### closed ###")


def on_open(ws):
    msg = {
        "event": "subscribe",
        "pair": ["XBT/USD", "XBT/EUR", "ETH/USD", "ETH/EUR"],
        "subscription": {"name": "ticker"}
    }
    ws.send(json.dumps(msg))


def kraken_ws():
    ws = websocket.WebSocketApp(
        WS_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.on_open = on_open
    wst = threading.Thread(target=ws.run_forever)
    wst.start()


if __name__ == "__main__":
    kraken_ws()