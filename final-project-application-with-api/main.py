'''
Name: Andrew Tillett
Date: 7/28/14
Class: DPW Online 1407
Assignment: Final Project: Application with API

'''
import webapp2
import urllib2 #gives us python classes and code needed to requesting info, receiving, and opening
import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        p.inputs = [["text", "title", "Title"], ["text", "authors", "Author(s)"], ["submit", "Search"]]
        self.response.write(p.page_write())

        if self.request.GET:
            title = self.request.GET["title"]
            authors = self.request.GET["authors"]
            key = '&key=AIzaSyCf5csGwo5jceqciyjS0GIEyVSJcsJ4Wt4'
            url = "https://www.googleapis.com/books/v1/volumes?q='" + title.replace(" ", "") + "'+inauthor:" + authors.replace(" ", "") + key


            request = urllib2.Request(url)
            opener = urllib2.build_opener()
            result = opener.open(request)

            jsondoc = json.load(result)

            books = jsondoc["items"]
            print books

            for item in books:
                try:
                    book_title = item["volumeInfo"]["title"]
                    book_author = item["volumeInfo"]["authors"][0]
                    book_buy = item["saleInfo"]["buyLink"]
                    book_rating = item["volumeInfo"]["averageRating"]
                    self.response.write("<br/>Title:   " + book_title + "<br/>Author:   " + book_author + "<br/>Rating:   " + str(book_rating) + "<br/>" + book_buy)
                except:
                    self.response.write("<br/>Title:   " + book_title + "<br/>Author:   " + book_author)





class BookModel(object):
    ''' This model handles fetching, parsing, and sorting data from Yahoo's weather api '''
    def __init__(self):
        self.__url = "https://www.googleapis.com/books/v1/volumes?q='"
        self.__title = ""
        self.__author = ""
        self.__jsondoc = ""


    def callApi(self):
        request = urllib2.Request(url)
        opener = urllib2.build_opener()
        result = opener.open(request)
        self.__jsondoc = json.load(result)
        books = self.__jsondoc["items"]
        self._dos = []
        for item in books:
            do = BookData()
            do.title = books["volumeInfo"]["title"]
            do.authors = books["volumeInfo"]["authors"][0]
            do.rating = books["volumeInfo"]["averageRating"]
            do.buy = item["saleInfo"]["buyLink"]
            self._dos.append(do)



class BookData(object):
    ''' this data object holds the data fetched by the model shown by the view  '''
    def __init__(self):
        self.title = ""
        self.authors = ""
        self.rating = ""
        self.buy = ""





class Page(object):
    def __init__(self):
        self._head = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>Book Search App</title>
    </head>
    <body>
        '''
        self._body = "Book Searching Application"
        self._close = '''

    </body>
</html>
        '''

    def page_write(self):
        return self._head + self._body + self._close


class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()

        self._form_open = "<form method='GET'>"
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
