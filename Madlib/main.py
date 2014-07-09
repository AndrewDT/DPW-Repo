'''
Name: Andrew Tillett
Class: Design Patters for Web Programming 1407
Assignment: Madlib
Date: 7/7/14

MadLib

Mad Libs is a comic word game where one player is prompted for a list of words to fill in the blanks of a story.

Create your own mad lib in Python that collects (at least) the following information:

HAS TO COLLECT
At least 3 strings
At least 3 numbers
And includes the following elements:

CAN COLLECT FROM
One array
One dictionary

At least 2 mathematical operators
Two conditional statements
(with at least one logical operator)
At least one function
It must return a value
It must have and use parameters
One loop - Remember that this is for repeating code!
And meet the following requirements:

The mad lib's code must be well commented and include the appropriate use of Docstrings
All elements should have a purpose within the greater madlib. (In other words you can't create an array or function that isn't used)
You must make at least 12 meaningful commits to this file in your repository or your assignment will earn a 0.
Any errors will earn an automatic ZERO on this assignment.
Your mad lib should print out the entire story using the "print" function

A villain was attacking the (STRING) around 4pm. In no time, he had caused insurmountable damage while terrorizing the citizens.
Luckily, (STRING) showed up in time to stop the madman! They fought and struggled for (NUMBER) minutes or (NUMBER) hours, but it was clear who the victor would be.
As a reward, the hero was given (NUMBER) (STRING) and the villain was given (NUMBER) years in prison! Although evil was vanquished, the hero still needed to make
it to a meeting by 5pm! Considering it took him (NUMBER) to defeat the villain in total, he (does or does not have enough time to make it!) It's rough being so heroic.

'''

#Madlib for viewers
madlib = "A villain was attacking the {location} around 3pm. In no time, he had caused insurmountable damage while terrorizing the citizens. Luckily, ____ showed up in time to stop the madman! They fought and struggled for ____ minutes or ____ hours, but it was clear who the victor would be.As a reward, the hero was given _____ _____ and the villain was given _____ years in prison! Although evil was vanquished, the hero still needed to make it to a meeting by 5pm! Considering it took him _____ to defeat the villain in total, and it will take at least 45 minutes to arrive, he (does or does not have enough time to make it!) It's rough being so heroic."

#Printing Madlib for viewers
print madlib

#Locations array for first blank choice
locations = ["- city", "- YMCA", "- PetSmart"]
#Printing locations for viewers to see and choose from
for l in locations:
    print l
#Input for viewers to choose first blank
response_location = raw_input("Please enter the location from the list provided. (Hero is determined by choice)  ")

location = response_location
madlib = madlib.format(**locals())
print madlib

#New dictionary declared
heroes = dict()
#Dictionary containing keys linking to hero to be filled into the blank
heroes = {locations[0]:"Batman",locations[1]:"Richard Simmons",locations[2]:"The Cashier"}




