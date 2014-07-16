'''
Name: Andrew Tillett
Date: 7/16/14
Class: Design Patters for Web Programming Online 1407
Assignment: Encapsulated Calculator
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
