import numpy as np

def cost(y, y_hat):
    
   return np.sum(0.5*(y - y_hat) ** 2)