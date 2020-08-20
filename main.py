from yahoo_finance import *
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import *
import matplotlib.pyplot as plt
import json
import datetime

with open('auth.json') as json_file:
    data = json.load(json_file)


cc = CryptoCurrencies(key=data["AlphaKey"], output_format='pandas')

data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')
"""print(data['1a. open (USD)'][1] - data['1a. open (USD)'][1+10] )"""


for x in data['1b. open (USD)']:
    print(x)
