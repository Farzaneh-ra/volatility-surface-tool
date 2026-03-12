import pandas as pd
dates = pd.date_range(start="2024-01-01",periods= 60, freq="D")
prices = pd.Series(range(100,160),index=dates)
monthly_prices = prices.resample("ME").last()
print("daily prices: ")
print(prices.head())
print("\nmonthly prices: ", monthly_prices.head())
