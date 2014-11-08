#!/usr/bin/python

"""
TUTORIAL4 Libraries
"""

"""
We can also call a specific object from a library by typing
"""
from time import sleep

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
            sleep(seconds) #Notice that we doont use dot notation time.sleep(seconds) we only use sleep(seconds)
            count += 1

myFunction(1)
