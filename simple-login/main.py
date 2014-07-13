'''
name - Andrew Tillett
date - 7/11/14
class - Design Patters for Web Programming Online 1407
assignment - Simple Login
'''

import webapp2 #Import Statement - says use the webapp2 library

#Declaring a class
class MainHandler(webapp2.RequestHandler):
    def get(self): #Function that starts everything. Initializing function (Catalyst)
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>

        '''
        page_body = '''<form method="GET">
            <label>Name: </label><input type="text" name="user"/>
            <label>E-Mail: </label><input type="text" name="email"/>
            <input type="submit" value="Submit" />
            '''


        page_close = '''
        </form>
    </body>
</html>
        '''
        #same as == True "Does this exist?"
        if self.request.GET:
            #MATCH NAME OF FORM ELEMENT FOR ASSOCIATIVE ARRAY
            #stores info we got from the form
            user = self.request.GET["user"]
            email = self.request.GET["email"]
            self.response.write(page_head + user + " " + email + page_close)

        else:
            self.response.write(page_head + page_body + page_close) #Printing our information out sent from server
        #For us to receive the info,


#LEAVE THIS ALONE (DON'T TOUCH)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

'''
Doing it with links instead of form tags
<a href="?email=mickey@disney.com&user=Mickey">Mickey</a><br/>
<a href="?email=minnie@disney.com&user=Donald"">Donald</a><br/>
<a>href="?email=donald@disney.com&user=Minnie"">Minnie</a><br/>
<a>href="?email=donald@disney.com&user=Pluto"">Pluto</a><br/>
'''