'''
Created on 7 nov. 2016

@author: Camelia
'''

class Client(object):
    '''
    classdocs
    '''
    def __init__(self, id, name):
        '''
        Constructor
        '''
        self._id = id
        self._name = name
        self._daysRented = 0
        
    def __repr__(self):
        """print the client in a nice way"""
        return "Client name: %s\nID: %s "%(self._name, self._id)
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)  and self.__dict__ == other.__dict__)
    
    def getDaysRented(self):
        return self._daysRented
    
    def setDaysRented(self, daysR):
        self._daysRented= daysR
    
    def getID(self):
        return self._id
    
    def setID(self, id):
        self._id = id
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
    def get_days_rented(self):
        return self.__days_rented

    def days_rented(self, value):
        self.__days_rented = value
    '''
    Function to overload print.
    '''
    def __str__(self, *args, **kwargs):
        return "Client with id: {0} and name: {1} with a total of {2} days rented.".format(self._id, self._name, self.days_rented)