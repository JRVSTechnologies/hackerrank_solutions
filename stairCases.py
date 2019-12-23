#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    x = 1

    while x <= n:
        spaces = (n - x)
        stairBlock = ""
        for _ in range(spaces):
            print(" ", end="")

        for _ in range(x):
            stairBlock += "#"
        print(stairBlock)
        x += 1

if __name__ == '__main__':
    n = 6

    staircase(n)
