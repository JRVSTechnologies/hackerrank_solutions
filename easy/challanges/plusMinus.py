#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):

    negative = 0
    positive = 0
    zero = 0

    for i in arr:
        if(i < 0):
            negative += 1
        elif(i > 0):
            positive += 1
        elif(i == 0):
            zero += 1

    print(calculateFraction(arr, positive))
    print(calculateFraction(arr, negative))
    print(calculateFraction(arr, zero))

def calculateFraction(arr, count):
    return str.format('{0:.6f}', round(count/len(arr), 6))

if __name__ == '__main__':
    arr = [1, 2, 3, -1, -2, -3, 0, 0]
    plusMinus(arr)
