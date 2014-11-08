#!/usr/bin/python

"""
TUTORIAL6 web scraping to a GMAIL account
"""

import imaplib
import time as t

while True:
    obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
    obj.login('pcomppy', 'pcompPy2014')
    inbox = obj.select('Inbox')
    unreadIds = obj.search(None, 'UnSeen')
    unread = unreadIds[1][0].split()
    unreadCount = len(unread)
    print ''
    print 'inbox', inbox
    print 'ids', unreadIds
    print 'splited', unread
    print 'unread', unreadCount
    t.sleep(3)