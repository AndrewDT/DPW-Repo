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
        wolf.name = "Gray Wolf"
        wolf.phylum = "Chordata"
        wolf.classification = "Mammalia"
        wolf.order = "Carnivora"
        wolf.family = "Canidae"
        wolf.genus = "Canis"
        wolf.avg_lifespan = "7 years"
        wolf.img_url = "http://www-tc.pbs.org/wnet/nature/files/2012/04/wolffact-post.jpg"
        wolf.habitat = "Arctic Tundra, Dense Forests, Mountains, Dry Shrublands"
        wolf.geolocation = "North America, Europe, Asia, Canadian Arctic, India"
        wolf.make_noise()

        badger = HoneyBadger()
        badger.name ="Honey Badger"
        badger.phylum = "Chordata"
        badger.classification = "Mammalia"
        badger.order = "Carnivora"
        badger.family = "Mustelidae"
        badger.genus = "Mellivora"
        badger.avg_lifespan = "26 years"
        badger.img_url = "http://animals.sandiegozoo.org/sites/default/files/styles/feeds_animal_thumbnail/public/honey_badger_thumb.jpg?itok=fu1a3BG_"
        badger.habitat = "Dry areas, Forests, Grasslands"
        badger.geolocation = "Africa, Asia"
        badger.make_noise()

        kangaroo = Kangaroo()
        kangaroo.name = "Kangaroo"
        kangaroo.phylum = "Chordata"
        kangaroo.classification = "Mammalia"
        kangaroo.order = "Diprotodontia"
        kangaroo.family = "Macropodidae"
        kangaroo.genus = "Macropus"
        kangaroo.avg_lifespan = "13 years"
        kangaroo.img_url = "http://animals.sandiegozoo.org/sites/default/files/styles/feeds_animal_thumbnail/public/kangaroo_thumb.jpg?itok=b7XyytP2"
        kangaroo.habitat = "All Australian habitats"
        kangaroo.geolocation = "Australia, New Guinea"
        kangaroo.make_noise()

        p = FormPage()
        self.response.write(p.print_out())

        if self.request.GET:
            animal = self.request.GET["animal"]
            if animal == wolf.name:
                p.form = '''
                <p>{wolf.phylum}</p>
                <p>{wolf.classification}</p>
                <p>{wolf.order}</p>
                <p>{wolf.family}</p>
                <p>{wolf.genus}</p>
                <p>{wolf.avg_lifespan}</p>
                <a href="{wolf.img_url}">Gray Wolf Image</a>
                <p>{wolf.habitat}</p>
                <p>{wolf.geolocation}</p>
                <p>{wolf.noise}</p>
                    '''
                p.form = p.form.format(**locals())
                self.response.write(p.head + p.body + p.form + p.close)
            elif animal == badger.name:
                p.form = '''
                <p>{badger.phylum}</p>
                <p>{badger.classification}</p>
                <p>{badger.order}</p>
                <p>{badger.family}</p>
                <p>{badger.genus}</p>
                <p>{badger.avg_lifespan}</p>
                <a href="{badger.img_url}">Honey Badger Image</a>
                <p>{badger.habitat}</p>
                <p>{badger.geolocation}</p>
                <p>{badger.noise}</p>
                    '''
                p.form = p.form.format(**locals())
                self.response.write(p.head + p.body + p.form + p.close)
            elif animal == kangaroo.name:
                p.form = '''
                <p>{kangaroo.phylum}</p>
                <p>{kangaroo.classification}</p>
                <p>{kangaroo.order}</p>
                <p>{kangaroo.family}</p>
                <p>{kangaroo.genus}</p>
                <p>{kangaroo.avg_lifespan}</p>
                <a href="{kangaroo.img_url}">Kangaroo Image</a>
                <p>{kangaroo.habitat}</p>
                <p>{kangaroo.geolocation}</p>
                <p>{kangaroo.noise}</p>
                    '''
                p.form = p.form.format(**locals())
                self.response.write(p.head + p.body + p.form + p.close)




class Mammals(object):
    def __init__(self):
        self.name = ""
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
        print (self.noise)

    def sleep(self):
        pass

    def print_out(self):
        return self.phylum + self.classification + self.order + self.family + self.genus + self.img_url + self.avg_lifespan + self.habitat + self.geolocation + self.noise

class GrayWolf(Mammals):
    def __init__(self):
        super(GrayWolf, self).__init__()

    def make_noise(self):
        self.noise = "Bark"

class HoneyBadger(Mammals):
    def __init__(self):
        super(HoneyBadger, self).__init__()

    def make_noise(self):
        self.noise = "Squeal"

class Kangaroo(Mammals):
    def __init__(self):
        super(Kangaroo, self).__init__()

    def make_noise(self):
        self.noise = "Grunt"


class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Mammal Fact Sheet</title>
    </head>
    <body>
                    '''
        self._body = ''
        self._close = '''

    </body>
</html>
                    '''

    @property
    def head(self):
        return self._head

    @property
    def body(self):
        return self._body

    @property
    def close(self):
        return self._close

    def print_out(self):
        return self._head + self._body + self._close



class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        self.__form = '''
        <form method="GET">
            <input type="submit" name="animal" value="Gray Wolf">
            <input type="submit" name="animal" value="Honey Badger">
            <input type="submit" name="animal" value="Kangaroo">
        </form>
            '''

    @property
    def form(self):
        return self.__form

    @form.setter
    def form(self, new_form):
        self.__form = new_form

    def print_out(self):
        return self.head + self.body + self.form + self.close



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
