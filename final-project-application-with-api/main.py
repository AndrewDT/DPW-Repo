'''
Name: Andrew Tillett
Date: 7/28/14
Class: DPW Online 1407
Assignment: Final Project: Application with API

STILL NEED:
Create a proof of concept to make sure you have chosen something within scope
You MUST validate the user's input. Blank submissions cannot be acceptable.
Comment your code. Everything needs to be explained in detail.
'''
import webapp2
import urllib2 #gives us python classes and code needed to requesting info, receiving, and opening
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [["text", "title", "Title"], ["text", "authors", "Author(s)"], ["submit", "Search"]]

        if self.request.GET:
            bm = BookModel()
            bm.title = self.request.GET["title"]
            bm.author = self.request.GET["authors"]
            bm.callApi()

            bv = BookView()
            bv.bdos = bm.dos

            p._body = bv.content

        self.response.write(p.page_write())




class BookView(object):
    '''  This class handles how the data is shown to the user  '''
    def __init__(self):
        self.__bdos = []
        self.__content = "<br/>"


    def update(self):
        for do in self.__bdos:
            if do.web_read:
                self.__content += "<div class='book_container'>"
                self.__content += "<div class='title_container'><h2>Title</h2><p>"+do.title+"</p></div><div class='author_container'><h2>Author</h2><p>"+do.authors+"</p></div>"
                self.__content += "<div class='read_container'><h2>Read</h2><a href='"+do.web_read + "'>Read Online</a></div>"
                if do.rating:
                    self.__content += "<div class='rating_container'><h2>Rating</h2><p>"+str(do.rating) + "</p></div>"
                    self.__content += "</div>"
                else:
                    self.__content += "</div>"
            elif do.rating:
                self.__content += "<div class='book_container'>"
                self.__content += "<div class='title_container'><h2>Title</h2><p>"+do.title+"</p></div><div class='author_container'><h2>Author:</h2><p>"+do.authors + "</p></div>"
                self.__content += "<div class='rating_container'><h2>Rating</h2><p>"+str(do.rating) + "</p></div>"
                self.__content += "</div>"
            else:
                self.__content += "<div class='book_container'>"
                self.__content += "<div class='title_container'><h2>Title</h2><p>"+do.title+"</p></div><div class='author_container'><h2>Author</h2><p>"+do.authors + "</p></div>"
                self.__content += "</div>"



    @property
    def content(self):
        return self.__content

    @property
    def bdos(self):
        pass

    @bdos.setter
    def bdos(self, arr):
        self.__bdos = arr
        self.update()



class BookModel(object):
    ''' This model handles fetching, parsing, and sorting data from Yahoo's weather api '''
    def __init__(self):
        self.__url = "https://www.googleapis.com/books/v1/volumes?q='"
        self.__title = ""
        self.__author = ""
        self.__jsondoc = ""


    def callApi(self):
        request = urllib2.Request(self.__url+self.__title.replace(" ", "")+"'+inauthor:"+self.__author.replace(" ", "%20"))
        print self.__url+self.__title.replace(" ", "")+"'+inauthor:"+self.__author.replace(" ", "%20")
        opener = urllib2.build_opener()
        result = opener.open(request)
        self.__jsondoc = json.load(result)
        books = self.__jsondoc["items"]
        self._dos = []
        for item in books:
            do = BookData()
            try:
                do.title = item["volumeInfo"]["title"]
                do.authors = item["volumeInfo"]["authors"][0]
                do.rating = item["volumeInfo"]["averageRating"]
                do.web_read = item["accessInfo"]["webReaderLink"]
                print item["saleInfo"]
                self._dos.append(do)
            except:
                print item["saleInfo"]
                self._dos.append(do)


    @property
    def dos(self):
        return self._dos

    @property
    def title(self):
        pass

    @title.setter
    def title(self, t):
        self.__title = t


    @property
    def author(self):
        pass

    @author.setter
    def author(self, a):
        self.__author = a



class BookData(object):
    ''' this data object holds the data fetched by the model shown by the view  '''
    def __init__(self):
        self.title = ""
        self.authors = ""
        self.rating = ""
        self.web_read = ""





class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Book Search App</title>
        <link rel="stylesheet" type="text/css" href="css/style.css" />
    </head>
    <body>
        <div id="page_container">
        '''
        self._body = '''
        <div id="greeting_container">
            <h1>Welcome to Book Lib!</h1>
            <p>Using Google Books, we search the database and provide the following if applicable:</p>
            <ul>
                <li>Title</li>
                <li>Author</li>
                <li>Online Readable</li>
                <li>Rating</li>
            </ul>
        </div>
        '''
        self._close = '''
        </div>
    </body>
</html>
        '''

    def page_write(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        self._form_open = "<form method='GET'><h1>Search for Books</h1>"
        self._form_fields = ""
        self.__inputs = ""
        self._form_end = "</form>"

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, arr):
        for item in arr:
            self._form_fields += "<input type='" + item[0] + "' name='" + item[1]
            try:
                self._form_fields += "' placeholder='" + item[2] + "' />"
            except:
                self._form_fields += "' />"


    def page_write(self):
        return self._head + self._form_open + self._form_fields + self._form_end + self._body + self._close





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
