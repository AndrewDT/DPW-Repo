
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        about_button = Button()
        about_button.label = "About Us"
        about_button.show_label()
        contact_button = Button()
        contact_button.label = "Contact Us"
        contact_button.show_label()


#Attributes are usually set up in the initializing function(doesn't have to be)
class Button(object):
    def __init__(self):
        self.label = "" #Public attribute (No underscores)
        self.__size = 60 #Private attribute (2 underscores)
        self._color = "0x00000" #Protected attribute (1 underscore)
        #self.on_roll_over("Hello!!")
        #Without self - no longer attr. Merely a var

    def click(self):
        print "I've been clicked"

    def on_roll_over(self, message):
        print "You've rolled over my button" + message

    def show_label(self):
        print "My label is " + self.label + "height "

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
