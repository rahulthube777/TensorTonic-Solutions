import numpy as np

# Also works
# def tanh(x):
#     if( isinstance(x, (int, float))):
#         return (np.exp(x) - np.exp(-x))/ (np.exp(x) + np.exp(-x))
#     list=[]
#     for ele in x:
#         list.append(tanh(ele))

#     return list

def tanh(x):
    return np.tanh(x)