#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
# (5 * round(g / 5))
# p % 5 >= 3

def gradingStudents(grades):
    # Write your code here
    regrade = []
    for g in grades:
        if(roundToBase(g) >= 40):
            if(g % 5 >= 3):
                regrade.append(roundToBase(g))
            else:
                regrade.append(g)
        else:
            regrade.append(g)

    return regrade

def roundToBase(n, base = 5):
    return (base * round(n / base))

if __name__ == '__main__':

    grades = [73,67,38,33]

    result = gradingStudents(grades)
