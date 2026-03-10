import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
data = yf.download("AAPL", start="2020-01-01")
returns = data['Close'].pct_change()
rolling_vol = returns.rolling(30).std()* (252**0.5)
rolling_vol.plot()
plt.title("Rolling Volatility")
plt.show()

