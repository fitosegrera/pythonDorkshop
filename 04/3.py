#!/usr/bin/python

"""
TUTORIAL4 Libraries
"""

"""
We can also create an instance of the library whe we call it:
"""
import time as myObject #myObject is an arbitrary name

state = True
count = 0


def myFunction(seconds):
    global state #We call the global variable state before using it
    while state:
        global count #We call the global variable count befor using it
        if count == 10:
            print count
            state = False
        else:
            print count
            myObject.sleep(seconds) #now myObject contains all the elements of the time library
            count += 1

myFunction(1)
