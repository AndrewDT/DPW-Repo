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
        animals = [Wolf(), Badger(), Kangaroo()]


        p = FormPage()
        p.whole_page = p.head + p.body + p.form
        self.response.write(p.whole_page)

        animals[0].name = "Gray Wolf"
        animals[0].phylum = "Chordata"
        animals[0].classification = "Mammalia"
        animals[0].order = "Carnivora"
        animals[0].family = "Canidae"
        animals[0].genus = "Canis"
        animals[0].avg_lifespan = "7 years"
        animals[0].img_url = "images/wolf_pack.jpg"
        animals[0].habitat = "Arctic Tundra, Dense Forests, Mountains, Dry Shrublands"
        animals[0].geolocation = "North America, Europe, Asia, Canadian Arctic, India"
        animals[0].make_noise()

        animals[1].name = "Honey Badger"
        animals[1].phylum = "Chordata"
        animals[1].classification = "Mammalia"
        animals[1].order = "Carnivora"
        animals[1].family = "Mustelidae"
        animals[1].genus = "Mellivora"
        animals[1].avg_lifespan = "26 years"
        animals[1].img_url = "images/honey_badger.jpg"
        animals[1].habitat = "Dry areas, Forests, Grasslands"
        animals[1].geolocation = "Africa, Asia"
        animals[1].make_noise()

        animals[2].name = "Kangaroo"
        animals[2].phylum = "Chordata"
        animals[2].classification = "Mammalia"
        animals[2].order = "Diprotodontia"
        animals[2].family = "Macropodidae"
        animals[2].genus = "Macropus"
        animals[2].avg_lifespan = "13 years"
        animals[2].img_url = "images/kangaroos.jpg"
        animals[2].habitat = "All Australian habitats"
        animals[2].geolocation = "Australia, New Guinea"
        animals[2].make_noise()

        if self.request.GET:
            animal = self.request.GET["animal"]
            if animal == animals[0].name:
                p.form_results = '''
        <div class="info_container_whole">
            <img src="{animals[0].img_url}" height="300" width="600" />
            <div class="info_container_top">
                <h2>Phylum</h2><p>{animals[0].phylum}</p>
                <h2>Class</h2><p>{animals[0].classification}</p>
                <h2>Order</h2><p>{animals[0].order}</p>
                <h2>Family</h2><p>{animals[0].family}</p>
                <h2>Genus</h2><p>{animals[0].genus}</p>
            </div>
            <div class="info_container_bottom">
                <h2>Avg Lifespan</h2><p>{animals[1].avg_lifespan}</p>
                <h2>Habitat</h2><p>{animals[1].habitat}</p>
                <h2>Geolocation</h2><p>{animals[1].geolocation}</p>
                <h2>Noise</h2><p>{animals[1].noise}</p>
            </div>
        <div>
                    '''
                p.update()
                p.whole_page = p.whole_page.format(**locals())
                self.response.write(p.print_out())
            elif animal == animals[1].name:
                p.form_results = '''
        <div class="info_container_whole">
            <img src="{animals[1].img_url}" height="300" width="600" />
            <div class="info_container_top">
                <h2>Phylum</h2><p>{animals[1].phylum}</p>
                <h2>Class</h2><p>{animals[1].classification}</p>
                <h2>Order</h2><p>{animals[1].order}</p>
                <h2>Family</h2><p>{animals[1].family}</p>
                <h2>Genus</h2><p>{animals[1].genus}</p>
            </div>
            <div class="info_container_bottom">
                <h2>Avg Lifespan</h2><p>{animals[1].avg_lifespan}</p>
                <h2>Habitat</h2><p>{animals[1].habitat}</p>
                <h2>Geolocation</h2><p>{animals[1].geolocation}</p>
                <h2>Noise</h2><p>{animals[1].noise}</p>
            </div>
        <div>
                    '''
                p.update()
                p.whole_page = p.whole_page.format(**locals())
                self.response.write(p.print_out())
            elif animal == animals[2].name:
                p.form_results = '''
        <div class="info_container_whole">
            <img src="{animals[2].img_url}" height="300" width="600" />
            <div class="info_container_top">
                <h2>Phylum</h2><p>{animals[2].phylum}</p>
                <h2>Class</h2><p>{animals[2].classification}</p>
                <h2>Order</h2><p>{animals[2].order}</p>
                <h2>Family</h2><p>{animals[2].family}</p>
                <h2>Genus</h2><p>{animals[2].genus}</p>
            </div>
            <div class="info_container_bottom">
                <h2>Avg Lifespan</h2><p>{animals[2].avg_lifespan}</p>
                <h2>Habitat</h2><p>{animals[2].habitat}</p>
                <h2>Geolocation</h2><p>{animals[2].geolocation}</p>
                <h2>Noise</h2><p>{animals[2].noise}</p>
            </div>
        <div>
                    '''
                p.update()
                p.whole_page = p.whole_page.format(**locals())
                self.response.write(p.print_out())



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

class Wolf(Mammals):
    def __init__(self):
        super(Wolf, self).__init__()

    def make_noise(self):
        self.noise = "Bark"

class Badger(Mammals):
    def __init__(self):
        super(Badger, self).__init__()

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
        <link rel="stylesheet" href="css/styles.css" type="text/css">
    </head>
    <body>
                    '''
        self._body = '''
        <header>HEADER</header>
        <h1>Welcome, click each button for a fun fact sheet about some of the world's favorite mammals!</h1>
        '''
        self._close = '''

    </body>
</html>
                    '''


    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, new_head):
        self._head = new_head
        self.update()

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, new_body):
        self._body = new_body
        self.update()

    @property
    def close(self):
        return self._close

    @close.setter
    def close(self, new_close):
        self._close = new_close
        self.update()

    def print_out(self):
        return self._head + self._body + self._close



class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        self.__form = '''
        <form method="GET">
            <input type="submit" name="animal" value="Gray Wolf">
            <br/>
            <input type="submit" name="animal" value="Honey Badger">
            <br/>
            <input type="submit" name="animal" value="Kangaroo">
        </form>
            '''

        self.__form_results = ""

        self.whole_page = ""

    def update(self):
        self.whole_page = self.form_results + self.close

    @property
    def form(self):
        return self.__form

    @form.setter
    def form(self, new_form):
        self.__form = new_form

    @property
    def form_results(self):
        return self.__form_results

    @form_results.setter
    def form_results(self, new_form_results):
        self.__form_results = new_form_results

    def print_out(self):
        return self.whole_page



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
