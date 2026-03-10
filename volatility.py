import pandas as pd
import yfinance as yf
data = yf.download("AAPL",start="2020-01-01")
returns = data['Close'].pct_change()
rolling_vol = returns.rolling(30).std() * (252 ** 0.5)
print(rolling_vol.tail())