import redis

from config import Config

r = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0, decode_responses=True)


def set_data(exchange, pair, price):
    r.hset(exchange, pair, price)


def get_exchange_data(exchange):
    return r.hgetall(exchange)


def get_pair_data(exchange, pair):
    return {pair: r.hget(exchange, pair)}

