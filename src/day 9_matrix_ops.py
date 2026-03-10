import numpy as np
returns = np.random.uniform(-1,1,(5,3))
cov_matrix = np.cov(returns, rowvar=False)
corr_matrix = np.corrcoef(returns, rowvar=False)

print("return matrix: ", returns)
print("cov_matrix: ", cov_matrix)
print("corr_matrix: ", corr_matrix)