import numpy as np

def sigmoid(x):
    x = np.array(x, dtype = np.float32)
    return 1 / ( 1 + np.exp(-x))


sigmoid([0, 2,-2])