'''
Name: Andrew Tillett
Date: 7/22/14
Class: DPW - Online 1407
Assignment: What Does the Fox Say
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #array of sub-class instances
        animals = [Wolf(), Badger(), Kangaroo()]

        #Instance of FormPage sub-class
        p = FormPage()
        #Assigning whole_page the value of p.head + p.body + p.form to create page html
        p.whole_page = p.head + p.body + p.form
        #writing page html
        self.response.write(p.whole_page)

        #setting each property of the Wolf() instance
        animals[0].name = "Gray Wolf"
        animals[0].phylum = "Chordata"
        animals[0].classification = "Mammalia"
        animals[0].order = "Carnivora"
        animals[0].family = "Canidae"
        animals[0].genus = "Canis"
        animals[0].avg_lifespan = "7 years"
        animals[0].img_url = "images/wolf_pack.jpg"
        animals[0].habitat = "Arctic Tundra, Forests, Mountains"
        animals[0].geolocation = "North America, Europe, Asia, India"
        animals[0].make_noise()

        #setting each property of the Badger() instance
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

        #setting each property of the Kangaroo() instance
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

        #function that takes the argument of the corresponding animal instance and create the html value in p.form, updates the page, formats the page locals, and writes to page the result
        def print_results(anim_obj):
                #setting the new value for p.form_results
                p.form_results = '''
        <div class="info_container_whole">
            <img src="{anim_obj.img_url}" height="300" width="610" />
            <div class="info_container_top">
                <h2>Phylum</h2><p>{anim_obj.phylum}</p>
                <h2>Class</h2><p>{anim_obj.classification}</p>
                <h2>Order</h2><p>{anim_obj.order}</p>
                <h2>Family</h2><p>{anim_obj.family}</p>
                <h2>Genus</h2><p>{anim_obj.genus}</p>
            </div>
            <div class="info_container_bottom">
                <h2>Avg Lifespan</h2><p>{anim_obj.avg_lifespan}</p>
                <h2>Habitat</h2><p>{anim_obj.habitat}</p>
                <h2>Geolocation</h2><p>{anim_obj.geolocation}</p>
                <h2>Noise</h2><p>{anim_obj.noise}</p>
            </div>
        <div>
                    '''
                #running the p.update() function
                p.update()
                #formatting the whole_page locals
                p.whole_page = p.whole_page.format(**locals())
                #writing out the page from the p.print_out method
                self.response.write(p.print_out())

        #conditional set to run nested code if self.request.GET == true
        if self.request.GET:
            #creating a variable to hold the value of self.request.GET
            animal = self.request.GET["animal"]
            #conditional set to run nested code if animal == to animals[0].name (Gray Wolf)
            if animal == animals[0].name:
                #calling the print_results function and passing the Wolf object as a parameter
                print_results(animals[0])
            #conditional set to run nested code if animal == to animals[1].name (Honey Badger)
            elif animal == animals[1].name:
                #calling the print_results function and passing the Badger object as a parameter
                print_results(animals[1])
            #conditional set to run nested code if animal == to animals[2].name (Kangaroo)
            elif animal == animals[2].name:
                #calling the print_results function and passing the Kangaroo object as a parameter
                print_results(animals[2])


#creation  of Mammals Abstract class
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

#creation of Wolf sub-class
class Wolf(Mammals):
    def __init__(self):
        super(Wolf, self).__init__()

    #polymorphism overriding the Mammals make_noise method
    def make_noise(self):
        #setting the value of the sub-class' noise to appropriate value
        self.noise = "Bark"

#creation of Badger sub-class
class Badger(Mammals):
    def __init__(self):
        super(Badger, self).__init__()

    #polymorphism overriding the Mammals make_noise method
    def make_noise(self):
        #setting the value of the sub-class' noise to appropriate value
        self.noise = "Squeal"

#creation of Kangaroo sub-class
class Kangaroo(Mammals):
    def __init__(self):
        super(Kangaroo, self).__init__()

    #polymorphism overriding the Mammals make_noise method
    def make_noise(self):
        #setting the value of the sub-class' noise to appropriate value
        self.noise = "Grunt"

#creation of Page Abstract class
class Page(object):
    def __init__(self):
        #property to contain the head of the page html (private)
        self.__head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Mammal Fact Sheet</title>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
    </head>
    <body>
                    '''
        #property to contain the body of the page html (private)
        self.__body = '''
        <header><img src="images/logo.png"></header>
        <h1>Welcome, click each button for a fun fact sheet about some of the world's favorite mammals!</h1>
        '''
        #property to contain the close of the page html (private)
        self.__close = '''

    </body>
</html>
                    '''

    #head getter
    @property
    def head(self):
        #returning self._head
        return self.__head

    #head setter
    @head.setter
    def head(self, new_head):
        #setting the value of self._head to new_head if changed
        self.__head = new_head

    #body getter
    @property
    def body(self):
        #returning self._body
        return self.__body

    #body setter
    @body.setter
    def body(self, new_body):
        #setting the value of self._body to new_body if changed
        self.__body = new_body

    #close getter
    @property
    def close(self):
        #returning self._close
        return self.__close

    #close setter
    @close.setter
    def close(self, new_close):
        #setting the value of self._close to new_close if changed
        self.__close = new_close

    #method to return the combined value of self._head self._body and self._close
    def print_out(self):
        return self.__head + self.__body + self.__close


#creation of FormPage sub-class
class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        #property to contain the form code for the html (private)
        self.__form = '''
        <form method="GET">
            <input type="submit" name="animal" value="Gray Wolf">
            <br/>
            <input type="submit" name="animal" value="Honey Badger">
            <br/>
            <input type="submit" name="animal" value="Kangaroo">
        </form>
            '''

        #property to contain the form result code for the html (private)
        self.__form_results = ""

        #property to contain the whole page's html
        self.whole_page = ""

    #method to update the whole page's html
    def update(self):
        #setting whole_page's value to self.form_results + self.close
        self.whole_page = self.form_results + self.close

    #form getter
    @property
    def form(self):
        #returning self.__form
        return self.__form

    #form setter
    @form.setter
    def form(self, new_form):
        #setting self.__form to the value of new_form
        self.__form = new_form

    #form getter
    @property
    def form_results(self):
        #returning self.__form_results
        return self.__form_results

    #form setter
    @form_results.setter
    def form_results(self, new_form_results):
        #setting the value of __form_results to new_form_results
        self.__form_results = new_form_results

    #polymorphism - overriding the Page Abstract class' print_out method and returning self.whole_page
    def print_out(self):
        #returning self.whole_page
        return self.whole_page



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
