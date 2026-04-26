import numpy as np
def sigmoid(x):
    if isinstance( x, (int, float)):
       return 1/(1+np.exp(-x))

    return [sigmoid(ele) for ele in x ]
    """
    Vectorized sigmoid function.
    """