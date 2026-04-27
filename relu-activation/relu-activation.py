import numpy as np

def relu(x):
    return np.maximum(0, x)


    # Did not work for 2d array
    # if( isinstance(x, (int,float))):
    #     return max(0.0, float(x) );

    # arr = np.zeros(len(x));
    # for i,ele in enumerate(x):
    #     arr[i] = relu(ele)
    # return arr