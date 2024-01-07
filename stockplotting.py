import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime('%Y-%m-%d')

start = '2012-01-01'
stop = formatted_date
stocks = ['META','IMB','AAPL','GOOG','TSLA']

for stock in stocks:
    data = yf.download(stock, start, stop)
    print(stock)
    print(data.head())

    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'])
    plt.title(f'Stock Prices for {stock}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.show()