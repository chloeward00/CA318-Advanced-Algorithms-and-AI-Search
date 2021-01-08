import numpy as np
class NeuralNetwork(object):
   def __init__(self, size_input, size_hidden, size_output):
       self.W1 = np.random.randn(size_input, size_hidden)
       self.W2 = np.random.randn(size_hidden, size_output)
def sol():
    np.random.seed(21)
    NN = NeuralNetwork(2, 3, 1)
    return NN.W1,NN.W2