#one lined comments
'''
Doc strings
'''


first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter Your Name   ")
#print "Hello there,", response

birth_year = 1992
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old"

#Assignment Operators JS (++ --) Python does not have these
#Python (+=, -=, *=, /+)

'''
budget = 51

if budget > 100:
    brand = "Nike"
    print "Yay! we can buy cool " + brand + " shoes!"
elif budget > 50:
    print "We can at least get some generic sneakers."
else:
    print "No cool shoes for me."

'''

#ARRAY----------------------
characters = ["leia", "luke", "chewy", "lando"]
characters.append("obi wan")
#print characters

#DICTIONARY----------------------------
movies = dict() #Create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]

#Loops and Functions

'''
#While Loop------
i = 0
while i<9:
    #print "The count is", i
    i = i+1

#For Loop------
for i in range(0,10):
    print "The count is", i
    i = i+1

#"FOR EACH" LOOP ------------
rappers = ["Tupac", "Nas", "Biggie Smalls"]
for r in rappers:
    print "One of the best rappers is " + r
'''

#FUNCTIONS IN PYTHON -------------------------
#def means DEFINITION

x = 2

def calcArea(h, w):
    area = h * w
    return area + x

a = calcArea(20, 40)
#print "My area is " + str(a) + "sqft"
#print a


title = "Contact Us"
body = "You can contact us at contact@us.com"
message = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
# **locals() method replaces brackets {variable} with corresponding value
message = message.format(**locals())
print message















