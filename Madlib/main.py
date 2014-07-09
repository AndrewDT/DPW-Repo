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
Luckily, (STRING) showed up in time to stop the madman! They fought and struggled for ____ minutes or ____ hours, but it was clear who the victor would be.As a reward, the hero was given _____ _____ and the villain was given _____ years in prison! Although evil was vanquished, the hero still needed to make it to a meeting by 5pm! Considering it took him _____ to defeat the villain in total, and it will take at least 45 minutes to arrive, he (does or does not have enough time to make it!) It's rough being so heroic."

'''

print "------Welcome to MadLib! Here you will be given sections of a paragraph one at a time and fill in the blanks. Once complete, the entire story will appear!------"

#Madlib for viewers
madlib_part_one = "A villain was attacking the {location} around 3pm. In no time, he had caused a great deal of damage while terrorizing the citizens. Luckily, ____ showed up in time to stop the madman!"
#Printing Madlib for viewers
print madlib_part_one

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


while response_location != locations[0] or response_location != locations[1] or response_location != locations[2]:
    if response_location == locations[0] or response_location == locations[1] or response_location == locations[2]:
        #Variable to hold the response of input
        location = response_location
        #Filling in the blanks of the madlib variable
        madlib_part_one = madlib_part_one.format(**locals())
        #printing out the madlib with blank filled
        print madlib_part_one
        break
    for l in locations:
        print l
    print "OOPS! Please choose from choices above"
    response_location = raw_input("Please enter the location from the list provided exactly as seen. (Hero is determined by choice)  ")




