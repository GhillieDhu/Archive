from __future__ import division
import sys
from math import log, sqrt

def find_ratio(s, n):
    func = lambda r : (1 + s * (r - 1))**(1/n)
    return Y(func, 1.000001, 0.000001)

def Y(func, x, tol):
    if abs((x - func(x)) / x) < tol:
        return x
    else:
        return Y(func, func(x), tol)

if __name__ == '__main__':
    print(find_ratio(365, int(sys.argv[1])))
