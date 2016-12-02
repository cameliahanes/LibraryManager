'''
Created on 12 nov. 2016

@author: Camelia
'''
import unittest
from Entities.Book import Book
from Entities.Client import Client
from Entities.Rental import Rental
from Entities.Library import Library
from Entities.Exception import LibraryException


class UnitTester(unittest.TestCase):
    """
    class to implement tests for the entire application
    """
    def testBook(self):
        book = Book(1, "Introduction to algorithms", "The Bible", "Thomas H Cormen")
        assert book.getID()== 1
        assert book.getTitle() == "Introduction to algorithms"
        assert book.getDescription() == "The Bible"
        assert book.getAuthor() == "Thomas H Cormen"
        book.setAuthor("Cami")
        assert book.getAuthor() == "Cami"
        book.setDescription("BestOfAll")
        assert book.getDescription() == "BestOfAll"
        book.setTitle("titl")
        assert book.getTitle() == "titl"
        
    def testClient(self):
        client = Client(2971019052536, "Hanes Camelia-Andreea")
        assert client.getID() == 2971019052536
        assert client.getName() == "Hanes Camelia-Andreea"
        client.setID(1971019052536)
        client.setName("Hanes Andrei")
        assert client.getName() == "Hanes Andrei"
        assert client.getID() == 1971019052536
        
    
    
    
u = UnitTester()
u.testBook()    
u.testClient()