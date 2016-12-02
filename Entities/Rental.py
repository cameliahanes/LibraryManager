'''
Created on 7 nov. 2016

@author: Camelia
'''
from datetime import date
from datetime import datetime
from datetime import timedelta

class Rental(object):
    '''
    classdocs
    '''

    def __init__(self, rentalID, bookID, clientID, rentedDate, dueDate, returnedDate):
        '''
        Constructor
        '''
        self.__rentalID = rentalID
        self.__bookID = bookID
        self.__clientID = clientID
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = False
        self.__overdue = 0
        
    def __repr__(self):
        """print rental in a nice way"""
        return "Rental #%d: Client with #%d ID has the book with #%d ID.\n Rented date is %s \nDue date is %s \nReturned date is "%(self.__rentalID, self.__bookID, self.__clientID, self.__rentedDate, self.__dueDate, self.__returnedDate)
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
    
    def getClientId(self):
        return self.__clientID
    
    def getBookID(self):
        return self.__bookID
    
    def getRentalID(self):
        return self.__rentalID
    
    def getRentedDate(self):
        return self.__rentedDate
    
    def getDueDate(self):
        return self.__dueDate
    
    def getReturnedDate(self):
        return self.__returnedDate
    
    def setReturnedDate(self, returnedDate):
        self.__returnedDate = returnedDate
    
    def get_overdue(self):
        return self.__overdue

    def overdue(self, value):
        self.__overdue = value
    
    def __str__(self, *args, **kwargs):
        if self.__returnedDate == False:
            today = date(date.today().year, date.today().month, date.today().day)
            #today = datetime.today()
           
            someday = date(self.__dueDate.year, self.__dueDate.month, self.__dueDate.day)
            diff = (today - someday).days           
            self.__overdue = diff
            """if the book is not returned then we print the overdue once with book properties"""
            return "Rental ID: {0}, book ID: {1}, client ID: {2}, rented date: {3}, due date: {4}, overdue: {5}".format(\
                                            self.__rentalID, self.__bookID, self.__clientID, self.__rentedDate, self.__dueDate, self.__overdue)
            