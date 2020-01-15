#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    print(ar)
    highestNumber = 0
    for n in ar:
        if(highestNumber < n):
            highestNumber = n

    print(ar.count(highestNumber))

if __name__ == '__main__':
    arr = [3, 2, 1, 3]

    birthdayCakeCandles(arr)
