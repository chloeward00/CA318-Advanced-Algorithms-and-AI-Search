import numpy as np

def sigmoid(z):
   return 1 / (1 + np.exp(-z))

def sol():

    z = np.array([
    [0.99, 0.71, 0.4, ],
    [0.54, 0.3, 0.38, ],
    [0.29, 0.41, 0.46, ],
    ])
    return sigmoid(z)