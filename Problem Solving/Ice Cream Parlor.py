#!/bin/python3

import math
import os
import random
import re
import sys

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        y = m - arr[i]
        if y in arr[:i]:
            index1 = arr.index(y) + 1
            index2 = i + 1
    return index1 , index2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
