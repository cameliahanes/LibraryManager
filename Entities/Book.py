'''
Created on 7 nov. 2016

@author: Camelia
'''

class Book(object):
    '''
    classdocs
    '''
    def __init__(self, id, title, description, author):
        '''
        Constructor
        '''
        self.rented = False
        self._id = id
        self._title = title
        self._description = description
        self._author = author
        self.__times_rented = 0
        self.__days_rented = 0
        
    def __repr__(self):
        """print book in a nice way"""
        return "Book #%id:\nTitle: %s\nDescription: %s\nAuthor: %s\n" %(self._id, self._title, self._description, self._author)
    
    def __eq__(self, other):
        """returns True if other is an instance of the class Book or of a subclass and False otherwise"""
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
        
    def getID(self):
        """getter of the id; returns the book id"""
        return self._id
    
    def setID(self, id):
        """setter for the book id; params: the new id"""
        self._id = id
        
    def getTitle(self):
        """getter for the book title"""
        return self._title
    
    def setTitle(self, title):
        """setter for the title; params: the new title"""
        self._title = title
        
    def getDescription(self):
        """getter for the description"""
        return self._description
    
    def setDescription(self, description):
        """setter for the book description has the new description as parameter"""
        self._description = description
        
    def getAuthor(self):
        """returns the name of the author"""
        return self._author
    
    def setAuthor(self, author):
        """setter for the book author"""
        self._author = author
    
    def SetRented(self, rented):
        self.rented = rented
        #where rented is a parameters with boolean values; 
    
    def returnRented(self):
        return self.rented
        
    def compareByTitle(self, a, b):
        if a.getTitle() < b.getTitle():
            return -1
        elif a.getTitle() > b.getTitle():
            return 1
        else:
            return 0
    
    @property
    def times_rented(self):
        return self.__times_rented
    @times_rented.setter 
    def times_rented(self, value):
        self.__times_rented = value
    
    @property
    def days_rented(self):
        return self.__days_rented
    @days_rented.setter
    def days_rented(self, value):
        self.__days_rented = value
        
    def __str__(self, *args, **kwargs):
        return "Book with id: {0}, title: {1}, description: {2}, author: {3}, rented {4} times and {5} days"\
            .format(self._id, self._title, self._description, self._author, self.times_rented, self.days_rented)

        