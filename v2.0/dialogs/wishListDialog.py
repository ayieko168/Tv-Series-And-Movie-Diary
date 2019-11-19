# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ayieko/Projects And  Research/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/wishListDialog.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(425, 90)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(6, 6, 411, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.titleEntry = QtGui.QLineEdit(self.groupBox)
        self.titleEntry.setGeometry(QtCore.QRect(50, 30, 271, 20))
        self.titleEntry.setObjectName(_fromUtf8("titleEntry"))
        self.addButton = QtGui.QPushButton(self.groupBox)
        self.addButton.setGeometry(QtCore.QRect(330, 22, 71, 31))
        self.addButton.setObjectName(_fromUtf8("addButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Wish List Dialog", None))
        self.groupBox.setTitle(_translate("Form", "Add A Title To Your Wish List", None))
        self.label.setText(_translate("Form", "Title :", None))
        self.addButton.setText(_translate("Form", "Add", None))

