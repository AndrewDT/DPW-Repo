'''
Name: Andrew Tillett
Date: 7/16/14
Class: Design Patters for Web Programming Online 1407
Assignment: Encapsulated Calculator
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #creating a new instance of the Person class and assigning values to the instance's properties
        jake = Person()
        jake.name = "jake"
        jake.weight = 200
        jake.height = 72
        jake.age = 21
        jake.calc_bmr()

        #creating a new instance of the Person class and assigning values to the instance's properties
        hugh = Person()
        hugh.name = "hugh"
        hugh.weight = 245
        hugh.height = 68
        hugh.age = 39
        hugh.calc_bmr()

        #creating a new instance of the Person class and assigning values to the instance's properties
        matt = Person()
        matt.name = "matt"
        matt.weight = 190
        matt.height = 62
        matt.age = 25
        matt.calc_bmr()

        #creating a new instance of the Person class and assigning values to the instance's properties
        steve = Person()
        steve.name = "steve"
        steve.weight = 187
        steve.height = 68
        steve.age = 31
        steve.calc_bmr()

        #creating a new instance of the Person class and assigning values to the instance's properties
        tony = Person()
        tony.name = "tony"
        tony.weight = 175
        tony.height = 64
        tony.age = 42
        tony.calc_bmr()

        #creating a new instance of the Page class and then writing the full_page variable
        p = Page()
        self.response.write(p.full_page)


        #Conditional set to run if self.request.GET == true and then run nested code if met
        if self.request.GET:
            #creating a new instance of the Person class
            user = Person()
            #assigning the name property of the user object to equal the "person" key from the on page form
            user.name = self.request.GET["person"]
            #Conditional set to run if user.name is equal to jake.name
            if user.name == jake.name:
                #adding div and objects info into the body, which can then be changed according to button clicked for each person
                p.body = '''
            <div id="info_container">
                <h3>BMR & Measurements</h3>
                <p class="odd">Name: {jake.name}</p>
                <p class="even">Weight: {jake.weight} lbs</p>
                <p class="odd">Height: {jake.height} inches</p>
                <p class="even">Age: {jake.age} years old</p>
                <p class="odd">BMR: {jake.bmr} calories</p>
            </div>
                '''
                #formatting the local variables of the p.body property
                p.body = p.body.format(**locals())
                #writing the updated p.full_page to the html
                self.response.write(p.full_page)
            #Conditional set to run if user.name is equal to hugh.name
            elif user.name == hugh.name:
                #adding div and objects info into the body, which can then be changed according to button clicked for each person
                p.body = '''
            <div id="info_container">
                <h3>BMR & Measurements</h3>
                <p class="odd">Name: {hugh.name}</p>
                <p class="even">Weight: {hugh.weight} lbs</p>
                <p class="odd">Height: {hugh.height} inches</p>
                <p class="even">Age: {hugh.age} years old</p>
                <p class="odd">BMR: {hugh.bmr} calories</p>
            </div>
                '''
                #formatting the local variables of the p.body property
                p.body = p.body.format(**locals())
                #writing the updated p.full_age to the html
                self.response.write(p.full_page)
            #Conditional set to run if user.name is equal to matt.name
            elif user.name == matt.name:
                #adding div and objects info into the body, which can then be changed according to button clicked for each person
                p.body = '''
            <div id="info_container">
                <h3>BMR & Measurements</h3>
                <p class="odd">Name: {matt.name}</p>
                <p class="even">Weight: {matt.weight} lbs</p>
                <p class="odd">Height: {matt.height} inches</p>
                <p class="even">Age: {matt.age} years old</p>
                <p class="odd">BMR: {matt.bmr} calories</p>
            </div>
                '''
                #formatting the local variables of the p.body property
                p.body = p.body.format(**locals())
                #writing the updated p.full_age to the html
                self.response.write(p.full_page)
            #Conditional set to run if user.name is equal to steve.name
            elif user.name == steve.name:
                #adding div and objects info into the body, which can then be changed according to button clicked for each person
                p.body = '''
            <div id="info_container">
                <h3>BMR & Measurements</h3>
                <p class="odd">Name: {steve.name}</p>
                <p class="even">Weight: {steve.weight} lbs</p>
                <p class="odd">Height: {steve.height} inches</p>
                <p class="even">Age: {steve.age} years old</p>
                <p class="odd">BMR: {steve.bmr} calories</p>
            </div>
                '''
                #formatting the local variables of the p.body property
                p.body = p.body.format(**locals())
                #writing the updated p.full_age to the html
                self.response.write(p.full_page)
            #Conditional set to run if user.name is equal to tony.name
            elif user.name == tony.name:
                #adding div and objects info into the body, which can then be changed according to button clicked for each person
                p.body = '''
            <div id="info_container">
                <h3>BMR & Measurements</h3>
                <p class="odd">Name: {tony.name}</p>
                <p class="even">Weight: {tony.weight} lbs</p>
                <p class="odd">Height: {tony.height} inches</p>
                <p class="even">Age: {tony.age} years old</p>
                <p class="odd">BMR: {tony.bmr} calories</p>
            </div>
                '''
                #formatting the local variables of the p.body property
                p.body = p.body.format(**locals())
                #writing the updated p.full_age to the html
                self.response.write(p.full_page)


#Creating a Person class with properties and corresponding getters/setters
class Person(object):
    def __init__(self):
        #setting the self instance(each created instance's self) name property
        self.name = ""
        #setting the self instance(each created instance's self) weight property also set as a private variable
        self.__weight = 0
        #setting the self instance(each created instance's self) height property also set as a private variable
        self.__height = 0
        #setting the self instance(each created instance's self) age property also set as a private variable
        self.__age = 0
        #setting the self instance(each created instance's self) BMR property also set as a private variable
        self.__bmr = 0


    #creating the getter for self.__weight
    @property
    def weight(self):
        return self.__weight

    #creating the setter for self.__weight
    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    #creating the getter for self.__height
    @property
    def height(self):
        return self.__height

    #creating the setter for self.__height
    @height.setter
    def height(self, new_height):
        self.__height = new_height

    #creating the getter for self.__age
    @property
    def age(self):
        return self.__age

    #creating the setter for self.__age
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    #creating the getter for self.__bmr
    @property
    def bmr(self):
        return self.__bmr

    #creating the setter for self.__bmr
    @bmr.setter
    def bmr(self, new_bmr):
        self.__bmr = new_bmr

    #Calculates the person's bmr from the assigned property values
    def calc_bmr(self):
        self.__bmr = 66 + (6.23*self.weight) + (12.7*self.height) - (6.8*self.age)



#Creating a Page class with properties and corresponding getters/setters
class Page(object):
    def __init__(self):
        #variable to contain the page's beginning html. Set as a private variable
        self.__head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>BMR Calculator</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <body>

                    '''
        #variable to contain the page's initial body html. Set as a private variable
        self.__body = '''
        <header>
        <img src="images/logo.png">
        </header>
        <div id="welcome_container">
        <h1>Welcome, here we'll show you how to calculate Basil Metabolic Rate (BMR)
        <h2>Basal metabolic rate (BMR) is the rate of energy expenditure by humans at rest, and is measured in kJ per hour per kg body mass.<br/> The formula is: <br/>BMR = 66 + ( 6.23 x weight in pounds ) + ( 12.7 x height in inches ) - ( 6.8 x age in year ) for males<br/>BMR = 655 + ( 4.35 x weight in pounds ) + ( 4.7 x height in inches ) - ( 4.7 x age in years ) for females<br/>Here we are using the formula for males</h2>
        </div>
        <form method="GET">
            <input type="submit" name="person" value="jake" />
            <input type="submit" name="person" value="hugh" />
            <input type="submit" name="person" value="matt" />
            <input type="submit" name="person" value="steve" />
            <input type="submit" name="person" value="tony" />
        </form>
        '''

        #variable to contain the page's ending html. Set as a private variable
        self.__close = '''
    </body>
</html>
                    '''
        #setting a variable to initially hold the values of self.head + self.body to be written to page
        self.full_page = self.head + self.body

    #update function to update self.full_page when a new body is set and add self.close to page
    def update(self):
        self.full_page = self.body + self.close

    #creating the getter for self.__head
    @property
    def head(self):
        return self.__head

    #creating the setter for self.__head
    @head.setter
    def head(self, new_head):
        self.__head = new_head
        self.update()

    #creating the getter for self.__body
    @property
    def body(self):
        return self.__body

    #creating the setter for self.__body
    @body.setter
    def body(self, new_body):
        self.__body = new_body
        self.update()

    #creating the getter for self.__close
    @property
    def close(self):
        return self.__close

    #creating the setter for self.__close
    @close.setter
    def close(self, new_close):
        self.__close = new_close
        self.update()





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
