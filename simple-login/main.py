'''
name
date
class
assignment
'''

import webapp2 #Import Statement - says use the webapp2 library

#Declaring a class
class MainHandler(webapp2.RequestHandler):
    def get(self): #Function that starts everything. Initializing function (Catalyst)
        self.response.write('Hello world!')
        #code goes here

    #or create additional functions
    def additional_functions(self):
        pass
        #code goes here

#LEAVE THIS ALONE (DON'T TOUCH)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
