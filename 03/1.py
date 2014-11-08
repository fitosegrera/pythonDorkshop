#!/usr/bin/python

"""
TUTORIAL3 functions
"""

"""
In python we don't define the function acording to the return datatype like in openFrameworks or Processing.
To create a function in python:
"""

def myFunction(a, b):
    c = a + b
    return c

result = myFunction(5, 10)
print result

"""
You can also print the return value directly like this:

print myFunction(5,10)

"""