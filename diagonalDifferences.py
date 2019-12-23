#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    a = getAndAddDiagonalOrder(arr, False)

    b = getAndAddDiagonalOrder(arr, True)

    return abs(a - b)

def getAndAddDiagonalOrder(arr, reverse):
    total = 0
    i = 0
    loopCount = 0
    for subArr in arr:
        if(reverse == True):
            subArr.reverse()
        print(total, end=" ")
        print(" + ", end=" ")
        print(subArr[loopCount], end=" ")
        total = total + subArr[loopCount]
        loopCount += 1

    print(total)
    return total

if __name__ == '__main__':

    arr = [[11,2,4],[4,5,6],[10,8,-12]]

    result = diagonalDifference(arr)

