import numpy as np


def sigmoid(z):
    return 1 / (1+np.exp(-z))

def sol():

    X = np.array( ([3,5],[5,1],[10,2]) , dtype = float)
    
    # output vector
    y = np.array( ([75], [82], [93]) , dtype = float)
    
    # scale the input and output data
    X = X / np.amax(X,axis=0)
    y = y / 100
    
    # define network parameters
    size_input = np.shape(X)[1] # number of columns of X
    size_hidden = 3
    size_output = 1
    
    # Create the weights
    np.random.seed(21)
    W1 = np.random.randn(size_input,3)
    W2 = np.random.randn(size_hidden,size_output)

    z2 = np.dot(X,W1)
    a2 = sigmoid(z2)

    z3 = np.dot(a2,W2)

    return sigmoid(z3)