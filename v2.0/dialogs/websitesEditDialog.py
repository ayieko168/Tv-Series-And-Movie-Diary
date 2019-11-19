# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/websitesEditDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(422, 300)
        self.websitesTableWidget = QtGui.QTableWidget(Dialog)
        self.websitesTableWidget.setGeometry(QtCore.QRect(5, 5, 298, 289))
        self.websitesTableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.websitesTableWidget.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.SelectedClicked)
        self.websitesTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.websitesTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.websitesTableWidget.setObjectName(_fromUtf8("websitesTableWidget"))
        self.websitesTableWidget.setColumnCount(2)
        self.websitesTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.websitesTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.websitesTableWidget.setHorizontalHeaderItem(1, item)
        self.websitesTableWidget.verticalHeader().setVisible(False)
        self.websitesTableWidget.verticalHeader().setDefaultSectionSize(19)
        self.websitesTableWidget.verticalHeader().setMinimumSectionSize(15)
        self.saveButtonDir = QtGui.QPushButton(Dialog)
        self.saveButtonDir.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.saveButtonDir.setObjectName(_fromUtf8("saveButtonDir"))
        self.addButttonDir = QtGui.QPushButton(Dialog)
        self.addButttonDir.setGeometry(QtCore.QRect(310, 60, 75, 23))
        self.addButttonDir.setObjectName(_fromUtf8("addButttonDir"))
        self.helpButtonDir = QtGui.QPushButton(Dialog)
        self.helpButtonDir.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.helpButtonDir.setObjectName(_fromUtf8("helpButtonDir"))
        self.clearButtonDir = QtGui.QPushButton(Dialog)
        self.clearButtonDir.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.clearButtonDir.setObjectName(_fromUtf8("clearButtonDir"))
        self.removeButton = QtGui.QPushButton(Dialog)
        self.removeButton.setGeometry(QtCore.QRect(310, 100, 75, 23))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 210, 101, 77))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(61, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.downloadSiteCheck = QtGui.QRadioButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSiteCheck.sizePolicy().hasHeightForWidth())
        self.downloadSiteCheck.setSizePolicy(sizePolicy)
        self.downloadSiteCheck.setMinimumSize(QtCore.QSize(91, 21))
        self.downloadSiteCheck.setChecked(True)
        self.downloadSiteCheck.setObjectName(_fromUtf8("downloadSiteCheck"))
        self.verticalLayout.addWidget(self.downloadSiteCheck)
        self.watchSiteCheck = QtGui.QRadioButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watchSiteCheck.sizePolicy().hasHeightForWidth())
        self.watchSiteCheck.setSizePolicy(sizePolicy)
        self.watchSiteCheck.setMinimumSize(QtCore.QSize(91, 21))
        self.watchSiteCheck.setObjectName(_fromUtf8("watchSiteCheck"))
        self.verticalLayout.addWidget(self.watchSiteCheck)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Multi Option Dialog", None))
        item = self.websitesTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Website name", None))
        item = self.websitesTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Website Link", None))
        self.saveButtonDir.setText(_translate("Dialog", "Save", None))
        self.addButttonDir.setText(_translate("Dialog", "Add", None))
        self.helpButtonDir.setText(_translate("Dialog", "Help", None))
        self.clearButtonDir.setText(_translate("Dialog", "Clear", None))
        self.removeButton.setText(_translate("Dialog", "Remove", None))
        self.label.setText(_translate("Dialog", "Site Type:", None))
        self.downloadSiteCheck.setText(_translate("Dialog", "Download Site", None))
        self.watchSiteCheck.setText(_translate("Dialog", "Watch Site", None))

