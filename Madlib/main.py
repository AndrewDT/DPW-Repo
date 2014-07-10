'''
Name: Andrew Tillett
Class: Design Patters for Web Programming 1407
Assignment: Madlib
Date: 7/7/14

MadLib

Mad Libs is a comic word game where one player is prompted for a list of words to fill in the blanks of a story.

Create your own mad lib in Python that collects (at least) the following information:

HAS TO COLLECT
At least 3 strings CHECK
At least 3 numbers CHECK
And includes the following elements:

CAN COLLECT FROM
One array CHECK
One dictionary CHECK

At least 2 mathematical operators CHECK
Two conditional statements CHECK
(with at least one logical operator) CHECK

At least one function CHECK
It must return a value CHECK
It must have and use parameters CHECK

One loop - Remember that this is for repeating code!
And meet the following requirements:

The mad lib's code must be well commented and include the appropriate use of Docstrings
All elements should have a purpose within the greater madlib. (In other words you can't create an array or function that isn't used)
You must make at least 12 meaningful commits to this file in your repository or your assignment will earn a 0.
Any errors will earn an automatic ZERO on this assignment.
Your mad lib should print out the entire story using the "print" function
'''


#DEFINITIONS (FUNCTIONS)-----------------------------------
def calcHour(min):
    if min.isdigit():
        hour = float(min)/60
        return hour
    else:
        pass


def calcResult(number1, number2):
    result = int(number1) + int(number2)
    return result
    print result

def numberCheck():
    number_var = raw_input("Please enter a number!  ")
    while number_var.isalpha() or number_var == "":
        print "\nSorry, has to be a number!"
        number_var = raw_input("Please enter a valid number!   ")
    else:
        return number_var


def stringCheck():
    string_var = raw_input("Please enter a word!   ")
    while string_var.isdigit() or string_var == "":
        print "\nSorry, we need a word!"
        string_var = raw_input("Please enter only letters!   ")
    else:
        return string_var



print "------Welcome to MadLib! Here you will be given sections of a paragraph one at a time and fill in the blanks. Once complete, the entire story will appear!------"

#Madlib for viewers
madlib = "\nA villain was attacking {location} around 3pm. In no time, he had caused a great deal of damage while terrorizing the citizens. Luckily, {hero} showed up in time to stop the madman! They fought and struggled for {minutes} minutes or about {hours} hours, but it was clear who the victor would be. As a reward, the hero was given a {reward} and the villain was given {years} years in prison!  Just as we know {number_one} plus {number_two} equals {result} and {obj} are delicious, we all know evil never {action}! \n"
#Printing Madlib for viewers
print madlib

#Locations array for first blank choice
locations = ["Gotham", "YMCA", "PetSmart"]
#Printing locations for viewers to see and choose from
for l in locations:
    print l
#Input for viewers to choose first blank
response_location = raw_input("Please enter the location from the list provided exactly as seen. (Hero is determined by choice)  ")

#New dictionary declared
heroes = dict()
#Dictionary containing keys linking to hero to be filled into the blank
heroes = {locations[0]:"Batman",locations[1]:"Richard Simmons",locations[2]:"The Cashier"}
hero = ""

while response_location != locations[0] or response_location != locations[1] or response_location != locations[2]:
    if response_location == locations[0] or response_location == locations[1] or response_location == locations[2]:
        #Variable to hold the response of input
        location = response_location
        hero = heroes[location]
        break
    for l in locations:
        print l
    print "\nOOPS! Please choose from choices above"
    response_location = raw_input("Please enter the location from the list provided exactly as seen. (Hero is determined by choice)  ")

i = 0
for i in range(0, 1):
    minutes = numberCheck()
    hours = calcHour(minutes)
    reward = stringCheck()
    years = numberCheck()
    number_one = numberCheck()
    number_two = numberCheck()
    result = calcResult(number_one, number_two)
    obj = stringCheck()
    action = stringCheck()

madlib = madlib.format(**locals())
print madlib + "\nThanks for playing!!!"