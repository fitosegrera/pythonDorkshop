#!/usr/bin/python

"""
TUTORIAL3 functions
"""

"""
Functions and global variables
"""

# x is working locally in each function

def myFunction1(a, b):
    x = a + b
    return x

def myFunction2(c, d):
    x = c + d
    return x

result1 = myFunction1(5, 10)

result2 = myFunction2(10, 10)

print result1, result2

#Lets try the conventional method used in other languages.
#Lets define the variable outside the functions and notice that now we have 
#3 different x variables. The one outside is not global

x = 0

def myFunction1(a, b):
    x = a + b
    return x

def myFunction2(c, d):
    x = c + d
    return x

result1 = myFunction1(5, 10)

result2 = myFunction2(10, 10)

print result1, result2

#To work with global variables in python you should do the following:

y = 10

def myFunction1(a, b):
    global y
    z = a + b + y
    return z

def myFunction2(c, d):
    global y
    z = c + d + y
    return z

result1 = myFunction1(5, 10)

result2 = myFunction2(10, 10)

print result1, result2