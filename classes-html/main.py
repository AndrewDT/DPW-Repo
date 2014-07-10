'''
Andrew Tillett
7/10/14
Classes-HTML
'''
import webapp2
#could say import pages
from pages import Page #From file(packet) import Page class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.body = "Miss Piggy likes Kermit De Frog"
        self.response.write(p.print_out()) #.response.write - writes to page


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
