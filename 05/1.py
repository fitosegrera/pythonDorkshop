#!/usr/bin/python

"""
TUTORIAL5 Classes
"""

"""
Lets create our first class in python
"""
import random as r

class MyClass:

    def myFunction(self, x):
        for i in range(x):
            print i

    def myOtherFunction(self, y):
        x = 0
        for item in range(y):
            x += r.random() * item
        return x

c = MyClass()
c.myFunction(100)
result = c.myOtherFunction(30)
print "/////////////"
print result