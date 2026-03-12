import pandas as pd
import numpy as np
data = pd.DataFrame({"AAPL":[180,np.nan,181,185,np.nan],"MSFT":[330,332,np.nan,335,338]})
print("original data: \n",data)
print("looking forward: \n",data.ffill())
print("\n dropped data:\n ", data.dropna())