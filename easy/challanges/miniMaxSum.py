#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    #REMEMBER THAT using : in array you can call in the range
    print(sum(arr[:4]), end=" ")
    print(sum(arr[1:]))


if __name__ == '__main__':
    arr = [1,2,3,4,5]

    miniMaxSum(arr)
