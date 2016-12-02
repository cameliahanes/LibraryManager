'''
Created on 12 nov. 2016

@author: Camelia
'''
from Entities.Book import Book
from Entities.Client import Client
from Entities.Rental import Rental
from Entities.Library import Library
from Entities.Exception import LibraryException
import pickle

class LibraryRepository(object):
    
    '''
    Class LibraryRepository has all the old and new states of the Library Repository
        Properties:
            _states = a list of all LibraryRepository objects, representing all the states the application has gone through
            _now = the index in the list where we are at a given moment; this way we can easily make a undo/redo operation
    
    '''


    def __init__(self, restore = True):
        '''
       Constructor: initialises the Repository with the saved one (if exists) or starts a fresh (empty) Library
        '''
        if restore:
            self.restoreLibrary()
        else:
            self.createFreshLibrary()

            
    def getNowIndex(self):
        '''
        Function to return the now index, described above
        returns an integer representing the pointer the the state of the application at a given time.
        '''
        return self._now

    def getLibrary(self):
        '''
        Function to return the actual state of the application
        returns a LibraryRepository object - which is the "now" state of the application
        '''
        return self._states[self.getNowIndex()]
    
    def getStateClone(self):
        '''
        Function to create a new LibraryRepository Object with the same values as the latest one.
        We basically create a new LibraryRepository and we alter it, and add it to the states list.
        returns the newState - a deepCopy LibraryRepository of the latest repository
        '''
        newState = Library()
        newState.deepCopy(self.getLibrary())
        return newState
    
    def addBook(self, book):
        '''
        Function to add a new Book
        parameter: book: the book we want to add
        '''
        newState = self.getStateClone()
        newState.addBook(book)
        self.createNewRepository(newState)
        
    def getBooksSize(self):
        '''
        Function to return the size of the actual book repository
        returns an integer representing the number of books in the library
        '''
        return self.getLibrary().getBooksSize()
    
    def removeBook(self, bookId):
        '''
        Function to remove a Book
        Raises exception if no book was found.
        parameter  bookId:
        raises TypeError if the given Book was not found in the Library
        '''
        newState = self.getStateClone()
        newState.removeBook(bookId)
        self.createNewRepo(newState)
    
    def updateTitle(self, bookId, newTitle):
        '''
        Function to update the Title of a book
        params 
            the book id and the new title that we want to update the book to
            raises type error if the book with the given id was not found        
        '''
        newState = self.getStateClone()
        newState.updateTitle(bookId, newTitle)
        self.createNewRepo(newState)
    
    def updateDescription(self, bookId, newDescr):
        '''
        Function to update the Title of a book
        params 
            the book id and the new description that we want to update the book to
            raises type error if the book with the given id was not found        
        '''
        newState = self.getStateClone()
        newState.updateDescription(bookId, newDescr)
        self.createNewRepo(newState)

    def updateAuthor(self, bookId, newAuthor):
        '''
        Function to update the Title of a book
        params 
            the book id and the new author that we want to update the book to
            raises type error if the book with the given id was not found        
        '''
        newState = self.getStateClone()
        newState.updateAuthor(bookId, newAuthor)
        self.createNewRepo(newState)
    
    def addClient(self, client):
        '''
        Function to add a new Client
        params client: the new client we want to add
        raises exception if the client's id already exists
        '''
        newState = self.getStateClone()
        newState.addClient(client)
        self.createNewRepository(newState)
    
    def removeClient(self, clientId):
        '''
        Function to remove a Client
        params clientId: the id of the client we want to remove
        '''
        newState = self.getStateClone()
        newState.removeClient(clientId)
        self.createNewRepository(newState)
    
    def updateClientId(self, clientId, newId):
        '''
        Function to update the Id of a client.
        params clientId and the new id
        raises TypeError if there is no client with the given id, or the newId already exist
        '''
        newState = self.getStateClone()
        newState.updateClientId(clientId, newId)
        self.createNewRepository(newState)
    
    def updateClientName(self, clientId, newName):
        '''
        Function to update the name of a client.
        params clientId and the new name
        raises TypeError if there is no client with the given id
        '''
        newState = self.getStateClone()
        newState.updateClientName(clientId, newName)
        self.createNewRepository(newState)
    
    def rentBook(self, rentalId, bookID, clientId, rentedDate, dueDate, returnedDate):
        newState = self.getStateClone()
        newState.rentBook(rentalId,  bookID, clientId, rentedDate, dueDate, returnedDate)
        self.createNewRepository(newState)

    def returnBook(self, bookID, clientId):
        newState = self.getStateClone()
        newState.returnBook(bookID, clientId)
        self.createNewRepository(newState)
    
    def getBooks(self):
        '''
        Function to list all the books at this moment in the Library
        '''
        return self.getLibrary().getBooks()

    def getClients(self):
        '''
        Function to list all the clients at this moment in the Library
        '''
        return self.getLibrary().getClients()

    def getRentals(self):
        '''
        Function to list all the loans  at this moment in the Library
        '''
        return self.getLibrary().getRentals()

    def forgetFuture(self):
        '''
        Function to delete all the states that are irrelevant from now on
        '''
        self._states = self._states[:self.getNowIndex() + 1]

    def createFuture(self, newRepo):
        '''
        Function to append the newRepository to the states list and to update the "now" pointer
        '''
        self._states.append(newRepo)
        self._now += 1

    def createNewRepository(self, newRepository):
        '''
        Function to create a new Repository based on the altered one
        params: newRepository - the altered repository (the one with the latest command made)
        '''
        self.forgetFuture()
        self.createFuture(newRepository)

    def undo(self):
        '''
        Function to handle the undo command, raises exception if there is nothing to be undone
        '''
        if self._now == 0:
            raise LibraryException("Already at earliest state!")
        else:
            self._now -= 1

    def redo(self):

        '''
        Function to handle the redo command, raises exception if there is nothing to be redone, when the now index is at the latest state
        '''
        if self._now == len(self._states) - 1:
            raise LibraryException("Already at newest state!")
        else:
            self._now += 1
    
    def createFreshLibrary(self):
        '''
        Function to create a fresh new Library
        '''
        self._states =  [Library()]
        self._now = 0
            
    def restoreLibrary(self):
        """
        this function restores the latest known library history
        """
        try:
            with open("repository/libraryHistory.bin", "rb") as f:
                latest= pickle.load(f)
                self._states = latest._states
                self._now = latest.now
        except IOError:
            self.createFreshLibrary()
                
    def saveLibraryHistory(self):
        """
        function to save all done operation in the libraryHisory.bin file\
        """
        try:
            with open("repository/libraryHistory.bin", "wb") as f:
                pickle.dump(self, f)
            return "Current state successfully saved!"
        except IOError:
            raise LibraryException("Current state couldn't be saved.")
    
    
