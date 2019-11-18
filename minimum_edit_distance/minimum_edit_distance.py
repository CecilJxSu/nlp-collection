#!/usr/bin/env python3
import numpy as np

def minimum_edit_distance(source, target):
    n = len(source)
    m = len(target)
    D = np.empty((n + 1, m + 1))

    # Initialization: the zeroth row and column is the distance from the empty string
    D[0,0] = 0
    for i in range(1,n + 1):
        D[i,0] = D[i-1,0] + deletion_cost(source[i-1])
    for j in range(1,m + 1):
        D[0,j] = D[0,j-1] + insertion_cost(target[j-1])

    # Recurrence relation:
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            D[i,j] = min(D[i-1,j] + deletion_cost(source[i-1]),
                         D[i-1,j-1] + subtitution_cost(source[i-1], target[j-1]),
                         D[i,j-1] + insertion_cost(target[j-1]))

    # Termination
    return D[n,m]

'''
Cost of 1 char deletion
'''
def deletion_cost(ch):
    return 1

'''
Cost of 1 char insertion
'''
def insertion_cost(ch):
    return 1

'''
Cost of 2 chars subtitution, identical chars have zero cost
'''
def subtitution_cost(ch1, ch2):
    return 2 if ch1 != ch2 else 0

if __name__ == '__main__':
    # For example
    distance = minimum_edit_distance("intention", "execution")
    print(distance)
