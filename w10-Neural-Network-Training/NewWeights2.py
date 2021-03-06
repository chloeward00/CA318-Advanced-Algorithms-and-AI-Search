import numpy as np
class NeuralNetwork(object):
   def __init__(self, size_input, size_hidden, size_output):
       self.W1 = np.random.randn(size_input, size_hidden)
       self.W2 = np.random.randn(size_hidden, size_output)

   def forward(self, X):
      self.z2 = np.dot(X, self.W1)
      self.a2 = self.sigmoid(self.z2)
      self.z3 = np.dot(self.a2, self.W2)
      y_hat = self.sigmoid(self.z3)

      return y_hat

   def sigmoid(self, z):
      return 1 / (1 + np.exp(-z))

   def sigmoid_prime(self, z):
      return np.exp(-z) / (1 + np.exp(-z))**2

   def cost(self, X, y):
      y_hat = self.forward(X)
      J = 0.5 * sum((y - y_hat) ** 2)
      return J

   def cost_prime(self, X, y):
      y_hat = self.forward(X)
      delta3 = np.multiply(-(y - y_hat) , self.sigmoid_prime(self.z3))
      # .T transpose of the matrix 
      dJdW2 = np.dot(self.a2.T, delta3)

      delta2 = np.dot(delta3, self.W2.T) * self.sigmoid_prime(self.z2)
      dJdW1 = np.dot(X.T, delta2)

      return dJdW1, dJdW2

def sol():
    np.random.seed(21)
    NN = NeuralNetwork(2, 3, 1)
    # Input data
    N = np.array( ([3,5],[5,1],[10,2]) , dtype = float)
    
    # output vector
    k = np.array( ([75], [82], [93]) , dtype = float)
    
    # scale the input and output data
    N = N / np.amax(N,axis=0)
    k = k / 100
    
    cost1 = NN.cost_prime(N, k)
    dJdW1, dJdW2 = NN.cost_prime(N, k)
    return NN.W2 - dJdW2