import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
API_KEY = 'WU51YMKHTXAS05CY'

# Set up the TimeSeries object
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Specify the symbol and interval for the time series data
symbol = 'IBM'
interval = '5min'

# Get the intraday time series data
data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize='full')

# Print a sample of the data
print(data.head(3))

# Plot the closing prices
data['4. close'].plot()
plt.title(f'Intraday Stock Prices for {symbol}')
plt.xlabel('Time')
plt.ylabel('Closing Price')
plt.show()