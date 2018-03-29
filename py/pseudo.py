from __future__ import division
import sys
import os
import pickle

def scan(root):
    fs = {}
    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            f = os.path.join(dirname, filename)
            fs[f] = os.path.getsize(f)
    return fs

def brine(cucumber, lid):
    barrel = open(lid, 'w')
    pickle.dump(cucumber, barrel)
    barrel.close()

def unbrine(lid):
    barrel = open(lid, 'r')
    cucumber = pickle.load(barrel)
    barrel.close()
    return cucumber

def combine(vvectordict, hvectordict, operation):
    matrixdict = {}
    for row in vvectordict:
        for column in hvectordict:
            if(row > column):
                matrixdict[(row, column)] = operation(vvectordict[row], hvectordict[column])
    return matrixdict

def autocombine(vectordict, operation):
    return combine(vectordict, vectordict, operation)

def rationalize(first, second):
    return min(first, second) / max(first, second)

def purge(first, second):
    return None

def invert_dict(table):
    inverse = {}
    for k, v in table.iteritems():
        inverse[v] = inverse.get(v, [])
        inverse[v].append(k)
    return inverse

def transpose_dict(table):
    transpose = {}
    for m in table:
        for n in table[m]:
            if not n in transpose:
                transpose[n] = {}
            transpose[n][m] = table[m][n]
    return transpose

if __name__ == '__main__':
    sized = scan(sys.argv[1])
    size_ratios = autocombine(sized, rationalize)
    inverse = invert_dict(size_ratios)
    brine(inverse, sys.argv[2])
