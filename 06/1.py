#!/usr/bin/python

"""
TUTORIAL6 http stuff
"""
"""
Lets start by doing a simple http request
"""

import urllib2

response = urllib2.urlopen('http://fii.to/')
html = response.read()
print html

