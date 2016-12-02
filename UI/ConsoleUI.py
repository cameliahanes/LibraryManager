'''
Created on 25 nov. 2016

@author: Camelia
'''
from Controller.LibraryController import LibraryController
from Entities.Exception import LibraryException
from bz2 import __author__
from Entities.Book import Book
from Entities.Client import Client
from datetime import date
from datetime import timedelta

__author__ = "Camelia"

class LibraryApplication():
    def __init__(self, controller):
        self._controller = controller
        
    def displayMainMenu(self):
        s = ""
        s += "1 - Work with books\n"
        s += "2 - Work with clients\n"
        s += "3 - Work with rentals\n"
        s += "4 - Undo last change in the library\n"
        s += "5 - Redo lase changes\n"
        s += "x - Exit menu\n"
        print (s)
        
    def displayBooksMenu(self):
        s = ""
        s += "1 - Add a new book to the library \n"
        s += "2 - Remove a book from the library \n"
        s += "3 - Update characteristics for books \n"
        s += "4 - Most rented books \n"
        s += "5 - Search for a book \n"
        s += "6 - Get the list of most rented authors \n"
        s += "x - Exit BookMenu \n"
        print(s)
    
    def searchForBookMenu(self):
        s = ""
        s += "Search by ID \n"
        s += "Search by title \n"
        s += "Search by author's name \n"
        s += "Search by description \n"
        s += "x - Exit search menu \n"
        print(s)
    
    def displayUpdateBooksMenu(self):
        s = ""
        s += "1 - Update book Id \n"
        s += "2 - Update book title \n"
        s += "3 - Update book author \n"
        s += "4 - Update Book description \n"
        s += "x - Exit updating menu \n"
        print(s)
    
    def booksMenu(self):
        """menu for handling the books options"""
        bookCommands=["1", "2", "3", "4", "5", "6", "x"]
        command = input("Enter option: ")
        if command not in bookCommands:
            print("Unknown option.")
        else:
            try:
                if command == "1":
                    id = int(input("Give book id: "))
                    title = input("Give book title: ")
                    description = input("Give book description: ")
                    author = input("Give book's author: ")
                    book = Book(id, title, description, author)
                    self._controller.addBook(book)
                elif command == "2":
                    id = int(input("Give book's id: "))
                    self._controller.removeBook(id)
                elif command == "3":
                    self.displayUpdateBooksMenu()
                    option = input("Enter option: ")
                    if option == "x":
                        return
                    elif option == "1":
                        title = input("Give the new title: ")
                        self._controller.updateTitle(id, title)
                    elif option == "2":
                        desc = input("Enter the new description: ")
                        self._controller.updateDescription(id, desc)
                    elif option == "3":
                        author = input("Enter the name of the new author: ")
                        self._controller.updateAuthor(id, author)
                    else:
                        print("Unrecognised option...")
                elif command == "4":
                    op = input("Press: T for displaying by the times rented / D for displaying by the days of rental periods, (x - for exiting books menu): ")
                    if op == "x":
                        return
                    if op == "T":
                        bks = self._controller.rentedBooksDescOrder(None, True)
                        for b in bks:
                            print(b.__str__(), "\n")
                    elif op == "D":
                        bks = self._controller.rentedBooksDescOrder(True, None)
                        for b in bks:
                            print(b.__str__(), "\n")
                    
                    else:
                        print("Unknown command...")
                elif command == "5":
                    self.searchForBookMenu()
                    o = input("Press key: ")
                    if o == "x":
                        return
                    if o == "1":
                        try:
                            id = int(input("Enter id: "))
                            book = self._controller.findBookById(id)
                            print(book.__str__())
                        except ValueError:
                            print("Id must be an integer...")
                    elif o == "2":
                        title = input("Enter title: ")
                        books = self._controller.findBooksByTitle(title, None, None)
                        for b in books:
                            print(b.__str__(), "\n")
                    elif o == "3":
                        d = input("Enter description: ")
                        books = self._controller.findBooksByTitle( None,desc, None)
                        for b in books:
                            print(b.__str__(), "\n")
                    elif o == "4":
                        a = input("Enter author's name: ")
                        books = self._controller.findBooksByTitle(None, None, a)
                        for b in books:
                            print(b.__str__(), "\n")
                elif command == "6":
                    auth = self._controller.mostRentedAuthors2()
                    for a in auth:
                        print("Author "+str(a["author"])+" has "+str(a["rents"])+" total rentals.")
            except LibraryException as le:
                print(str(le))
            except ValueError as ve:
                print("Entry requests integer type.")
        
    def displayClientsMenu(self):
        s = ""
        s += "1 - Add client \n"
        s += "2 - Remove client \n"
        s += "3 - Update client's Name \n"
        s += "4 - Search for a client \n"
        s += "5 - Get most active clients \n"
        s += "x - Exit clients menu \n"
        print(s)
        
    def clientsMenu(self):
        commands = ["1", "2", "3", "4", "5", "x"]
        cmd = input("Enter your option: ")
        try:
            if cmd not in commands:
                print("Unknown command...")
            elif cmd == "x":
                return
            elif cmd == "1":
                try:
                    id = int(input("Enter the client's id: "))
                    name = input("Enter client's name: ")
                    cl = Client(id, name)
                    self._controller.addClient(cl)
                except ValueError:
                    print("Id must be an integer...")
            elif cmd == "2":
                try:
                    id = int("Enter the id of the client to be removed: ")
                    self._controller.removeClient(id)
                except ValueError:
                    print("Id must be an integer...")
            elif cmd == "3":
                try:
                    id = int(input("Enter client's id: "))
                    newName = input("Enter the new name for this client: ")
                    self._controller.updateClientName(id, newName)
                except ValueError:
                    print("Id must be integer...")
            elif cmd == "4":
                command = input("Press 1 for searching by ID and 2 for searching by Name \n")
                if command == "1":
                    try:
                        id = int("Give ID: ")
                        print(self._controller.findClientzById(id))
                    except ValueError:
                        print("Id must be integer...")
                elif command == "2":
                    name = input("Enter client's name: ")
                    clients = self._controller.findClientByName(name)
                    for c in clients:
                        print(c.__str__())
                else:
                    print("Unrecognised option...")
            elif cmd == "5":
                clients = self._controller.mostActiveClients()
                for c in clients:
                    print("Client with ID: "+str(c["ID"])+" and NAME: "+str(c["name"]) + " has " + str(c["days"]) +" days of total rentals.")
        except LibraryException as le:
            print(str(le))    
            
    def displayRentalsMenu(self):
        s = ""
        s += "1 - Display all rentals \n"
        s += "2 - Late rentals \n"
        s += "3 - Rent book \n"
        s += "4 - Return book \n"
        s += "x - Exit rentals menu \n"
        print(s)
    
    def rentalsMenu(self):
        command = input("Choose option: ")
        if command == "1":
            rents = self._controller.getRentals()
            for r in rents:
                print(r.__str__())
        elif command == "2":
            od = self._controller.overDueRentals()
            for o in od:
                print("Rental with id "+ str(o["rentalID"])+" has "+str(o["overdue"])+" days delay.")
        elif command == "3":
            try:
                rid = int(input("Enter the rental ID:"))
                id = int(input("Give the book id: "))
                clID = int(input("Give client's id: "))
                rentedDate = date.today()
                dueDate = (date.today() + timedelta(days=14)) #.isoformat()
                returnedDate = False
                self._controller.rentBook(rid, id, clID, rentedDate, dueDate, returnedDate)
                #rnts += 1
            except ValueError:
                print("ID must be integer...")
            except LibraryException as le:
                print(str(le))
        elif command == "4":
            try:
                bookid = int(input("Enter book's ID: "))
                clientID = int(input("Enter client's ID: "))
                self._controller.returnBook(bookid, clientID)    
            except LibraryException as le:
                print(str(le))
        elif command == "x":
            return
        else:
            print("Unknown command ...")
        
    def run(self):
        availableCommands = ["1", "2", "3", "4", "5", "x"]
        
        while True:
            self.displayMainMenu()
            command = input("Enter your option: ").strip()
            if command not in availableCommands:
                print("Invalid command")
            elif command == "x":
                return
            elif command == "1":
                self.displayBooksMenu()
                self.booksMenu()
            elif command == "2":
                self.displayClientsMenu()
                self.clientsMenu()
            elif command == "3":
                self.displayRentalsMenu()
                self.rentalsMenu()
            elif command == "4":
                self._controller.undo()
            elif command == "5":
                self._controller.redo()
            elif command == "x":
                return
            else:
                print("Unknown command...")