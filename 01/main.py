#!/usr/bin/python
"""
TUTORIAL ON PYTHON'S SYNTAX'
fito_segrera
"""


#---------------COMMENTS-----------------

#This is a single line of comment

"""
This is a comments that allows me to write multiple lines of stuff...
It is the equivalent to /* in languages like c++, processing and javascript*/
"""

#-------------DATA TYPES-----------------

"""
Python as any other language, understands data-types like floats
The diference is that python DOES NOT USE A PREFIX to declare them
"""

#int
myInt = 1

#float
myFloat = 1.0

#String
myString = "This is a string!!"

myBoolean = True

#Lists

myList=[1,2,3,4,5,6]

"""
In the same way you can declare a char, byte, doouble or any other data-type...
Notice that python does not use semicolons at the end of a line!!
"""

#------------BASIC STUFF------------------
"""
Basic math operations are simple
"""

x = 5
y = 7
sum = x + y
subs = y - x
mult = y * x
div = y / x

"""
For mor complex operations you need to use the math library
"""

#----------------INDENTATION-----------------
"""
Python does not use indentation or curly braces. This makes the syntax a little
tricky but at the same time clean, elegant and ordered
"""

"""
Commonly in many languages you will be doing something like:

if (x > y){
    z = x + y;
}else if (x == y){
    z = x;
}else{
    z = y;
}

or

if (x > y){
z = x + y;
}
else if (x == y){
z = x;
}
else{
z = y;
}

Because of the curly braces you can indent however you want
The curly braces mark where an operation starts and end...
"""

"""
This is how we do it in python:
"""

if x > y:
    z = x + y
elif x == y:
    z = x
else:
    z = y

#---------------PRINTING---------------------

"""
Printing in python is very very simple.

Normaly in processing or arduino you do:

print("hello world");

In javascript:

consle.log("hello world");

"""

"""
This is how we do it in python:
"""

print "hello world"

