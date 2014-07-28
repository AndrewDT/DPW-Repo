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
        p = FormPage()
        p.inputs = [["text", "title", "Title"], ["text", "authors", "Author(s)"], ["submit", "Search"]]
        self.response.write(p.page_write())



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


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        self._form_open = "<form method='GET'>"
        self._form_fields = ""
        self.__inputs = ""
        self._form_end = "</form>"

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, arr):
        for item in arr:
            self._form_fields += "<input type='" + item[0] + "' name='" + item[1]
            try:
                self._form_fields += "' placeholder='" + item[2] + "' />"
            except:
                self._form_fields += "' />"


    def page_write(self):
        return self._head + self._form_open + self._form_fields + self._form_end + self._body + self._close





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)