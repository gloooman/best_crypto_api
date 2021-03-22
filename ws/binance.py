from pprint import pprint
import websocket
import json

response = {
    'A': '5090.00000000',
    'B': '190945.00000000',
    'a': '0.01959800',
    'b': '0.01958000',
    's': 'VTHOUSDT',
    'u': 85602179
}


def on_message(ws, message):
    resp = json.loads(message)
    pprint(resp)
    # diff = round((float(resp['a']) + float(resp['b']))/2, 6)
    # db[resp['s']] = diff


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("### connected ###")


def binance_ws():
    ws = websocket.WebSocketApp(
        "wss://stream.binance.com:9443/ws/!bookTicker",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()


if __name__ == "__main__":
    binance_ws()
