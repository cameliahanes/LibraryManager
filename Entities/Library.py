'''
Created on 12 nov. 2016

@author: Camelia
'''
from Entities.Book import Book
from Entities.Client import Client
from Entities.Exception import LibraryException
from Entities.Rental import Rental
from datetime import date

class Library():
    '''
    it represents the library state at a given moment
    Parameters: 
    books = [] - the list of all books at the given moment
    clients = [] -the list of all clients at the given moment
    rentals = [] - the list of all rentals
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._clients = []
        self._books = []
        self._rentals = []
        
        
    def __repr__(self):
        return '\n\n'.join(str(book) for book in self._books) + "\n\n" + '\n\n'.join(str(client) for client in self._clients) + "\n\n"  + '\n\n'.join(str(loan) for loan in self._loans)
  
    def addBook(self, book):
        """
        funtion to add a new book to the list;
        params: book - the new entry
        """            
        self._books.append(book)
        
    def removeBook(self, id):
        """
        funtion to remove a book from the bookliss
        parameters : the book id
        raises LibraryException if the book was not found in the list
        """
        for i in range(0, len(self._books)):
            if self._books[i].getID() == id:
                del self._books[id]
                return
        raise LibraryException("Book not found.")
    
    def removeRentalByBookId(self, bookId):
        """
        function to remove an existing rental by book id
        raises LibraryException if book wasn't found
        parameters: bookId
        """
        
        for i in range(0, len(self._rentals)):
            rental = self._rentals[i]
            if rental.getBookID() == bookId:
                del self._rentals[i]
                return
        raise LibraryException("Book not found.")
    
    def findRentalByBookID(self, bookID):
        """
        function to find an existing rental by the book id
        :param : the id of the book
        """
        for i in range(0, len(self._rentals)):
            rental = self._rentals[i]
            if rental.getBookID() == bookID:
                return rental
        raise LibraryException("Book with ID: {0} doesn't exist or it is not rented.".format(bookID))
    
    def updateTitle(self,bookId, newTitle):
        """
        function to update the title of the book with id above given
        Parameters: the bookId and the new title
        Raises LibraryError if book wasn't found
        """
        for i in range(0, len(self._books)):
            if self._books[i].getID() == bookId:
                self._books[i].setTitle(newTitle)
                return
        raise LibraryException("Book not found.")
    
    def updateAuthor(self, bookId, newAuthor):
        """
        function to update the author of the book with id above given
        Parameters: the bookId and the new author
        Raises LibraryError if book wasn't found
        """
        for i in range(0, len(self._books)):
            if self._books[i].getID() == bookId:
                self._books[i].setAuthor(newAuthor)
                return
        raise LibraryException("Book not found.")
        
    def updateDescription(self, bookId, newDesc):
        """
        function to update the description of the book with id above given
        Parameters: the bookId and the new description
        Raises LibraryError if book wasn't found
        """
        for i in range(0, len(self._books)):
            if self._books[i].getID() == bookId:
                self._books[i].setDescription(newDesc)
                return
        raise LibraryException("Book not found.")
            
    def searchBook(self, bookId):
        '''
        Function to search for a book in the list
        params:  bookId: the id of the book we want to search for
        returns the unique given book (since the id is unique)
        raises LibraryError Exception if the book was not found in the book list
        '''
        for i in range(len(self._books)):
            book = self._books[i]
            if book.getID() == bookId:
                return book
        raise LibraryException("Book not found!")    
        
    def getBooks(self):
        """
        getter for the list of books in the library
        """    
        return self._books

    def getBooksSize(self):
        """
        returns the length of the book array
        """
        return len(self._books)
    
    def searchClient(self, clientId):
        '''
        Function to search for a client by his unique id
        params: clientId: an integer representing the id of the client we want to search for
        returns the unique Client (since the id is unique)
        raises TypeError if there is no client with the given id
        '''
        for i in range(len(self._clients)):
            client = self._clients[i]
            if client.getID() == clientId:
                return client
        raise LibraryException("Client not found!")

    def addClient(self, client):
        """
        function to add a new client to the array of clients
        params: the new client
        raises error if the client with the id already exists in the array
        """
        try:
            self.searchClient(client.getID())
            raise ValueError("Client with ID given already exists.")
        except LibraryException:
            self._clients.append(client)
            
    def updateClientName(self, clientId, newName):
        """
        function to update the name of the client with the id above given
        params: the id of the client and the new name
        raises LibraryException if the client doesn't exist in the list
        """
        for i in range(0, len(self._clients)):
            if self._clients[i].getID() == clientId:
                self._clients[i].setName(newName)
                return
        raise LibraryException("Client not found.")
    
    def updateClientId(self, clientId, newClientId):
        """"
        function to update the client's with id above given id
        raises valueerror if the new id is already existing in the list
        params: the actual and the new id
        """
        try:
            self.searchClient(clientId)
            raise ValueError("Client id already existing.")
        except LibraryException:
            for client in self._clients:
                if client.getID() == clientId:
                    client.setID(newClientId)
                    return
            raise LibraryException("Client not found.")
        
    def removeClient(self, clientId):
        '''
        Function to remove a Client
        params clientId: the new client we want to remove
        raises exception if the client doesn't exist in the list
        '''
        for i in range(len(self._clients)):
            client = self._clients[i]
            if client.getId() == clientId:
                del self._clients[i]
                return
        raise LibraryException("Client not found!")
        
    def getClients(self):
        '''
        Getter for the _clients list
        returns the _clients list from the main class
        '''
        return self._clients
    
    def getRentals(self):
        """
        getter for the rentals
        returns the list of all rentals
        """
        return self._rentals

    def deepCopy(self, other):
        '''
        Function to deepCopy another LibraryRepository to this (self) one
        ;copies all the data from another Repository to this one with no references of the objects (so that the states do not depend at all)
        params: other: another LibraryRepository
        '''
        self._books = [Book(book.getID(), book.getTitle(), book.getDescription(), book.getAuthor()) for book in other.getBooks()]
        self._clients = [Client(client.getID(), client.getName()) for client in other.getClients()]
        self._rentals = [Rental(rental.getRentalID(), rental.getBookID(), rental.getClientId(), rental.getRentedDate(),rental.getDueDate(), rental.getReturnedDate()) for rental in other.getRentals()]

    def rentBook(self, rentalId, clientId, bookID, rentedDate, dueDate, returnedDate):
        """
        book to return a book
        parameters:
        """
        clt = self.searchClient(clientId)
        bk = self.searchBook(bookID)
        if bk in [rental.getBook() for rental in self.getRentals()]:
            raise LibraryException("Book already rented to somebody!")
        
        for r in self.getRentals():
            if r.getRentalID() == rentalId:
                raise LibraryException("Already existing rental ID, choose another.")
        
        self._rentals.append(Rental( rentalId, bookID, clientId, rentedDate, dueDate, False))
        
    def returnBook(self, clientId, bookID):
        client = self.searchClient(clientId)
        book = self.searchBook(bookID)
        
        for r in self.getRentals():
            if r.getBookID() == bookID and r.getClientId() == clientId:
                r.setReturnedDate(date.today())
                return
        raise LibraryException("Unrecognised rental.")
        
        """
        if not bookID in [rental.getBookID() for rental in self.getRentals()]:
            raise LibraryException("Book is not rented, how could you return it? Maybe a donation?")
        #self.removeRentalByBookId(bookID)    
        else:
            rental.setReturnedDate(date.today())
        """
    def sort_by_rents(self):
        sortedv = []
        for b in self.getBooks():
            sortedv.append({"id": b.book_id, "times_rented": b.times_rented})
    #    sortedv = sorted(sortedv, key=itemgetter("times_rented"), reverse=True)
        list_for_return = []
        for b in range(0, len(sortedv)):
            list_for_return.append(self.find_by_id(sortedv[b]["id"]))
        return list_for_return

       





        
        