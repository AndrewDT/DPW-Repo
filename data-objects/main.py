'''
Andrew Tillett
7/10/14
Design Patters for Web Programming Online 1407
Data-Objects
'''

#Data objects allow us to treat classes as a holder of data

#data objects
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        luke = Character()
        luke.name = "Luke Skywalker"
        luke.profession = "Jedi Knight"
        luke.age = 26
        luke.home_planet = "Tattooine"

        leia = Character()
        leia.name = "Princess Leia"
        leia.profession = "Princess"
        leia.age = luke.age
        leia.home_planet = "Alderan"

        yoda = Character()
        yoda.name = "Master Yoda"
        yoda.profession = "Jedi Master"
        yoda.age = 762
        yoda.home_planet = "Dagobah"

        chars = [luke, leia, yoda]
        print chars[1].profession

class Character(object):
    def __init__(self): #constructor function
        self.name = ""
        self.profession = ""
        self.age = 0
        self.home_planet = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
