import pandas as pd
import yfinance as yf
data = yf.download("AAPL", start="2020-01-01")
print(data.head())
data["returns"] = data['Close'].pct_change()
print(data[['Close','returns']].tail(10))
