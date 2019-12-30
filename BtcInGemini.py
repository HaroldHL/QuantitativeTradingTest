import matplotlib.pyplot as plt
import pandas as pd
import requests

# timeline
periods = '3600'

# get btc via Http
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
  params={
    'periods': periods
  })
data = resp.json()

# convert pandas data frame
df = pd.DataFrame(
  data['result'][periods],
  columns=[
    'CloseTime',
    'OpenPrice',
    'HighPrice',
    'LowPrice',
    'ClosePrice',
    'Volume',
    'NA'])

# output head
print(df.head())

# graph
df['ClosePrice'].plot(figsize=(14, 7))

plt.show()