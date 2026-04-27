import numpy as np

def tanh(x):
    # return np.divide(np.exp(x) - np.exp(-x), np.exp(x) + np.exp(-x))
    if( isinstance(x, (int, float))):
        return (np.exp(x) - np.exp(-x))/ (np.exp(x) + np.exp(-x))
    list=[]
    for ele in x:
        list.append(tanh(ele))

    return list