from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MainDesign import *
from dialogs.MessageBox import showMessage
from dialogs import cridentialsDialog
from dialogs import wishListDialog
from dialogs import addNewTitleDialog
from dialogs import websitesEditDialog
from utils import checker
import webbrowser
import json, os, time
from github import Github

data_base = {}

class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## MENUBAR CONNECTIONS
        self.ui.menuFile.triggered[QAction].connect(self.menuFileCMD)
        self.ui.menuOptions.triggered[QAction].connect(self.menuOptionsCMD)
        self.ui.menuView.triggered[QAction].connect(self.menuViewCMD)
        self.ui.menuCurent_Table.triggered[QAction].connect(self.menuCurent_TableCMD)
        self.ui.menuWatch_Sites.triggered[QAction].connect(self.menuWatch_SitesCMD)
        self.ui.menuDownload_Sites.triggered[QAction].connect(self.menuDownload_SitesCMD)
        self.ui.menuHelp.triggered[QAction].connect(self.menuHelpCMD)
        self.ui.addNewEntryButton.clicked.connect(self.addNewEntryButtonCMD)

        ## SETUP 
        self.setUpTables()
        self.initialDataPopulation()

        ## VARIABLES
        self.selected_watch_Site = ""
        self.selected_download_Site = ""

    def menuViewCMD(self, q):
        selection = q.text()

        print(f"{selection} option selection in the view menu")

    def menuOptionsCMD(self, q):
        selection = q.text()

        print(f"{selection} option selection in the options menu")

        if selection == "Update List":
            self.initialDataPopulation()
        
        elif selection == "Login":
            
            ## GET CREDENTIALS
            crid = LoginDialogClass()
            crid.run()
            user, _pass, ocup = crid.getCridentials()

        
            if (_pass != "") and (user != ""):

                ## Sign In to Github..
                print("sign in to github")
                self.signInGithub(user, _pass)

        elif selection == "Logout option":
            
            showMessage()

        elif selection == "Create Account":

             webbrowser.open_new_tab('https://github.com/join')

        elif selection == "Add To Wish List":

            wishDi = wishDialoClass()
            wishDi.run()
            title = wishDi.getTitle()
            print(f"add {title} to the wish list")
        
        elif selection == "Add New Title":

            addObj = addTitleDialogClass()
            addObj.run()
            print(addObj.getData())

    def menuHelpCMD(self, q):
        selection = q.text()
        print(f"open {selection} help dialog")

    def menuDownload_SitesCMD(self, q):

        # INIT
        selection = q.text()
        self.selectionLogic(selection)

        self.selected_download_Site = self.download_sites_Dict[selection][0]
        print("selected_download_Site set to  = ", self.selected_download_Site)
        
    def menuWatch_SitesCMD(self, q):
        
        # INIT
        selection = q.text()
        self.selectionLogic(selection)

        self.selected_watch_Site = self.watch_sites_Dict[selection][0]
        print("selected_watch_Site set to  = ", self.selected_watch_Site)
        
    def menuFileCMD(self, q):
        command = q.text()

        if command == "Push My Data":
            print("push")

            print("prepairing to push your data...")
            print("done.")
        
        elif command == "Pull My Data":
            print("pull")
        
        elif command == "Edit Sites":
            print("edit sites")

            webEd = websitesEditDialogClass()
            webEd.run()
            watch, download = webEd.getData()

            data_base = getDataBase()
            data_base["watch_sites"] = watch
            data_base["download_sites"] = download

            writeDataBase(data_base)
            
            self.initialDataPopulation()

        elif command == "Exit":
            print("exit")

            self.close()
        
    def initialDataPopulation(self):
        """Populate the tables with the databased found. Also
           Populate the menubar with the optional menus i.e:
           the watch sites and download sites. This also sets
           the default selected site option.
           """
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
        STATE = True
        for k, v in sorted(self.watch_sites_Dict.items()):
            actionOb = self.ui.menuWatch_Sites.addAction(k)
            actionOb.setCheckable(True)
            actionOb.setChecked(STATE)
            STATE = False
        
        STATE = True
        for k, v in sorted(self.download_sites_Dict.items()):
            actionOb = self.ui.menuDownload_Sites.addAction(k)
            actionOb.setCheckable(True)
            actionOb.setChecked(STATE)
            STATE = False

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

        self.selectionLogic()
        
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

    def selectionLogic(self, selection):
        """Set all other menu options not selected to False
           when one of the menu options are set. This only
           applie to Qaction objects that are set to checkable."""

        for actn in self.ui.menuWatch_Sites.actions():
            if actn.text() != selection:
                actn.setChecked(False)

    def signInGithub(self, user, passw):

        print(f"sign in using {user}, {passw}")

        g = Github(user, passw)

        

class LoginDialogClass(QDialog):

    def __init__(self):

        super().__init__()
        self.crUi = cridentialsDialog.Ui_Dialog()
        self.crUi.setupUi(self)
        
        self.crUi.showButtonCri.clicked.connect(self.showPass)
        self.crUi.doneButtonCri.clicked.connect(self.doneCMD)

        data_base = getDataBase()
        u = data_base["details"]["use"]
        p = checker.decoder(data_base["details"]["pas"])
        st = data_base["details"]["occupied"]

        if st == "True":
            self.crUi.userNameEntryCri.setText(u)
            self.crUi.passwordEntryCri.setText(p)

    def showPass(self):

        print("show pass")
        if self.crUi.passwordEntryCri.echoMode():  # if normal...
            self.crUi.passwordEntryCri.setEchoMode(QtGui.QLineEdit.Normal)
            self.crUi.showButtonCri.setText("hide")
        else:
            self.crUi.passwordEntryCri.setEchoMode(QtGui.QLineEdit.Password)
            self.crUi.showButtonCri.setText("show")

    def getCridentials(self):

        credentials = []

        u = self.crUi.userNameEntryCri.text()
        p = self.crUi.passwordEntryCri.text()
        rem = self.crUi.rememberMeCheckCri.isChecked()
        credentials.append(u)
        credentials.append(p)
        credentials.append(rem)
        credentials = tuple(credentials)

        return credentials
    
    def run(self):

        self.show()
        self.exec_()

    def doneCMD(self):

        self.getCridentials()
        if (self.crUi.userNameEntryCri.text() == "") or (self.crUi.passwordEntryCri.text() == ""):
            showMessage()
        else:
            self.close()


class wishDialoClass(QDialog):

    def __init__(self):

        super().__init__()
        self.wishUi = wishListDialog.Ui_Form()
        self.wishUi.setupUi(self)

        self.wishUi.addButton.clicked.connect(self.addButtonCMD)

    def addButtonCMD(self):

        self.getTitle()
        self.close()

    def run(self):

        self.show()
        self.exec_()

    def getTitle(self):

        return str(self.wishUi.titleEntry.text()).title()


class addTitleDialogClass(QDialog):

    def __init__(self):

        super().__init__()
        self.addUi = addNewTitleDialog.Ui_Dialog()
        self.addUi.setupUi(self)

        self.addUi.addButton.clicked.connect(self.addButtonCMD)
        self.addUi.tvShowCheck.clicked.connect(lambda: self.addUi.stackedWidget.setCurrentIndex(0))
        self.addUi.movieCheck.clicked.connect(lambda: self.addUi.stackedWidget.setCurrentIndex(1))
        self.addUi.todayCheck.clicked.connect(lambda: self.addUi.dateEdit.setEnabled(False))
        # self.addUi.selectDateCheck.clicked.connect(lambda: self.addUi.todayCheck.setEnabled(False))


    def addButtonCMD(self):

        self.getData()
        self.close()

    def run(self):

        self.show()
        self.exec_()

    def getData(self):

        data = []
        t = time.strftime("%Y/%m/%d :: %H:%M", time.gmtime(time.time()))

        if self.addUi.tvShowCheck.isChecked():
            title = self.addUi.tvShowTitleEntry.text()
            se = self.addUi.seasonSpin.text()
            ep = self.addUi.episodeSpin.text()
            date = t

            data.insert(0, "TvShow")
            for item in [title, se, ep, date]:
                data.append(item)

        else:

            title = self.addUi.movieTitle.text()
            if self.addUi.todayCheck.isChecked():
                date = t
            elif self.addUi.selectDateCheck.isChecked():
                date = self.addUi.dateEdit.text()

            data.insert(0, "Movie")
            for item in [title, date]:
                data.append(item)

        return data


class websitesEditDialogClass(QDialog):

    def __init__(self):

        super().__init__()
        self.multiDirUi = websitesEditDialog.Ui_Dialog()
        self.multiDirUi.setupUi(self)

        self.download_sites_Dict = {}
        self.watch_sites_Dict = {}

        
        self.multiDirUi.saveButtonDir.clicked.connect(self.saveCMD)
        self.multiDirUi.helpButtonDir.clicked.connect(self.helpCMD)
        self.multiDirUi.addButttonDir.clicked.connect(self.addCMD)
        self.multiDirUi.clearButtonDir.clicked.connect(self.clearCMD)
        self.multiDirUi.downloadSiteCheck.clicked.connect(self.populateTable)
        self.multiDirUi.watchSiteCheck.clicked.connect(self.populateTable)
        self.multiDirUi.removeButton.clicked.connect(self.removeItem)

        self.multiDirUi.websitesTableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.multiDirUi.websitesTableWidget.customContextMenuRequested.connect(self.on_customContextMenuRequested)


        self.populateTable()

    def saveCMD(self):
        print("save")

        listWidget = self.multiDirUi.websitesTableWidget
        # print(listWidget.rowCount())
        nameList =  [str(listWidget.item(i, 0).text()) for i in range(listWidget.rowCount())]
        linkList =  [str(listWidget.item(i, 1).text()) for i in range(listWidget.rowCount())]

        if self.multiDirUi.watchSiteCheck.isChecked():
            for i in range(listWidget.rowCount()):
                self.watch_sites_Dict[nameList[i]] = [linkList[i]]

        elif self.multiDirUi.downloadSiteCheck.isChecked():
            for i in range(listWidget.rowCount()):
                self.download_sites_Dict[nameList[i]] = [linkList[i]]

        # print(f"watch dict = {self.watch_sites_Dict}, download dict = {self.download_sites_Dict}")
        # print(f"nameList = {nameList} , linkList = {linkList}")
            
        self.close()

    def helpCMD(self):

        print("open help")

    def addCMD(self):

        print("add")

        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter the name of the Website you want to add')
        link, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Enter the link to the website you want to enter')
        if ok and (text!=""):
            
            self.addWebsite([text, link])

    def clearCMD(self):

        self.multiDirUi.websitesTableWidget.clear()

    def run(self):

        self.show()
        self.exec_()

    def addWebsite(self, values=[]):
        table = self.multiDirUi.websitesTableWidget

        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        header = table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.Stretch)
        
        pos = 0
        for value in values:
            # print(f"add {value} at", pos)
            table.setItem(rowPosition, pos, QtGui.QTableWidgetItem(str(value)))
            pos+=1

    def getData(self):

        data = []
        data.append(self.watch_sites_Dict)
        data.append(self.download_sites_Dict)

        return data

    def populateTable(self):

        DIR = os.getcwd()
        with open(f"{DIR}\\v2.0\\utils\\data_base.json") as data_baseFo:
            data_base = json.load(data_baseFo)
            self.multiDirUi.websitesTableWidget.setRowCount(0)

            self.watch_sites_Dict = data_base["watch_sites"]
            self.download_sites_Dict = data_base["download_sites"]
            
            if self.multiDirUi.watchSiteCheck.isChecked():
                for k, v in sorted(self.watch_sites_Dict.items()):
                    v.insert(0, k)
                    self.addWebsite(v)

            elif self.multiDirUi.downloadSiteCheck.isChecked():
                for k, v in sorted(self.download_sites_Dict.items()):
                    v.insert(0, k)
                    self.addWebsite(v)

    def removeItem(self):

        curItem = self.multiDirUi.websitesTableWidget.currentItem()

        print(f"remove {curItem.text()}")

    @pyqtSlot(QPoint)
    def on_customContextMenuRequested(self, pos):

        top_menu = QMenu(self)

        menu = top_menu.addMenu("Menu")
        config = menu.addMenu("Configuration ...")

        _load = config.addAction("&Load ...")
        _save = config.addAction("&Save ...")

        config.addSeparator()

        config1 = config.addAction("Config1")
        config2 = config.addAction("Config2")
        config3 = config.addAction("Config3")

        action = menu.exec_(QtGui.QCursor.pos())

        if action == _load:
            # do this
            pass
        elif action == _save:
            # do this
            pass
        elif action == config1:
            # do this
            pass
        elif action == config2:
            # do this
            pass
        elif action == config3:
            # do this
            pass

def getDataBase():
    global data_base

    DIR = os.getcwd()
    with open(f"{DIR}\\v2.0\\utils\\data_base.json") as data_baseFo:
        data_base = json.load(data_baseFo)

    return data_base
        
def writeDataBase(database_dict):

    DIR = os.getcwd()
    with open(f"{DIR}\\v2.0\\utils\\data_base.json", "w") as data_baseFo:
        json.dump(database_dict, data_baseFo, indent=2)























if __name__ == "__main__":

    w = QApplication([])
    app = App()
    app.show()
    w.exec_()


