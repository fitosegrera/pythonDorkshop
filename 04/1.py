#!/usr/bin/python

"""
TUTORIAL4 Libraries
"""

"""
In python we use import to call a library installed in your system
"""
import time

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
            time.sleep(seconds)
            count += 1

myFunction(1)
