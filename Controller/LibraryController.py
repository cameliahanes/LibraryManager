'''
Created on 20 nov. 2016

@author: Camelia
'''
from Entities.Book import Book
from Entities.Client import Client
from Entities.Exception import LibraryException
from Entities.Library import Library
from Entities.Rental import Rental
from Repository import LibraryRepository
from datetime import date, timedelta
import operator
from _operator import itemgetter


class LibraryController:
    """the class library controller which id the bridge between the user interface and the repository
    
    properties: the repository, where the operations and the fields are stored
    
    """
    
    def __init__(self, repo):
        """the constructor
        it initialisez the controller with the repository
        """
        self._repo = repo  
        
    def addBook(self, book):
        """function of the controller to add a new book"""
        """the only parameter is the new book to be added to the library"""
        self._repo.addBook(book)
        
        
    def removeBook(self, bookId):
        """the function removes the book with the ID given as parameter"""
        """it raises type error if the book wasn't found in the library"""
        for book in [rental.getBookID() for rental in self._repo.getRentals()]:
            if book.getID() == bookId:
                raise LibraryException("Book is rented...")
        self._repo.removeBook(bookId)
        
    def updateTitle(self, bookId, newTitle):
        """
        function to update the title of a book;
        params: the book id and the new title for the book to be updated
        """
        self._repo.updateTitle(bookId, newTitle)
        
    def updateDescription(self, bookId, newDescription):
        """
        function to update the description of a book with id given
        params:
        the book id and the new description
        """
        self._repo.updateDescription(bookId, newDescription)
        
    def updateAuthor(self, bookId, newAuthor):
        """
        function to update the name of the author of a book
        params : the ook id and the new author
        """
        self._repo.updateAuthor(bookId, newAuthor)
        
    def addClient(self, client):
        """
        function to add a new client
        params: the client to be added
        """
        self._repo.addClient(client)
        
    def removeClient(self, clientId):
        """
        function to remove the client with the given id
        params:  the client id
        
        """
        for client in[rental.getClients() for rental in self._repo.getRentals()]:
            if client.getID() == clientId:
                raise LibraryException("Client has rented a book, return it and then remove the client...")
        self._repo.removeClient(clientId)
        
    def updateClientId(self, clientId, newId):
        """
        function to update a client's id
        parameters: the current id and the new id to be updated with
        raises error in two cases:
        if the new id already exists in the list of clients and if the current id doesn't exist, so there is no client to be updated
        """
        self._repo.updateClientId(clientId, newId)
        
    def updateClientName(self, clientId, newName):
        """
        function to update the name of an existing client
        params :  the id of the client and the new name
        it raises error if there is no client with the given id
        """
        self._repo.updateClientName(clientId, newName)

    def findClientzById(self, id):
        """searches for a client by a certain id"""
        cls = self._repo.getClients()
        for c in cls:
            if c.getID() == id:
                return c.__str__()
        raise LibraryException("Client not found.")

    def findClientByName(self, name):
        """searches for a client n the list by a given name
        returns a list with clients whose names match the requirements provided by the string
        """
        cls = self.getClients()
        lstClients = []
        for c in cls:
            if c.getName().lower == name.lower:
                lstClients.append(c)
                continue
            if name.lower() in c.getName().lower():
                lstClients.append(c)
                continue
        return lstClients
    
    def findBookById(self, id):
        """
        searches for a book with the given id
        """
        for b in self.getBooks():
            if b.getID() == id:
                return b
        raise LibraryException("The book with entered title couldn't be found.")
        
                
    def findBooksByTitle(self, name, description, author):
        """
        searches for books with a gien title
        returns a list with books with the title given
        """    
        bks = self.getBooks()
        lstBooks = []
        for b in bks:
            if  name != None and name.lower() in b.getTitle().lower():
                lstBooks.append(b)
                continue
            if description != None and description.lower() in b.getDescription().lower():
                lstBooks.append(b)
                continue
            if author != None and author.lower() in b.getAuthor().lower():
                lstBooks.append(b)
                continue
        return lstBooks    
        
    def getLibrary(self):
        """
        function to get all books and clients existing in the library at the moment
        """
        return self._repo.getLibrary()
    
    def getBooks(self):
        """
        function to get all the existing books in the library at the moment
        
        """
        return self._repo.getBooks()
    
    def getClients(self):
        """
        function to get all clients in the library
        """
        return self._repo.getClients()
    
    def getRentals(self):
        """
        functon to get all the rentals in the library
        """
        return self._repo.getRentals()
    
    def rentBook(self, rentalId,  bookID, clientId, rentedDate, dueDate, returnedDate):
        """
        this function implements the process of renting a book
        """
        return self._repo.rentBook(rentalId,  bookID, clientId, rentedDate, dueDate, returnedDate)
        
    def returnBook(self,  bookID, clientId):
        """
        this function implements the process of returning a book
        """
        return self._repo.returnBook( bookID, clientId)
    
    def undo(self):
        """
        function to implement the undo
        """
        self._repo.undo()
        
    def redo(self):
        """
        function to implement the redo
        """
        self._repo.redo()
     
    def recreate(self):
        '''
        Function to create a fresh new Library
        '''
        self._repo.createFreshLibrary()
   
   
    def rentedBooksDescOrder(self, daysRented, timesRented):
        """
        returns a list of books sorted in descending order by the number of days they were rented
        or by the times they were rented
        """
        bksSorted = self._repo.getBooks() 
        """the list of existing books"""
        
        #for book in bks:
         #   bksSorted.append(book)
        if daysRented != None:
           # print(sorted(bksSorted, key=lambda Book:Book.days_rented, reverse = True))
            return sorted(bksSorted, key=lambda Book:Book.days_rented, reverse = True)
        else:
            return sorted(bksSorted, key = lambda Book:Book.times_rented, reverse = True)
            
    def mostRentedAuthors(self):
        """
        returns a list of authors in descending order by the times theis bokr were rented
        """
        authorss = []
        
        rentals = self.getRentals()
        """all rentals from the library"""
        for r in rentals:
            bookId = r.getBookID()
            """we extract the book id and now we search for the author name"""
            bks = self.getBooks()
            """we search in the book list for the book id and catch the author"""
            for b in bks:
                if b.getID() == bookId: #if we found the id in the list then we return the autor to the program
                    auth = b.getAuthor()
                    """now we search for the autor to see if it already exists in the list, otherwise we add it"""
                    for i in authorss:
                        if i["author"] == auth:
                            i["times rented"] += 1
                            break
                        else:
                            aaa = {"author":auth, "times rented":0}
                            authorss.append(aaa)
        return authorss.sort("times rented", True)        
    
    def filterRentals(self, clientId, bookId):
        """
        returns a lit of rentals according to the required field
        """
        r = []
        rntls = self.getRentals()
        for ree in rntls:
            if clientId != None:
                if clientId == ree.getClientId():
                    r.append(ree)
                    continue
            if bookId != None:
                if bookId == ree.getBookID():
                    r.append(ree)
                    continue
        return r
    
    def filterRentals2(self, clientIDList, bookIDList, author):
        """functon to filter the rentals using client's id or book's id or
        the due date
        output: the list of all filtered rentals
        """
        l = []
        for r in self.getRentals():
            if clientIDList != None and r.getClientId() != clientIDList:
                continue
            if bookIDList != None and r.getBookID() not in bookIDList:
                continue
            if author != None:
                id = r.getBookID()
                for b in self.getBooks():
                    if b.getID() == id and author not in b.getAuthor():
                        continue
            l.append(r)
        return l
    
    def mostActiveClients(self):
        """function to return the list of clients in descending order of the number of books they have rented and
        the days
        """
        stat = []
        for c in self.getClients():
            rentals = self.filterRentals2(c.getID(), None, None)
            days = 0
            for r in rentals:
                if r.getReturnedDate() != None:
                    days += (r.getReturnedDate() - r.getRentedDate()).days()
            stat.append({"ID":c.getID(), "name":c.getName(), "days":days})
        return sorted(stat, key = itemgetter("days"), reverse = True)
    
    def mostRentedAuthors2(self):
        """
        function to return a list of authors with the numbers of rentals respectively in descending order
        """
        stat = []
        for b in self.getBooks():
            rentals = self.filterRentals2(None, None, b.getAuthor())
            rents = len(rentals)
            stat.append({"author":b.getAuthor(), "rents":rents})
        return sorted(stat, key=itemgetter("rents"), reverse = True)
    
    
    def overDueRentals(self):
        stat = []
        for r in self.getRentals():
            if r.getReturnedDate() == None:
                stat.append({"rentalID":r.getRentalID(), "overdue":(date.today()-r.getDueDate()).days()})
        return sorted(stat, key = itemgetter("overdue"), reverse = True)