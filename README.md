## BEST CRYPRO PRICE API

### Start with localhost
1. Install requirements
`pip install -r requirements.txt`

2. Start redis-server

3. Start flask
`python main.py`

4. Start websocket
`python -m ws`

### Start with docker
`docker-compose up`

### Example endpoints
`http://0.0.0.0:5000/exchange`

`http://0.0.0.0:5000/exchange?exchange=Kraken`

`http://0.0.0.0:5000/exchange?pair=ETHUSDT`

`http://0.0.0.0:5000/exchange?pair=ETHUSDT&exchange=Kraken`
