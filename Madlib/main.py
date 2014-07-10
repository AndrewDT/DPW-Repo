'''
Name: Andrew Tillett
Class: Design Patters for Web Programming 1407
Assignment: Madlib
Date: 7/7/14
'''


#DEFINITIONS (FUNCTIONS)-----------------------------------


#Function to convert the minutes variable into hours for the hours variable by passing the minutes variable as an argument
def calcHour(min):
    if min.isdigit():
        hour = float(min)/60
        return hour
    else:
        pass

#Function to calculate the result of 2 numbers passed as arguments and returned to the results variable
def calcResult(number1, number2):
    sum = int(number1) + int(number2)
    return sum

#Function to check a user's input and ensure they input a number and re-run while it is not
def numberCheck():
    number_var = raw_input("Please enter a number!  ")
    while number_var.isalpha() or number_var == "":
        print "\nSorry, has to be a number!"
        number_var = raw_input("Please enter a valid number!   ")
    else:
        return number_var

#Function to check a user's input and ensure they enter a string and re-run while it is not
def stringCheck():
    string_var = raw_input("Please enter a word!   ")
    while string_var.isdigit() or string_var == "":
        print "\nSorry, we need a word!"
        string_var = raw_input("Please enter only letters!   ")
    else:
        return string_var


#Printing a welcome message for players
print "------Welcome to MadLib! Here you will be given sections of a paragraph one at a time and fill in the blanks. Once complete, the entire story will appear!------"

#variable to contain the madlib
madlib = "\nA villain was attacking {location} around 3pm. In no time, he had caused a great deal of damage while terrorizing the citizens. Luckily, {hero} showed up in time to stop the madman! They fought and struggled for {minutes} minutes or about {hours} hours, but it was clear who the victor would be. As a reward, the hero was given a {reward} and the villain was given {years} years in prison!  Just as we know {number_one} plus {number_two} equals {result} and {obj} are delicious, we all know evil never {action}! \n"
#Printing madlib for players
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

#Conditional to run in case the player does not input one of the given choices
while response_location != locations[0] or response_location != locations[1] or response_location != locations[2]:
    #Once the player chooses one of the given options this code runs
    if response_location == locations[0] or response_location == locations[1] or response_location == locations[2]:
        #Variable to hold the response of input
        location = response_location
        #Variable to contain hero that corresponds to the key of the chosen location within the dictionary
        hero = heroes[location]
        #Breaking the while loop once correct option is chosen
        break
    #Re-printing the options for players to choose from, printing an error message, and requiring a new input to match conditional
    for l in locations:
        print l
    print "\nOOPS! Please choose from choices above"
    response_location = raw_input("Please enter the location from the list provided exactly as seen. (Hero is determined by choice)  ")

#Setting variable to use in "for" loop
i = 0
#"For" loop to run each function with variables to contain results for use in the madlib
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

#Formatting the variables within the madlib to match player input and printing out completed madlib with thank you message
madlib = madlib.format(**locals())
print madlib + "\nThanks for playing!!!"