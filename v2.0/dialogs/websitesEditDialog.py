# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/websitesEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 300)
        self.websitesTableWidget = QtWidgets.QTableWidget(Dialog)
        self.websitesTableWidget.setGeometry(QtCore.QRect(5, 5, 298, 289))
        self.websitesTableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.websitesTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.websitesTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.websitesTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.websitesTableWidget.setObjectName("websitesTableWidget")
        self.websitesTableWidget.setColumnCount(2)
        self.websitesTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.websitesTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.websitesTableWidget.setHorizontalHeaderItem(1, item)
        self.websitesTableWidget.verticalHeader().setVisible(False)
        self.websitesTableWidget.verticalHeader().setDefaultSectionSize(19)
        self.websitesTableWidget.verticalHeader().setMinimumSectionSize(15)
        self.saveButtonDir = QtWidgets.QPushButton(Dialog)
        self.saveButtonDir.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.saveButtonDir.setObjectName("saveButtonDir")
        self.addButttonDir = QtWidgets.QPushButton(Dialog)
        self.addButttonDir.setGeometry(QtCore.QRect(310, 60, 75, 23))
        self.addButttonDir.setObjectName("addButttonDir")
        self.helpButtonDir = QtWidgets.QPushButton(Dialog)
        self.helpButtonDir.setGeometry(QtCore.QRect(310, 180, 75, 23))
        self.helpButtonDir.setObjectName("helpButtonDir")
        self.clearButtonDir = QtWidgets.QPushButton(Dialog)
        self.clearButtonDir.setGeometry(QtCore.QRect(310, 140, 75, 23))
        self.clearButtonDir.setObjectName("clearButtonDir")
        self.removeButton = QtWidgets.QPushButton(Dialog)
        self.removeButton.setGeometry(QtCore.QRect(310, 100, 75, 23))
        self.removeButton.setObjectName("removeButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 210, 101, 77))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(61, 21))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.downloadSiteCheck = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSiteCheck.sizePolicy().hasHeightForWidth())
        self.downloadSiteCheck.setSizePolicy(sizePolicy)
        self.downloadSiteCheck.setMinimumSize(QtCore.QSize(91, 21))
        self.downloadSiteCheck.setChecked(True)
        self.downloadSiteCheck.setObjectName("downloadSiteCheck")
        self.verticalLayout.addWidget(self.downloadSiteCheck)
        self.watchSiteCheck = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watchSiteCheck.sizePolicy().hasHeightForWidth())
        self.watchSiteCheck.setSizePolicy(sizePolicy)
        self.watchSiteCheck.setMinimumSize(QtCore.QSize(91, 21))
        self.watchSiteCheck.setObjectName("watchSiteCheck")
        self.verticalLayout.addWidget(self.watchSiteCheck)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Multi Option Dialog"))
        item = self.websitesTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Website name"))
        item = self.websitesTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Website Link"))
        self.saveButtonDir.setText(_translate("Dialog", "Save"))
        self.addButttonDir.setText(_translate("Dialog", "Add"))
        self.helpButtonDir.setText(_translate("Dialog", "Help"))
        self.clearButtonDir.setText(_translate("Dialog", "Clear"))
        self.removeButton.setText(_translate("Dialog", "Remove"))
        self.label.setText(_translate("Dialog", "Site Type:"))
        self.downloadSiteCheck.setText(_translate("Dialog", "Download Site"))
        self.watchSiteCheck.setText(_translate("Dialog", "Watch Site"))
