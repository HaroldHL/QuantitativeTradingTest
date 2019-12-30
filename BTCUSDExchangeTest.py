import json
import requests

gemini_ticker ='http://api.gemini.com/v1/pubticker/{}'
symbol ='btcusd'
btc_data = requests.get(gemini_ticker.format(symbol)).json()

print(json.dumps(btc_data,indent = 4))