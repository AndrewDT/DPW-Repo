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
        p.title = "My page!"
        p.css = "css/style.css"
        p.body = "Miss Piggy likes Kermit De Frog"
        self.response.write(p.whole_page)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
