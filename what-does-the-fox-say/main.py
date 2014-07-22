'''
Name: Andrew Tillett
Date: 7/22/14
Class: DPW - Online 1407
Assignment: What Does the Fox Say?

Create an Abstract Animal class (with the appropriate properties, attributes and methods). This should include a method for the animal making a sound.
3 Animal Classes that will inherit from the AbstractAnimal class and that will have attributes for the following:
Properties:
Phylum
Class
Order
Family
Genus
URL for the image of the animal
Average Lifespan
Habitat
Geolocation
Methods:
Method that overrides the AbstractAnimal's sound-making method. This is so the Animal will make it's own, more specific sound.
There should be an instance created of each of the animal classes and they should be stored within an array.
There should be a button (or link) for each item.
When a button is clicked, your application should show the data for the animal that button represents.
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
