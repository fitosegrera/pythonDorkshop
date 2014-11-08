#!/usr/bin/python

"""
TUTORIAL3 functions
"""

"""
Functions within functions
"""

def myFunction1(a, b):
    x = a + b
    return x

def myFunction2(c, d):
    z = myFunction1(c,d)

print myFunction2(10, 10)
