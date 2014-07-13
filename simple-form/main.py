'''
Name: Andrew Tillett
Date: 07/13/14
Class: Design Patters for Web Programming Online 1407
Assignment: Simple Form


Create and deliver a form with Python. This form should submit info to a Python script and display the results for the user.

The purpose of the form is of your choosing but your form MUST meet the following requirements:

Collect at least 5 pieces of information from the user.
Use at least one text based input element
Use at least one checkbox input element
Use at least one select element
The form should use the GET method to deliver variables to the following page. The following page should list out the information entered (think of a receipt after an order) in an organized and visually pleasing way.

Design will be an important component of your grade, so do NOT focus purely on function. Your form should look polished, professional, and user friendly. Your design should fit the market (ideal user) of your application and it's overall purpose. For example, if you make a form to collect info for a pizza company, your design should reflect the market that would use this form.

Minimum requirements (Violating these garners an automatic 0):

Remember that, like other assignments in this class, your design skills and choices will be graded!
Comment your code. Everything needs to be explained in detail.
Don't forget to do 20 commits.
You may not use any Python frameworks for this assignment.
Global variables are not permitted.
Any errors will earn an automatic ZERO on this assignment.
'''



import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
