#!/usr/bin/python

"""
TUTORIAL2 Conditionals and loops in python
"""

"""
We can create boolean states to kill a loop like this:
"""

state = True
counter = 0

while state:
    print counter
    if counter >= 1000:
        state = False
    counter += 1