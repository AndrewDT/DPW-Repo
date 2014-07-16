'''
Name: Andrew Tillett
Date: 7/16/14
Class: Design Patters for Web Programming Online 1407
Assignment: Encapsulated Calculator


Find a purpose:

Like other projects in this class, you must create the situation for this type of web application. You are essentially listing out pieces of information from the same type of object and then using some of the data to calculate a 6th piece of information and displaying it all within the application. This is an exercise in creating and protecting certain pieces of data within an object, so try to find a purpose that reflects that (but NOT one listed here or used in class).

Your application must have the following requirements:

5 Data Objects (made from the same class) that will hold the data. These should be hard coded. No form or user input should be used for this assignment.
These data objects should be made from the same class. There should be a minimum of 5 attributes. This class MUST have properties set up for at least 2 of the attributes/variables in the class and there should be at least one example of a getter and one of a setter. (The setter must be there, even though it will not actually be used by the rest of the code.)
name
weight
height
age
bmr
BMR = 66 + ( 6.23 x weight in pounds ) + ( 12.7 x height in inches ) - ( 6.8 x age in year )

There should be a button (or link) for each item.
When a button is clicked, your application should show the data for the object that button represents and use some of the data in a calculation. The results for that calculation should appear in the app as well.
Here's an example:

A grade average calculator. It holds the grade data for 5 students (Leonardo, Michael Angelo, Raphael, Donatello and Splinter). The application holds a "view" where the data will be seen and five buttons, one for each student. When the button labeled "Raphael" is clicked, his grade data appears in the view and likewise for the other students. In addition to his grades his GPA (calculated from his grades) is shown as well.

Minimum requirements (Violating these garners an automatic 0):

Remember that, like other assignments in this class, your design skills and choices will be graded!
Comment your code. Everything needs to be explained in detail.
Don't forget to do 20 commits.
You may not use any Python frameworks for this assignment.
Global variables are not permitted.
Any errors will earn an automatic ZERO on this assignment.
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        jake = Person()
        jake.name = "Jake"
        jake.weight = 200
        jake.height = 72
        jake.age = 21
        jake.calc_bmr()
        self.response.write("Jake's BMR is " + str(jake.bmr) + " calories a day")

        hugh = Person()
        hugh.name = "Hugh"
        hugh.weight = 245
        hugh.height = 68
        hugh.age = 39
        hugh.calc_bmr()
        self.response.write("<br/>Hugh's BMR is " + str(hugh.bmr) + " calories a day")


        matt = Person()
        matt.name = "Matt"
        matt.weight = 190
        matt.height = 62
        matt.age = 25
        matt.calc_bmr()
        self.response.write("<br/>Matt's BMR is " + str(matt.bmr) + " calories a day")

        steve = Person()
        steve.name = "Steve"
        steve.weight = 187
        steve.height = 68
        steve.age = 31
        steve.calc_bmr()
        self.response.write("<br/>Steve's BMR is " + str(steve.bmr) + " calories a day")

        tony = Person()
        tony.name = "Tony"
        tony.weight = 175
        tony.height = 64
        tony.age = 42
        tony.calc_bmr()
        self.response.write("<br/>Tony's BMR is "  + str(tony.bmr) + " calories a day")

        #variable containing the code for the !DOCTYPE through header set of tags for the page's html
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Encapsulated Calculator</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <body>
        <header>
        </header>
                    '''

        #variable containing the code for the form, all inputs, and the form submit button
        page_body = '''


                    '''

        #variable containing the code for the end of the form, body, entire footer, and ending html tag
        page_end = '''
        </form>
    </body>
    <footer>
    </footer>
</html>
                    '''

class Person(object):
    def __init__(self):
        self.name = ""
        self.__weight = 0
        self.__height = 0
        self.__age = 0
        self.__bmr = 0


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def bmr(self):
        return self.__bmr

    @bmr.setter
    def bmr(self, new_bmr):
        pass

    def calc_bmr(self):
        self.__bmr = 66 + (6.23*self.weight) + (12.7*self.height) - (6.8*self.age)














app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
