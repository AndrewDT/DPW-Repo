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
        wolf = GrayWolf()
        wolf.phylum = "Chordata"
        wolf.classification = "Mammalia"
        wolf.order = "Carnivora"
        wolf.family = "Canidae"
        wolf.genus = "Canis"
        wolf.avg_lifespan = "7 years"
        wolf.img_url = "http://www-tc.pbs.org/wnet/nature/files/2012/04/wolffact-post.jpg"
        wolf.habitat = "Arctic Tundra, Dense Forests, Mountains, Dry Shrublands"
        wolf.geolocation = "North America, Europe, Asia, Canadian Arctic, India"
        self.response.write(wolf.print_out())

        badger = HoneyBadger()
        badger.phylum = "Chordata"
        badger.classification = "Mammalia"
        badger.order = "Carnivora"
        badger.family = "Mustelidae"
        badger.genus = "Mellivora"
        badger.avg_lifespan = "26 years"
        badger.img_url = "http://animals.sandiegozoo.org/sites/default/files/styles/feeds_animal_thumbnail/public/honey_badger_thumb.jpg?itok=fu1a3BG_"
        badger.habitat = "Dry areas, Forests, Grasslands"
        badger.geolocation = "Africa, Asia"
        self.response.write("<br/>" + badger.print_out())


class Mammals(object):
    def __init__(self):
        self.phylum = ""
        self.classification = ""
        self.order = ""
        self.family = ""
        self.genus = ""
        self.img_url = ""
        self.avg_lifespan = ""
        self.habitat = ""
        self.geolocation = ""
        self.noise = ""

    def wake_up(self):
        pass

    def eat(self):
        pass

    def run(self):
        pass

    def make_noise(self):
        pass

    def sleep(self):
        pass

    def print_out(self):
        return self.phylum + self.classification + self.order + self.family + self.genus + self.img_url + self.avg_lifespan + self.habitat + self.geolocation + self.noise

class GrayWolf(Mammals):
    def __init__(self):
        super(GrayWolf, self).__init__()

    def make_noise(self):
        return self.noise

    def print_out(self):
        return self.phylum + self.classification + self.order + self.family + self.genus + self.img_url + self.avg_lifespan + self.habitat + self.geolocation + self.noise

class HoneyBadger(Mammals):
    def __init__(self):
        super(HoneyBadger, self).__init__()

    def make_noise(self):
        return self.noise

    def print_out(self):
        return self.phylum + self.classification + self.order + self.family + self.genus + self.img_url + self.avg_lifespan + self.habitat + self.geolocation + self.noise


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
