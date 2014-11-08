#!/usr/bin/python

"""
TUTORIAL2 Conditionals and loops in python
"""

"""
In processing a for loop looks like this:

int[] myArray = {100,200,300,400,500};

for(int i = 0; i < myArray.length; i++){
    print(myArray[i]);
}
"""

"""
IN PYTHON:
"""

myList=[100,200,300,400,500,600]

for i in myList:
    print i

#If you want to create a for loop in an specific range:

for i in range(10):
    print i

#Iterate through a list
myList = [100,200,300,400,500,600,700,800]

for i in range(len(myList)):
    print myList[i]

