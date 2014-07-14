'''
Name: Andrew Tillett
Date: 07/13/14
Class: Design Patters for Web Programming Online 1407
Assignment: Simple Form


Create and deliver a form with Python. This form should submit info to a Python script and display the results for the user.

The purpose of the form is of your choosing but your form MUST meet the following requirements:

Collect at least 5 pieces of information from the user.
Use at least one text based input element CHECK
Use at least one checkbox input element CHECK
Use at least one select element CHECK
The form should use the GET method to deliver variables to the following page. The following page should list out the information entered (think of a receipt after an order) in an organized and visually pleasing way.

Design will be an important component of your grade, so do NOT focus purely on function. Your form should look polished, professional, and user friendly. Your design should fit the market (ideal user) of your application and it's overall purpose. For example, if you make a form to collect info for a pizza company, your design should reflect the market that would use this form.

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
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Movie Magic</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <body>
                    '''

        page_body = '''
        <form id="movie_preference" method="GET">
            <label>Name: </label><input type="text" name="user" /> <br/>
            <label>What's your favorite movie? </label><input type="text" name="movieFavorite" /> <br/>
            <label>What's your least favorite movie? </label><input type="text" name="movieLeast" /> <br/>
            <label>How many movies do you watch weekly? </label>
            <input type="checkbox" name="frequency"  value="2 or less a week" />2 or less a week
            <input type="checkbox" name="frequency" value="3-4 a week" />3-4 a week
            <input type="checkbox" name="frequency" value="5 or more a week" />5 or more a week <br/>
            <label>Please select your age group: </label>
            <select required form="movie_preference" name="age">
                <option value="13 - 18">13 - 18</option>
                <option value="19 - 25">19 - 25</option>
                <option value="25+">25+</option>
            </select>
            <br/>
            <input type="submit" value="Submit" />

                    '''

        page_end = '''
        </form>
    </body>
</html

                    '''
        if self.request.GET:
            user = self.request.GET["user"]
            movie_favorite = self.request.GET["movieFavorite"]
            movie_least = self.request.GET["movieLeast"]
            frequency = self.request.GET["frequency"]
            age = self.request.GET["age"]
            page_receipt = '''
            <ul>
                <li>{user}</li>
                <li>{movie_favorite}</li>
                <li>{frequency}</li>
                <li>{age}</li>
            </ul>
                            '''
                self.response.write(page_head + page_receipt + page_end)
        else:
            self.response.write(page_head + page_body + page_end)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)