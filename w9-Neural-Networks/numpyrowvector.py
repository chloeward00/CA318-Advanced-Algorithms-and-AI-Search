import numpy as np

def sol():
    np.random.seed(21)
    z = np.random.randn(3,1)
    zT = np.transpose(z)
    return zT
    