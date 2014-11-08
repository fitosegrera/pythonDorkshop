#!/usr/bin/python

"""
TUTORIAL1 Conditionals and loops in python
"""

myVar1 = 10
myVar2 = 5
result = 0

if myVar1 == myVar2:
    result = myVar1 + myVar2

elif myVar1 > myVar2:
    myVar1 += 1
    result = myVar1 * myVar2

else:
    result = myVar1

print "The result is:   ", result
print "this was done by incrementing", myVar1 - 1, "by one, and then multypling myVar1 * myVar2 =", myVar1 * myVar2

