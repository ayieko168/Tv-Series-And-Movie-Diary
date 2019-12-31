from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from MainDesign import *
import dialogs.MessageBox as messagebox
from dialogs import cridentialsDialog
from dialogs import wishListDialog
from dialogs import addNewTitleDialog
from dialogs import websitesEditDialog
from utils import checker, search_function
import webbrowser
import json, os, time, shutil, requests
from github import Github

data_base = {}
data_base_path = ""
template_path = ""
values_format = "title, type, season, episode, datecomplete, datebrake, dateadded, dateseen"


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
        self.ui.searchTitleEntry.textChanged.connect(self.flySearchTitleFunction)
        self.ui.searchButton.clicked.connect(self.searchTitleFunction)
        self.ui.searchButton.clicked.connect(self.flySearchTitleFunction)

        

        ## KEY BINDING
        # self.ui.addNewEntryButton.setShortcut("F6")

        ## SETUP 
        setUpPaths()
        self.setUpTables()
        self.initialDataPopulation()
        updateSearchList()

        # Set Up Richt Click Functionality
        self.ui.currentlyWatchingTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.currentlyWatchingTable.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        self.ui.completedTvShowsTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.completedTvShowsTable.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        self.ui.onBreakTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.onBreakTable.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        self.ui.wishListTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.wishListTable.customContextMenuRequested.connect(self.on_customContextMenuRequested)
        self.ui.seenMoviesTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.seenMoviesTable.customContextMenuRequested.connect(self.on_customContextMenuRequested)

    def searchTitleFunction(self):

        title = self.ui.searchTitleEntry.text()
        if self.ui.searchSourceOnlineCheck.isChecked():
            print("not fly online = ", title)

    def flySearchTitleFunction(self):

        title = self.ui.searchTitleEntry.text()

        if self.ui.searchSourceLocalCheck.isChecked():
            # print("fly local = ", title)

            searchList = getDataBase()["search_dict"]
            self.ui.searchStatusLabel.setText("Searching...")
            result = search_function.search_the_word(searchList, title)
            match = result["match"]
            self.ui.searchStatusLabel.setText(f"Match :: {match}")

            print(f"results for {title} is {result}")

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

                ## test credentials
                print("test credentials")
                git_utils = GithubUtilities()
                validity = git_utils.validate_user(user, _pass)

                ## Sign In to Github..
                if validity == "Valid User":
                    print("sign in to github")
                    git_utils.sign_in(user, _pass)
                else:
                    print("Cant sign in to github because of bad credentials or bad connections")

                # ## Store
                # data_base = getDataBase()
                # data_base["details"]["use"] = user
                # data_base["details"]["pas"] = checker.encoder(_pass)
                # data_base["details"]["occupied"] = "True"
                #
                # writeDataBase(data_base)


        elif selection == "Logout option":
            
            pass

        elif selection == "Create Account":

             webbrowser.open_new_tab('https://github.com/join')

        elif selection == "Add To Wish List":

            wishDi = wishDialoClass()
            wishDi.run()
            title = wishDi.getTitle()
            print(f"add {title} to the wish list")
        
        elif selection == "Add New Title":

            self.addNewEntryButtonCMD()

        elif selection == "Clear All Data":

            ret = messagebox.showWarningMessage("All your data will be lost.\nAre you sure you want to clear all your data?")
            if ret == "Yes":
                print("clear data")
                

                with open(template_path) as tempFo:
                    tempDict = json.load(tempFo)
                
                with open(data_base_path, "w") as destFo:
                    json.dump(tempDict, destFo, indent=2, separators=(',', ':  '))
                
                self.initialDataPopulation()

        elif selection == "Update Local Search List":

            updateSearchList()

    def menuHelpCMD(self, q):
        selection = q.text()
        print(f"open {selection} help dialog")

        if selection == "Video Tutorials":
    
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=2lI5CvZjBPI&list=PLYBkj59Lkv1rtz6lrjRHIizK3kTTH41vB")
        
        elif selection == "About":

            pass

    def menuDownload_SitesCMD(self, q):

        # INIT
        selection = q.text()
        self.selectionLogic(selection, self.ui.menuDownload_Sites)
        self.selected_download_Site_Link = getDataBase()["download_sites"][selection][0]

        print(f"selected_watch_Site set to  = {selection}, link = {self.selected_download_Site_Link}")
        
    def menuWatch_SitesCMD(self, q):
        
        # INIT
        selection = q.text()
        self.selectionLogic(selection, self.ui.menuWatch_Sites)
        self.selected_watch_Site_Link = getDataBase()["watch_sites"][selection][0]

        print(f"selected_watch_Site set to  = {selection}, link = {self.selected_watch_Site_Link}")
        
    def menuFileCMD(self, q):
        command = q.text()

        if command == "Push My Data":
            print("push")

            print("prepairing to push your data...")
            print("done.")
        
        elif command == "Pull My Data":
            print("pull")
        
        elif command == "Buck Up My Data":

            print("create buck up")
            user = os.getlogin()

            data_base_dst = f"C:\\Users\\{user}\\Desktop\\TvShow_Diary_Database_buckup.buk"

            shutil.copyfile(data_base_path, data_base_dst)

            print("done.")

        elif command == "Load Data from A Buckup":

            filepath = QFileDialog.getOpenFileName(filter = "Buck Up Files (*.buk)")

            ## Load the data from it and then dump the data to the programms data_base
            with open(filepath) as buckFo:
                data_base = json.load(buckFo)
            
            writeDataBase(data_base)

            self.initialDataPopulation()

            print("done.")

        elif command == "Edit Sites":
            print("edit sites")

            webEd = websitesEditDialogClass()
            webEd.run()
            watch, download = webEd.getData()
            ret = webEd.returnCode()

            if ret == 0:
                data_base = getDataBase()
                data_base["watch_sites"] = watch
                data_base["download_sites"] = download

                writeDataBase(data_base)
                
                self.initialDataPopulation()
            else:
                print("nothing to write")

        elif command == "Exit":
            print("exit")

            self.close()
        
    def initialDataPopulation(self):
        """Populate the tables with the databased found. Also
           Populate the menubar with the optional menus i.e:
           the watch sites and download sites. This also sets
           the default selected site option.
           """
        
        with open(data_base_path) as data_baseFo:
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
            currently_watching_values = [v[0], v[2], v[3]]
            self.addTableItem(self.ui.currentlyWatchingTable, currently_watching_values)
        
        # populate complete_tv_shows table
        for k, v in sorted(self.complete_tv_shows_Dict.items()):
            complete_tv_shows_values = [v[0], v[2], v[3], v[4]]
            self.addTableItem(self.ui.completedTvShowsTable, complete_tv_shows_values)
        
        # populate shows_on_break table
        for k, v in sorted(self.shows_on_break_Dict.items()):
            shows_on_break_values = [v[0], v[2], v[3], v[5]]
            self.addTableItem(self.ui.onBreakTable, shows_on_break_values)
        
        # populate wish_list table
        for k, v in sorted(self.wish_list_Dict.items()):
            wish_list_values = [v[0], v[1], v[6]]
            self.addTableItem(self.ui.wishListTable, wish_list_values)
        
        # populate seen_movies table
        for k, v in sorted(self.seen_movies_Dict.items()):
            seen_movies_values = [v[0], v[7]]
            self.addTableItem(self.ui.seenMoviesTable, seen_movies_values)
        

        ## POPULATE THE OPTIONAL MENU OPTIONS
        # Clear the menu options
        self.ui.menuWatch_Sites.clear()
        self.ui.menuDownload_Sites.clear()

        # populate the websites
        for k, v in sorted(self.watch_sites_Dict.items()):
            actionOb = self.ui.menuWatch_Sites.addAction(k)
            actionOb.setCheckable(True)
            if k == self.details_Dict["watch"]:
                actionOb.setChecked(True)
                self.selected_watch_Site_Link = v[0]
            else:
                actionOb.setChecked(False)
        
        for k, v in sorted(self.download_sites_Dict.items()):
            actionOb = self.ui.menuDownload_Sites.addAction(k)
            actionOb.setCheckable(True)
            if k == self.details_Dict["download"]:
                actionOb.setChecked(True)
                self.selected_download_Site_Link = v[0]
            else:
                actionOb.setChecked(False)

    def addTableItem(self, table, values=[]):
        """Add an item at the bottom of the list in 'table', value
           is a list of values of the row created.
           table is a QTablbeWidget object.
           <values> is a list that starts with the Item Name then the values.
           """

        rowPosition = table.rowCount()
        table.insertRow(rowPosition)
        
        pos = 0
        for value in values:
            # print(f"add {value} at", pos)
            table.setItem(rowPosition, pos, QTableWidgetItem(str(value)))
            pos+=1

    def addNewEntryButtonCMD(self):

        ## open the add title dialog and get the entered data
        newDialog = addTitleDialogClass()
        newDialog.run()
        data = newDialog.getData()
        print(data[0])

        ## Add the title in to the respective table and update the database
        if (data[0] == "TvShow") and (data[1] != ""):
            self.addTableItem(self.ui.currentlyWatchingTable, data[1:])
            writeTableToDataBase(self.ui.currentlyWatchingTable, "currently_watching")
            updateSearchList()
        elif (data[0] == "Movie") and (data[1] != ""):
            self.addTableItem(self.ui.seenMoviesTable, data[1:])
            writeTableToDataBase(self.ui.seenMoviesTable, "seen_movies")
            updateSearchList()
        else:
            print("nothing to write")
         
    def setUpTables(self):
        """set the basic pproperties of the tables"""

        header = self.ui.currentlyWatchingTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        header = self.ui.completedTvShowsTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)

        header = self.ui.onBreakTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        header = self.ui.wishListTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        header = self.ui.seenMoviesTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.ui.stackedWidget.setCurrentIndex(0)

    def menuCurent_TableCMD(self, q):
        """swithch the current tab to a selection you make."""
        
        command = q.text()
        self.selectionLogic(command, self.ui.menuCurent_Table)

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

    def selectionLogic(self, selection, menu):
        """Set all other menu options not selected to False
           when one of the menu options are set. This only
           applie to Qaction objects that are set to checkable."""

        for actn in menu.actions():
            if actn.text() != selection:
                actn.setChecked(False)

    @pyqtSlot(QPoint)
    def on_customContextMenuRequested(self, pos):

        table = QApplication.focusWidget()
        tableName = table.objectName()

        top_menu = QMenu(self)
        menu = top_menu.addMenu("Menu")

        Edit = menu.addAction("Edit")
        menu.addSeparator()
        moveTo = menu.addMenu("Move title to...")
        menu.addSeparator()
        trailer = menu.addAction("Watch Trailer")
        viewThumb = menu.addAction("View Thumbnail")
        menu.addSeparator()
        download = menu.addAction("Download")
        watch = menu.addAction("Wathch Online")
        viewDetails = menu.addAction("Vied Details")
        menu.addSeparator()
        delete = menu.addAction("Delete")

        currentlyWatching = moveTo.addAction("Currentlt watching Tab")
        complete = moveTo.addAction("Complete Show Tab")
        onBreak = moveTo.addAction("On Breake Tab")
        wishList = moveTo.addAction("Wish List Tab")
        seen = moveTo.addAction("Seen Movies Tab")

        if tableName == "currentlyWatchingTable":
            key = "currently_watching"
        elif tableName == "completedTvShowsTable":
            key = "complete_tv_shows"
        elif tableName == "onBreakTable":
            key = "shows_on_break"
        elif tableName == "wishListTable":
            key = "wish_list"
        elif tableName == "seenMoviesTable":
            key = "seen_movies"
        
        def getItemData(itemIndex):
            data = []

            for i in range(table.columnCount()):
                print(i)
                try:
                    data.append(table.item(itemIndex, i).text())
                except:
                    pass

            return data
        

        action = menu.exec_(QtGui.QCursor.pos())

        if action == Edit:
            # do this
            pass
        
        elif action == currentlyWatching:
            # tabel = QTableWidget.objectName
                # QTableWidget.columnAt()
                # QModelIndex.row()
                # QTableWidgetItem.text
                # print(f"item index = {item_index}")
                # print(table.itemAt(item_index, 0))

            item_row = table.currentIndex().row()
            itemName = table.item(item_row, 0).text()
            itemData = getItemData(item_row)
            
            print(f"item Selected = {itemName}")
            print(f"item data = {itemData}")

            # Remove from this tables data base
            table.removeRow(item_row)
            writeTableToDataBase(table, key)

            # Add to desired data base
            self.addTableItem(self.ui.currentlyWatchingTable, itemData)
            writeTableToDataBase(self.ui.currentlyWatchingTable, "currently_watching")
  
        elif action == complete:
            item_row = table.currentIndex().row()
            itemName = table.item(item_row, 0).text()
            itemData = getItemData(item_row)
            
            print(f"item Selected = {itemName}")
            print(f"item data = {itemData}")

            # Remove from this tables data base
            table.removeRow(item_row)
            writeTableToDataBase(table, key)

            # Add to desired data base
            self.addTableItem(self.ui.completedTvShowsTable, itemData)
            writeTableToDataBase(self.ui.completedTvShowsTable, "complete_tv_shows")

        elif action == onBreak:
            item_row = table.currentIndex().row()
            itemName = table.item(item_row, 0).text()
            itemData = getItemData(item_row)
            
            print(f"item Selected = {itemName}")
            print(f"item data = {itemData}")

            # Remove from this tables data base
            table.removeRow(item_row)
            writeTableToDataBase(table, key)

            # Add to desired data base
            self.addTableItem(self.ui.onBreakTable, itemData)
            writeTableToDataBase(self.ui.onBreakTable, "shows_on_break")

        elif action == wishList:
            item_row = table.currentIndex().row()
            itemName = table.item(item_row, 0).text()
            itemData = getItemData(item_row)
            
            print(f"item Selected = {itemName}")
            print(f"item data = {itemData}")

            # Remove from this tables data base
            table.removeRow(item_row)
            writeTableToDataBase(table, key)

            # Add to desired data base
            self.addTableItem(self.ui.wishListTable, itemData)
            writeTableToDataBase(self.ui.wishListTable, "wish_list")

        elif action == seen:
            item_row = table.currentIndex().row()
            itemName = table.item(item_row, 0).text()
            itemData = getItemData(item_row)
            
            print(f"item Selected = {itemName}")
            print(f"item data = {itemData}")

            # Remove from this tables data base
            table.removeRow(item_row)
            writeTableToDataBase(table, key)

            # Add to desired data base
            self.addTableItem(self.ui.seenMoviesTable, itemData)
            writeTableToDataBase(self.ui.seenMoviesTable, "seen_movies")

        elif action == trailer:
            item_row = table.currentIndex().row()
            curItem = table.item(item_row, 0).text()

            webbrowser.open_new_tab("https://www.youtube.com/results?search_query={}".format(curItem))

        elif action == viewThumb:
            # do this
            pass
        elif action == download:
            title = table.item(table.currentIndex().row(), 0).text()

            self.download(title)

        elif action == watch:

            title = table.item(table.currentIndex().row(), 0).text()

            self.watch(title)

        elif action == viewDetails:
            # do this
            pass
        elif action == delete:
            # do this
            pass
        
    def watch(self, title):

        print(f"watch {title}")
        title = title.lower()
        link = self.selected_watch_Site_Link

        try:
            link = link.replace("{}", title)
            webbrowser.open_new_tab(link)
        except Exception as e:
            print("exception = ", e)
            webbrowser.open_new_tab(link)

        print(link, title)

    def download(self, title):

        print(f"download {title}")
        title = title.lower()
        link = self.selected_download_Site_Link

        try:
            link = link.replace("{}", title)
            webbrowser.open_new_tab(link)
        except Exception as e:
            print("exception = ", e)
            webbrowser.open_new_tab(link)

        print(link, title)

    # def update


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
            self.crUi.passwordEntryCri.setEchoMode(QLineEdit.Normal)
            self.crUi.showButtonCri.setText("hide")
        else:
            self.crUi.passwordEntryCri.setEchoMode(QLineEdit.Password)
            self.crUi.showButtonCri.setText("show")

    def getCridentials(self):
        """return a list containing the current user, pass and occupation state obtained from the GetCredentials Dialog"""

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

        print("done")

        self.getCridentials()
        if (self.crUi.userNameEntryCri.text() == "") or (self.crUi.passwordEntryCri.text() == ""):
            print("Plese enter some credentials... one of the fields is empty")
        else:
            self.getCridentials()
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
            title = self.addUi.tvShowTitleEntry.text().title()
            se = self.addUi.seasonSpin.text()
            ep = self.addUi.episodeSpin.text()
            date = t

            data.insert(0, "TvShow")
            for item in [title, se, ep, date]:
                data.append(item)

        else:

            title = self.addUi.movieTitle.text().title()
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
        
        self.multiDirUi.saveButtonDir.clicked.connect(self.saveCMD)
        self.multiDirUi.helpButtonDir.clicked.connect(self.helpCMD)
        self.multiDirUi.addButttonDir.clicked.connect(self.addCMD)
        self.multiDirUi.clearButtonDir.clicked.connect(self.clearCMD)
        self.multiDirUi.downloadSiteCheck.clicked.connect(self.populateTable)
        self.multiDirUi.watchSiteCheck.clicked.connect(self.populateTable)
        self.multiDirUi.removeButton.clicked.connect(self.removeItem)

        self.download_sites_Dict = {}
        self.watch_sites_Dict = {}
        self.return_code = 1

        # Set Up Richt Click Functionality
        self.multiDirUi.websitesTableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.multiDirUi.websitesTableWidget.customContextMenuRequested.connect(self.on_customContextMenuRequested)

        self.populateTable()

    def saveCMD(self):
        print("save")

        listWidget = self.multiDirUi.websitesTableWidget
        nameList =  [str(listWidget.item(i, 0).text()) for i in range(listWidget.rowCount())]
        linkList =  [str(listWidget.item(ii, 1).text()) for ii in range(listWidget.rowCount())]

       

        if self.multiDirUi.watchSiteCheck.isChecked():
            self.watch_sites_Dict = {}

            for j in range(listWidget.rowCount()):
                self.watch_sites_Dict[nameList[j]] = [linkList[j]]
                # print("inside watch")
                # print(f"nameList = {nameList} , linkList = {linkList}")

        elif self.multiDirUi.downloadSiteCheck.isChecked():
            self.download_sites_Dict = {}

            for jj in range(listWidget.rowCount()):
                self.download_sites_Dict[nameList[jj]] = [linkList[jj]]
                # print("insude download")
                # print(f"nameList = {nameList} , linkList = {linkList}")

        # print(f"watch dict = {self.watch_sites_Dict}, download dict = {self.download_sites_Dict}")
        # print(f"nameList = {nameList} , linkList = {linkList}")
        
        self.return_code = 0
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

        rows = self.multiDirUi.websitesTableWidget.rowCount() + 1
        for row in range(rows):
            print(f"remove row {row}, of {rows} rows")
            self.multiDirUi.websitesTableWidget.removeRow(0)
        
        self.multiDirUi.websitesTableWidget.update()

    def run(self):

        self.show()
        self.exec_()

    def addWebsite(self, values=[]):
        table = self.multiDirUi.websitesTableWidget

        rowPosition = table.rowCount()
        table.insertRow(rowPosition)

        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        
        pos = 0
        for value in values:
            # print(f"add {value} at", pos)
            table.setItem(rowPosition, pos, QTableWidgetItem(str(value)))
            pos+=1

    def getData(self):

        data = []
        data.append(self.watch_sites_Dict)
        data.append(self.download_sites_Dict)

        return data

    def populateTable(self):
        
        with open(data_base_path) as data_baseFo:
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

        curItem = self.multiDirUi.websitesTableWidget.currentRow()
        print(curItem)
        self.multiDirUi.websitesTableWidget.removeRow(curItem)
        self.multiDirUi.websitesTableWidget.update()

        print(f"remove {curItem}")

    def returnCode(self):

        return self.return_code

    @pyqtSlot(QPoint)
    def on_customContextMenuRequested(self, pos):
        
        table = self.multiDirUi.websitesTableWidget
        top_menu = QMenu(self)

        menu = top_menu.addMenu("Menu")

        remove = menu.addAction("Remove")
        edit = menu.addAction("Edit")
        menu.addSeparator()
        default = menu.addAction("Make Default")
        
        action = menu.exec_(QtGui.QCursor.pos())

        if action == remove:
            self.removeItem()

        elif action == edit:
            # do this
            pass
        elif action == default:
            if self.multiDirUi.downloadSiteCheck.isChecked():
                siteName = table.item(table.currentIndex().row(), 0).text()
                print(f"make {siteName} the default download website")

                data_base = getDataBase()
                detailDict = data_base["details"]
                detailDict["download"] = siteName
                data_base["details"] = detailDict

                writeDataBase(data_base)
            elif self.multiDirUi.watchSiteCheck.isChecked():

                siteName = table.item(table.currentIndex().row(), 0).text()
                print(f"make {siteName} the default watch website")

                data_base = getDataBase()
                detailDict = data_base["details"]
                detailDict["watch"] = siteName
                data_base["details"] = detailDict

                writeDataBase(data_base)


class GithubUtilities:

    def __init__(self):

        pass

    def sign_in(self, user, pas):

        g = Github("user", "password")

    def validate_user(self, user, pas):

        r = requests.get('https://api.github.com', auth=(user, pas))
        return_status = r.status_code

        if return_status == requests.codes.ok:
            return "Valid User"
        else:
            return "Invalid User"


def getDataBase():
    """Return a dictionary containing the main database"""
    global data_base

    with open(data_base_path) as data_baseFo:
        data_base = json.load(data_baseFo)

    return data_base


def writeDataBase(database_dict):

    with open(data_base_path, "w") as data_baseFo:
        json.dump(database_dict, data_baseFo, indent=2, separators=(',', ':  '))


def writeTableToDataBase(table, datakey):
    """ Write the existent table items to the database under
        <datakey> key in the dasired dictionary"""

    data_base = getDataBase()
    datakey_Dict = data_base[datakey]
    data_Dict = {}
    listWidget = table
    t = time.strftime("%Y/%m/%d :: %H:%M", time.gmtime(time.time()))
    # QTableView

    for i in range(listWidget.rowCount()):
        title = str(listWidget.item(i, 0).text())
        previousValues = datakey_Dict[title]
        pv = previousValues

        values = []
        for j in range(listWidget.columnCount()):
            value = str(listWidget.item(i, j+1).text())
            values.append(value)

        data_Dict[title] = [title, pv[1], values[0], values[1], t]
        
        data_base[datakey] = data_Dict

    # writeDataBase(data_base)


def updateSearchList():

    data_base = getDataBase()

    currently_watchingDict = data_base["currently_watching"]
    complete_tv_showsDict = data_base["complete_tv_shows"]
    shows_on_breakDict = data_base["shows_on_break"]
    wish_listDict = data_base["wish_list"]
    recycle_binDict = data_base["recycle_bin"]
    search_dictList = data_base["search_dict"]

    for _dict in (currently_watchingDict, complete_tv_showsDict, shows_on_breakDict, wish_listDict, recycle_binDict):
        for k, _ in _dict.items():
            if k not in search_dictList:
                search_dictList.append(k)
    
    data_base["search_dict"] = sorted(search_dictList)

    writeDataBase(data_base)

    print("done.")


def setUpPaths():

    global data_base_path, template_path

    ## set up data base path
    try:
        x = os.path.abspath("utils\\data_base.json")
        with open(x) as p:
            pass
    except FileNotFoundError:
        x = os.path.abspath("v2.0\\utils\\data_base.json")
        with open(x) as p:
            pass

    data_base_path = x

    ## set up template path
    try:
        x = os.path.abspath("utils\\template.json")
        with open(x) as p:
            pass
    except FileNotFoundError:
        x = os.path.abspath("v2.0\\utils\\template.json")
        with open(x) as p:
            pass

    template_path = x


























if __name__ == "__main__":

    w = QApplication([])
    app = App()
    app.show()
    w.exec_()


