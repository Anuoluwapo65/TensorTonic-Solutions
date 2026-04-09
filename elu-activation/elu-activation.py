import numpy as np  
def elu(x, alpha = 1.0):
    x = np.array(x, dtype = np.float32)
    return np.where(x > 0, x, alpha * (np.exp(x) - 1)).tolist()

elu([1, -1, 0, 2, -0.5])