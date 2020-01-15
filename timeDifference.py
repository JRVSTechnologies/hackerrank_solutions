#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    if(s[-2:] == "AM" and s[:2] == "12"):
        return "00" + s[2:-2]
    elif(s[-2:] == "AM"):
        return s[:-2]
    elif(s[-2:] == "PM" and s[:2] == "12" and int(s[6:8]) > 0):
        return s[:-2]
    else:
        return str(int(s[0:2]) + 12) + s[2:8]


if __name__ == '__main__':
    s = "12:23:45PM"

    print(timeConversion(s))
