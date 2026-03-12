import pandas as pd
import yfinance as yf
tickers = ["AAPL","MSFT","SPY"]
data = yf.download(tickers,start="2023-01-01",auto_adjust=True)["Close"]
returns = data.pct_change().dropna()
print("Close prices: \n", data.head())
print("\nreturns: \n",returns.head())
