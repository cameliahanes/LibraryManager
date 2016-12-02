'''
Created on 27 nov. 2016

@author: Camelia
'''
import atexit
from Repository.LibraryRepository import LibraryRepository
from Entities.Exception import LibraryException
from Controller.LibraryController import LibraryController
from UI.ConsoleUI import LibraryApplication

if __name__ == '__main__':
    repo = LibraryRepository()
    controller = LibraryController(repo)
#atexit.register(repo.saveLibraryHistory())
    app = LibraryApplication(controller)
    app.run()
    