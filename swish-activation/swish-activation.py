import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x, dtype = np.float32)
    sigmoid = 1 / (1 + np.exp(-x))
    return x * sigmoid
 
    pass


swish([0, 1, -1, 3])