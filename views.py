from flask import request, jsonify
from app import app
from db import get_exchange_data, get_pair_data
from ws import IMPL_MAP


@app.route('/exchange')
def exchange():
    birge_exchange = request.args.get('exchange')
    pair = request.args.get('pair')
    if pair and birge_exchange:
        data = {birge_exchange: get_pair_data(birge_exchange, pair)}
    elif pair:
        data = {impl_exchange: get_pair_data(impl_exchange, pair) for impl_exchange in IMPL_MAP.keys()}
    elif birge_exchange:
        data = {birge_exchange: get_exchange_data(birge_exchange)}
    else:
        data = {impl_exchange: get_exchange_data(impl_exchange) for impl_exchange in IMPL_MAP.keys()}
    return jsonify(data)
