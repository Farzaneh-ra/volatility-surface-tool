import pandas as pd
import yfinance as yf
data = yf.download("AAPL",start="2020-01-01")
returns = data['Close'].pct_change()
volatility = returns.std() * (252 ** 0.5)
print("annualized volatility: ",volatility)