#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# This one is a bit complicated, we have use a debug matrix to see where the jumps are going over the safe clouds
# here you can see and be explained below
def jumpingOnClouds(c):

    #we need a doublejump counter to see how many clouds can we skipJump
    doubleJump = 0
    #we start at negative because we start at index 0
    safecounter = -1
    #counter will help us to count the amount of steps we took to see if its a single or double jump
    counter = 0
    #first jump is to see we dont count the first cloud thus the safe cloud should be 2 counts
    firstjump = True

    #validate when it should by binary count 3 clouds or 2 clouds for midway jump before thundercloud
    # remember after a thunder cloud the counter of a jump should start at 1 as a jump over safe cloud to thunder cloud
    # is a given step
    skipJumpValidate = 3

    #print("n, ct, sc, dj, sjv")

    for n in c:

        #we check if the counter has reached 3 - this means it has double jump into the clouds skipping one
        if(counter == skipJumpValidate):
            #make sure that the jump to thundercloud is not included
            if(n != 1):
                doubleJump += 1
                #now mid jump only need to skip single cloud to do double instead of 3 when passing thunder
                skipJumpValidate = 2
                counter = 0

        #we need to identify if its the first jump as its only a
        if (firstjump and counter == 2):
            if(n != 1):
                doubleJump += 1
                firstjump = False

        #if cloud is thunder
        if(n == 1):
            counter = 0
            #now after passing thunder it has to validate 3 clouds
            skipJumpValidate = 3
            firstjump = False

        #if cloud is safe
        if (n == 0):
            safecounter += 1

        #debug matrix
        #print(n, end=" ")
        #print(counter, end=" ")
        #print(safecounter, end=" ")
        #print(doubleJump, end=" ")
        #print(skipJumpValidate)

        #counter at the bottom of the for loop
        counter += 1

    #print(safecounter - doubleJump)

    return safecounter - doubleJump


if __name__ == '__main__':

    #c = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]  #7

    #c = [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0] #5

    #c = [0, 0, 1, 0, 0, 1, 0] #4

    c = [0, 0, 0, 1, 0, 0] #3

    #c = [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
    #1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] #53

    result = jumpingOnClouds(c)

