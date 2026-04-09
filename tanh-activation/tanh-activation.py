import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """

    x = np.array (x, dtype = np.float32)
    x_exp, neg_exp = np.exp(x), np.exp(-x)
    return ( x_exp - neg_exp) / ( x_exp + neg_exp)
    pass

    tanh([0, 1, -1, 3])