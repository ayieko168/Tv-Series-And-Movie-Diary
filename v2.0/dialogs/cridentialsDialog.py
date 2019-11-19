# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/cridentialsDialog.ui'
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
        Dialog.resize(368, 142)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.doneButtonCri = QtGui.QPushButton(Dialog)
        self.doneButtonCri.setGeometry(QtCore.QRect(280, 100, 75, 23))
        self.doneButtonCri.setObjectName(_fromUtf8("doneButtonCri"))
        self.showButtonCri = QtGui.QPushButton(Dialog)
        self.showButtonCri.setGeometry(QtCore.QRect(170, 100, 75, 23))
        self.showButtonCri.setObjectName(_fromUtf8("showButtonCri"))
        self.userNameEntryCri = QtGui.QLineEdit(Dialog)
        self.userNameEntryCri.setGeometry(QtCore.QRect(110, 20, 251, 20))
        self.userNameEntryCri.setObjectName(_fromUtf8("userNameEntryCri"))
        self.passwordEntryCri = QtGui.QLineEdit(Dialog)
        self.passwordEntryCri.setGeometry(QtCore.QRect(110, 60, 251, 20))
        self.passwordEntryCri.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordEntryCri.setObjectName(_fromUtf8("passwordEntryCri"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.rememberMeCheckCri = QtGui.QCheckBox(Dialog)
        self.rememberMeCheckCri.setGeometry(QtCore.QRect(50, 100, 91, 21))
        self.rememberMeCheckCri.setChecked(True)
        self.rememberMeCheckCri.setObjectName(_fromUtf8("rememberMeCheckCri"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Credentials Dialog", None))
        self.label.setText(_translate("Dialog", "User Name / Email: ", None))
        self.doneButtonCri.setText(_translate("Dialog", "Done", None))
        self.showButtonCri.setText(_translate("Dialog", "show", None))
        self.label_2.setText(_translate("Dialog", "Password: ", None))
        self.rememberMeCheckCri.setText(_translate("Dialog", "Remember Me", None))

