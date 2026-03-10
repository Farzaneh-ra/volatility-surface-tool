import pandas as pd
data = pd.DataFrame({"AAPL":[180,182,181,185,188],"MSFT":[330,332,331,335,338]})
returns = data.pct_change()
print("prices: ", data)
print("\nreturns: ",returns)