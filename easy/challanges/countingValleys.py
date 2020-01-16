#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    seaLevel = 0
    seaLevelState = True
    valleycount = 0
    mountaincount = 0

    #remember it needs to wait for a change in sealevel state to be able to count again

    for n in list(s):
        if(n == "U"):
            seaLevel = seaLevel + 1
        elif(n == "D"):
            seaLevel = seaLevel - 1

        if(seaLevel == 1 and seaLevelState == True):
            mountaincount = mountaincount + 1

        if(seaLevel == -1 and seaLevelState == True):
            valleycount = valleycount + 1

        if(seaLevel == 0):
            seaLevelState = True
        else:
            seaLevelState = False

    return valleycount





if __name__ == '__main__':
    fptr = open("../../input.txt", 'r')

    n = 8

    s = "UDDDUDUU"

    result = countingValleys(n, s)

