 #!/usr/bin/python

"""
TUTORIAL6 http stuff
"""
"""
Lets work with json data

First lets install a library called simplejson

on your terminal type:

    sudo pip install simplejson

or go to the link and download it manually:

    https://pypi.python.org/pypi/simplejson/
"""

import simplejson as json
import urllib2

response = urllib2.urlopen('http://date.jsontest.com') #we do the call
data = response.read() #We read the data
print "The JSON looks like this:"
print data
data = json.loads(data)#We load it into python a JSON
date = data['date']#We extract the value of the key "date"
print "Printing only the value of the key 'date':"
print date