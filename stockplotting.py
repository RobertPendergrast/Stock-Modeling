import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

def get_stock_data(stock):
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d')

    start = '2012-01-01'
    stop = formatted_date
    stocks = ['META','IMB','AAPL','GOOG','TSLA']
    data = yf.download(stock, start, stop)
    print(stock)
    print(data.head())

    return data

def plot_stock_data(data, stock, model =None):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label = f"{stock}Close Price")

    if model is not None:
        plt.plot(model, label=f'{stock} Moving Average', linestyle='--')


    plt.title(f'Stock Prices for {stock}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.show()

def calculate_average(data, window):
    average = data['Close'].rolling(window=window).mean()
    return average

stock_name = input("Enter the stock symbol: ").upper() 
stock_data = get_stock_data(stock_name)
average = calculate_average(stock_data,100)
plot_stock_data(stock_data, stock_name, model=average)