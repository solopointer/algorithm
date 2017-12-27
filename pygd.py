import copy
import math
import numpy as np

def gd(ders, ders2, start_x, alpha, iter_cnt):
    x = copy.deepcopy(start_x)
    x_row,x_col = x.shape
    if x_col != 1:
        return
    for i in xrange(0,iter_cnt): 
        new_x = [0] * x_cnt
        for t in xrange(x_cnt): 
            if ders2 is not None: 
                new_x[t] = x[t] - alpha * ders(x, t) / (ders2(x, t)**2)
            else: 
                new_x[t] = x[t] - alpha * ders(x, t)
        x = copy.deepcopy(new_x)
    return x

if __name__ == '__main__': 
    x = [1,1]
    def derivative(data,i): 
        if i == 0: 
            return math.cos(data[0]) + math.cos(data[0] + data[1])
        elif i == 1: 
            return math.cos(data[1]) + math.cos(data[0] + data[1])
    def derivative2(data,i): 
        if i == 0: 
            return -1 * math.sin(data[0]) - math.sin(data[0]+data[1])
        elif i == 1: 
            return -1 * math.sin(data[1]) - math.sin(data[0]+data[1])
    res = gd(derivative, None, x, 0.1, 1000)
    print res
    res = gd(derivative, derivative2, x, 0.1, 1000)
    print res



