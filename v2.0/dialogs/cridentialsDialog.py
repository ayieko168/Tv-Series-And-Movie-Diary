# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/cridentialsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 142)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.doneButtonCri = QtWidgets.QPushButton(Dialog)
        self.doneButtonCri.setGeometry(QtCore.QRect(280, 100, 75, 23))
        self.doneButtonCri.setObjectName("doneButtonCri")
        self.showButtonCri = QtWidgets.QPushButton(Dialog)
        self.showButtonCri.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.showButtonCri.setObjectName("showButtonCri")
        self.userNameEntryCri = QtWidgets.QLineEdit(Dialog)
        self.userNameEntryCri.setGeometry(QtCore.QRect(110, 20, 251, 20))
        self.userNameEntryCri.setObjectName("userNameEntryCri")
        self.passwordEntryCri = QtWidgets.QLineEdit(Dialog)
        self.passwordEntryCri.setGeometry(QtCore.QRect(110, 60, 251, 20))
        self.passwordEntryCri.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEntryCri.setObjectName("passwordEntryCri")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 61, 20))
        self.label_2.setObjectName("label_2")
        self.rememberMeCheckCri = QtWidgets.QCheckBox(Dialog)
        self.rememberMeCheckCri.setGeometry(QtCore.QRect(50, 100, 91, 21))
        self.rememberMeCheckCri.setChecked(True)
        self.rememberMeCheckCri.setObjectName("rememberMeCheckCri")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Credentials Dialog"))
        self.label.setText(_translate("Dialog", "User Name / Email: "))
        self.doneButtonCri.setText(_translate("Dialog", "Done"))
        self.showButtonCri.setText(_translate("Dialog", "show"))
        self.label_2.setText(_translate("Dialog", "Password: "))
        self.rememberMeCheckCri.setText(_translate("Dialog", "Remember Me"))
