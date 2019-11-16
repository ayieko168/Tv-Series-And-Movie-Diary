from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MainDesign import *
from dialogs.MessageBox import showMessage
import json, os

class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## MENUBAR CONNECTIONS
        self.ui.menuFile.triggered[QAction].connect(self.menuFileCMD)
        # self.ui.menuOptions.triggered[QAction].connect(self.menuOptionsCMD)
        # self.ui.menuView.triggered[QAction].connect(self.menuViewCMD)
        self.ui.menuCurent_Table.triggered[QAction].connect(self.menuCurent_TableCMD)
        self.ui.menuWatch_Sites.triggered[QAction].connect(self.menuWatch_SitesCMD)
        # self.ui.menuDownload_Sites.triggered[QAction].connect(self.menuDownload_SitesCMD)
        # self.ui.menuHelp.triggered[QAction].connect(self.menuHelpCMD)
        self.ui.addNewEntryButton.clicked.connect(self.addNewEntryButtonCMD)

        ## SETUP 
        self.setUpTables()
        self.initialDataPopulation()

    def menuFileCMD(self, q):
        command = q.text()

        if command == "Push My Data":
            print("push")

            self.push_data_base()
        
        elif command == "Pull My Data":
            print("pull")
        
        elif command == "Edit Sites":
            print("edit sites")
        
        elif command == "Exit":
            print("exit")

            self.close()
        
    def initialDataPopulation(self):
        DIR = os.getcwd()
        
        with open(f"{DIR}\\v2.0\\utils\\data_base.json") as data_baseFo:
            data_base = json.load(data_baseFo)

            ## Individual data Dictionaries
            self.currently_watching_Dict = data_base["currently_watching"]
            self.complete_tv_shows_Dict = data_base["complete_tv_shows"]
            self.shows_on_break_Dict = data_base["shows_on_break"]
            self.wish_list_Dict = data_base["wish_list"]
            self.seen_movies_Dict = data_base["seen_movies"]
            self.details_Dict = data_base["details"]
            self.watch_sites_Dict = data_base["watch_sites"]
            self.download_sites_Dict = data_base["download_sites"]
            self.search_dict = data_base["search_dict"]

        ## Populate the tables:
        # Clear all table rows
        self.ui.currentlyWatchingTable.setRowCount(0)
        self.ui.completedTvShowsTable.setRowCount(0)
        self.ui.onBreakTable.setRowCount(0)
        self.ui.wishListTable.setRowCount(0)
        self.ui.seenMoviesTable.setRowCount(0)

        # populate currently_watching table
        for k, v in sorted(self.currently_watching_Dict.items()):
            v.insert(0, k)
            self.addTableItem(self.ui.currentlyWatchingTable, v)
        
        # populate complete_tv_shows table
        for k, v in sorted(self.complete_tv_shows_Dict.items()):
            v.insert(0, k)
            self.addTableItem(self.ui.completedTvShowsTable, v)
        
        # populate shows_on_break table
        for k, v in sorted(self.shows_on_break_Dict.items()):
            v.insert(0, k)
            self.addTableItem(self.ui.onBreakTable, v)
        
        # populate wish_list table
        for k, v in sorted(self.wish_list_Dict.items()):
            v.insert(0, k)
            self.addTableItem(self.ui.wishListTable, v)
        
        # populate seen_movies table
        for k, v in sorted(self.seen_movies_Dict.items()):
            v.insert(0, k)
            self.addTableItem(self.ui.seenMoviesTable, v)
        
        ## POPULATE THE OPTIONAL MENU OPTIONS
        # Clear the menu options
        self.ui.menuWatch_Sites.clear()
        self.ui.menuDownload_Sites.clear()

        # populate the websites
        for k, v in sorted(self.watch_sites_Dict.items()):
            self.ui.menuWatch_Sites.addAction(k)
        
        for k, v in sorted(self.download_sites_Dict.items()):
            self.ui.menuDownload_Sites.addAction(k)

    def addTableItem(self, table, values=[]):
        """Add an item at the bottom of the list in 'table', value
           is a list of values of the row created.
           table is a QTablbeWidget object.
           """

        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        
        pos = 0
        for value in values:
            # print(f"add {value} at", pos)
            table.setItem(rowPosition, pos, QtGui.QTableWidgetItem(str(value)))
            pos+=1

    def addNewEntryButtonCMD(self):

        showMessage()
        
    def setUpTables(self):
        """set the basic pproperties of the tables"""

        header = self.ui.currentlyWatchingTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)

        header = self.ui.completedTvShowsTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.Stretch)

        header = self.ui.onBreakTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.Stretch)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)

        header = self.ui.wishListTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)

        header = self.ui.seenMoviesTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)

    def menuCurent_TableCMD(self, q):
        """swithch the current tab to a selection you make."""
        command = q.text()

        print(command)
        
        if command == "Currently Watching":
            print(f"switch tab to {command}")
            self.ui.stackedWidget.setCurrentIndex(0)
        
        elif command == "Complete Tv Shows":
            print(f"switch tab to {command}")
            self.ui.stackedWidget.setCurrentIndex(1)
        
        elif command == "Shows on Break":
            print(f"switch tab to {command}")
            self.ui.stackedWidget.setCurrentIndex(2)

        elif command == "Wish List":
            print(f"switch tab to {command}")
            self.ui.stackedWidget.setCurrentIndex(3)

        elif command == "Seen Movies":
            print(f"switch tab to {command}")
            self.ui.stackedWidget.setCurrentIndex(4)

        elif command == "Search Results Tab":
            print(f"switch tab to {command}")
            self.ui.stackedWidget.setCurrentIndex(5)

    def push_data_base(self):

        print("prepairing to push your data...")

        print("done.")





if __name__ == "__main__":

    w = QApplication([])
    app = App()
    app.show()
    w.exec_()


