# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/wishListDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(425, 90)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(6, 6, 411, 71))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.titleEntry = QtWidgets.QLineEdit(self.groupBox)
        self.titleEntry.setGeometry(QtCore.QRect(50, 30, 271, 20))
        self.titleEntry.setObjectName("titleEntry")
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setGeometry(QtCore.QRect(330, 22, 71, 31))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Wish List Dialog"))
        self.groupBox.setTitle(_translate("Form", "Add A Title To Your Wish List"))
        self.label.setText(_translate("Form", "Title :"))
        self.addButton.setText(_translate("Form", "Add"))
