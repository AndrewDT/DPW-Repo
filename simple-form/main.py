'''
Name: Andrew Tillett
Date: 07/13/14
Class: Design Patters for Web Programming Online 1407
Assignment: Simple Form
'''



import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #variable containing the code for the !DOCTYPE through header set of tags for the page's html
        page_head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Movie Magic</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <body>
        <header>
            <img src="css/images/logo.png">
        </header>
                    '''

        #variable containing the code for the form, all inputs, and the form submit button
        page_body = '''
        <form id="movie_preference" method="GET">
            <h3>Please fill out our brief survey, <br/> for all movie lovers!</h3>
            <label>Name: <br/></label><input type="text" name="user" /> <br/>
            <label>What's your favorite movie? <br/></label><input type="text" name="movieFavorite" /> <br/>
            <label>What's your least favorite movie? <br/></label><input type="text" name="movieLeast" /> <br/>
            <label>How many movies do you watch weekly? <br/></label>
            <input type="checkbox" name="frequency"  value="2 or less a week" />2 or less a week
            <input type="checkbox" name="frequency" value="3-4 a week" />3-4 a week
            <input type="checkbox" name="frequency" value="5 or more a week" />5 or more a week <br/>
            <label>Please select your age group: <br/></label>
            <select required form="movie_preference" name="age">
                <option value="13 - 18">13 - 18</option>
                <option value="19 - 25">19 - 25</option>
                <option value="25+">25+</option>
            </select>
            <br/>
            <input id="submit" type="submit" value="Submit" />

                    '''

        #variable containing the code for the end of the form, body, entire footer, and ending html tag
        page_end = '''
        </form>
    </body>
    <footer>
    </footer>
</html>

                    '''
        #Conditional set if self.request.GET == true, then run nested code
        if self.request.GET:
            #variables containing each value corresponding to GET method name value
            user = self.request.GET["user"]
            movie_favorite = self.request.GET["movieFavorite"]
            movie_least = self.request.GET["movieLeast"]
            frequency = self.request.GET["frequency"]
            age = self.request.GET["age"]
            #variable containing the code for the page once each field has been filled and submitted
            page_receipt = '''
            <ul>
                <li><h2>Name:</h2> {user}</li>
                <li><h2>Favorite Movie:</h2> {movie_favorite}</li>
                <li><h2>Least Favorite Movie:</h2> {movie_least}</li>
                <li><h2>How Frequently You Watch Movies:</h2> {frequency}</li>
                <li><h2>My Age Group is:</h2> {age}</li>
            </ul>
                            '''
            #conditional for nested code to run once each of the form fields have been filled and submitted within parent conditional
            if user and movie_favorite and movie_least and frequency and age:
                #formatting the page_receipt variable's locals to match GET values
                page_receipt = page_receipt.format(**locals())
                #writing the html to the page from within each variable
                self.response.write(page_head + page_receipt + page_end)
        #conditional set to write basic page html with form if the above parent if statement condition is not met
        else:
            #writing the html to the page from within each variable
            self.response.write(page_head + page_body + page_end)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)