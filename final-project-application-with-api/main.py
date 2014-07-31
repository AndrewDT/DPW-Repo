'''
Name: Andrew Tillett
Date: 7/28/14
Class: DPW Online 1407
Assignment: Final Project: Application with API
'''
import webapp2
import urllib2 #gives us python classes and code needed to requesting info, receiving, and opening
import json

#Controller
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Instantiation of FormPage sub-class
        p = FormPage()
        #Setting the value of the inputs property to allow creation of form inputs
        p.inputs = [["text", "title", "Title"], ["text", "authors", "Author(s)"], ["submit", "Search"]]

        #Conditional set to run if self.request.GET == true and run nested code
        if self.request.GET:
            #Insantiation of BookModel class
            bm = BookModel()
            #Setting the value of the title property to the title input's result
            bm.title = self.request.GET["title"]
            #Setting the value of the author property to the author input's result
            bm.author = self.request.GET["authors"]
            #Conditional to run if self.request.GET is an empty string and run error message code if true, else continue as should
            if self.request.GET["title"] == "" or self.request.GET["authors"] == "":
                #Replacing the body property to contain an error message for empty fields
                p._body = "<h1 id='error_message'>Title and/or Author cannot be empty<br/>Please enter both fields</h1>"
            else:
                #Calling the callApi function of BookModel instance
                bm.callApi()
                #Instantiation of BookView class
                bv = BookView()
                #Setting the value of bdos to equal the dos(data objects) from BookModel class
                bv.bdos = bm.dos
                #Replacing the body property to contain information from the result of the Api call within content property
                p._body = bv.content

        #Writing the html tp the page using th page_write() function
        self.response.write(p.page_write())



#View
class BookView(object):
    '''  This class handles how the data is shown to the user  '''
    def __init__(self):
        #Property to contain an array of "Book Data Objects"
        self.__bdos = []
        #Property to contain the values from the "Data Objects" and the html
        self.__content = "<br/>"

    #Function to add the html with the "Data Object" values to the content property
    def update(self):
        #Loop to run through do "Data Objects" in bdos "Book Data Objects"
        for do in self.__bdos:
            #Conditional set to run if a web_read value is found
            if do.web_read:
                #Adding book_container div to content property
                self.__content += "<div class='book_container'>"
                #Adding title_container div/content and author_container div/content to content property
                self.__content += "<div class='title_container'><h2>Title</h2><p>"+do.title+"</p></div><div class='author_container'><h2>Author</h2><p>"+do.authors+"</p></div>"
                #Adding read_container div/content to content property
                self.__content += "<div class='read_container'><h2>Read</h2><a href='"+do.web_read + "'>Read Online</a></div>"
                #Conditional set to run if above conditional is true and rating value if found
                if do.rating:
                    #Adding rating_container div/content to content property
                    self.__content += "<div class='rating_container'><h2>Rating</h2><p>"+str(do.rating) + "</p></div>"
                    #Adding closing div of book_container to content property
                    self.__content += "</div>"
                else:
                    #Adding closing div of book_container to content property
                    self.__content += "</div>"
            #Conditional set to run if above conditional is false and rating value is found
            elif do.rating:
                #Adding book_container div to content property
                self.__content += "<div class='book_container'>"
                #Adding title_container div/content and author_container div/content to content property
                self.__content += "<div class='title_container'><h2>Title</h2><p>"+do.title+"</p></div><div class='author_container'><h2>Author:</h2><p>"+do.authors + "</p></div>"
                #Adding rating_container div/content to content property
                self.__content += "<div class='rating_container'><h2>Rating</h2><p>"+str(do.rating) + "</p></div>"
                #Adding closing div of book_container to content property
                self.__content += "</div>"
            else:
                #Adding the book_container div to content property
                self.__content += "<div class='book_container'>"
                #Adding title_container div/content and author_container div/content to content property
                self.__content += "<div class='title_container'><h2>Title</h2><p>"+do.title+"</p></div><div class='author_container'><h2>Author</h2><p>"+do.authors + "</p></div>"
                #Adding closing div of book_container to content property
                self.__content += "</div>"


    #Setting the getter of self.__content
    @property
    def content(self):
        #returning self.__content
        return self.__content

    #Setting the getter of self.__bdos
    @property
    def bdos(self):
        pass

    #Setting the setter of self.__bdos
    @bdos.setter
    def bdos(self, arr):
        #Setting the value of self.__bdos to arr
        self.__bdos = arr
        #Running the self.update() function
        self.update()


#Model
class BookModel(object):
    ''' This model handles fetching, parsing, and sorting data from Yahoo's weather api '''
    def __init__(self):
        #Property to contain the basic URL for the API
        self.__url = "https://www.googleapis.com/books/v1/volumes?q='"
        #Property to contain title information from input
        self.__title = ""
        #Property to contain author information from input
        self.__author = ""
        #Property to contain jsondoc information
        self.__jsondoc = ""

    #Function to contact the API, gather information, create do "Data Object", and append them to dos "Data Objects" property
    def callApi(self):
        #Assembling API request
        request = urllib2.Request(self.__url+self.__title.replace(" ", "")+"'+inauthor:"+self.__author.replace(" ", "%20"))
        #Creating an object to get the URL
        opener = urllib2.build_opener()
        #Getting a result from the API - requesting
        result = opener.open(request)
        #Using JSON to load result
        self.__jsondoc = json.load(result)
        #Variable to contain json call to "items" form API call
        books = self.__jsondoc["items"]
        #dos "Data Objects" property to contain do "Data Object" being passed from below for loop
        self._dos = []
        #For loop to run through each item "Data Object - do" in the books "Data Objects - dos" variable
        for item in books:
            #Instantiation of BookData()
            do = BookData()
            #Try and find and set below properties and then append do to dos
            try:
                #Setting the title property to the title value within the API object
                do.title = item["volumeInfo"]["title"]
                #Setting the author property to the authors value within the API object
                do.authors = item["volumeInfo"]["authors"][0]
                #Setting the rating property to the averageRating value within the API object
                do.rating = item["volumeInfo"]["averageRating"]
                #Setting the web_read property to the webReaderLink value within the API object
                do.web_read = item["accessInfo"]["webReaderLink"]
                #Adding the do to the dos property array
                self._dos.append(do)
            except:
                #Adding the do to the dos property array
                self._dos.append(do)

    #Setting the getter for self._dos
    @property
    def dos(self):
        #Returning self._dos
        return self._dos

    #Setting the getter for self.__title
    @property
    def title(self):
        pass

    #Setting the setter for self.__title
    @title.setter
    def title(self, t):
        #Setting the value of self.__title to t
        self.__title = t

    #Setting the getter for self.__author
    @property
    def author(self):
        pass

    #Setting the setter for self.__author
    @author.setter
    def author(self, a):
        #Setting the value of self.__author to a
        self.__author = a



class BookData(object):
    ''' this data object holds the data fetched by the model shown by the view  '''
    def __init__(self):
        #Property to contain title from API "Data Objects" in other class
        self.title = ""
        #Property to contain authors from API "Data Objects" in other class
        self.authors = ""
        #Property to contain rating from API "Data Objects" in other class
        self.rating = ""
        #Property to contain web_read from API "Data Objects" in other class
        self.web_read = ""




#Abstract Class
class Page(object):
    def __init__(self):
        #Property to contain head html for page
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Book Search App</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
    </head>
    <body>
        <img src='images/logo_final.png'' />
        <div id="page_container">
        '''
        #Property to contain body html for page
        self._body = '''
        <div id="greeting_container">
            <h1>Welcome to Book Lib!</h1>
            <p>Using Google Books, we search the database and provide the following if available:</p>
            <ul>
                <li>Title</li>
                <li>Author</li>
                <li>Online Readable</li>
                <li>Rating</li>
            </ul>
        </div>
        '''
        #Property to contain closing html for page
        self._close = '''
        </div>
    </body>
</html>
        '''

    #Function for writing above properties to page for page html
    def page_write(self):
        #Returning above properties for complete page html
        return self._head + self._body + self._close


#Sub-class of Page Abstract Class
class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        #Property to contain opening form tag for html
        self._form_open = "<form method='GET'><h1>Search for Books</h1>"
        #Property to contain form fields for html
        self._form_fields = ""
        #Property to contain form inputs for html
        self.__inputs = ""
        #Property to contain closing form tag for html
        self._form_end = "</form>"

    #Setting the getter for inputs
    @property
    def inputs(self):
        #Returning self.__inputs
        return self.__inputs

    #Setting the setter for inputs
    @inputs.setter
    def inputs(self, arr):
        #Loop to run through each item in arr
        for item in arr:
            #Adding input with incoming arguments to complete form input
            self._form_fields += "<input type='" + item[0] + "' name='" + item[1]
            #Trying to add input with incoming arguments to complete form input for third item
            try:
                self._form_fields += "' placeholder='" + item[2] + "' />"
            except:
                #Adding input with incoming arguments to complete form input if try is false
                self._form_fields += "' />"

    #POLYMORPHISM - Overriding page_write function from Page Abstract class, function for writing page html with form to page
    def page_write(self):
        #Returning properties for page html with form to write to page
        return self._head + self._form_open + self._form_fields + self._form_end + self._body + self._close





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
