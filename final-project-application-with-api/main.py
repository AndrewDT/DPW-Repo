'''
Name: Andrew Tillett
Date: 7/28/14
Class: DPW Online 1407
Assignment: Final Project: Application with API

'''
import webapp2
import urllib2 #gives us python classes and code needed to requesting info, receiving, and opening
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Book Search App</title>
    </head>
    <body>
        '''
        self._body = "Book Searching Application"
        self._close = '''

    </body>
</html>
        '''

    def page_write(self):
        return self._head + self._body + self._close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
