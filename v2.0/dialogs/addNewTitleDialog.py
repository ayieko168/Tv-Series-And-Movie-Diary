# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Tv-Series-And-Movie-Diary/v2.0/dialogs/addNewTitleDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 196)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 351, 151))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 331, 148))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label.setObjectName("label")
        self.tvShowTitleEntry = QtWidgets.QLineEdit(self.groupBox)
        self.tvShowTitleEntry.setGeometry(QtCore.QRect(60, 30, 251, 20))
        self.tvShowTitleEntry.setObjectName("tvShowTitleEntry")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 51, 21))
        self.label_2.setObjectName("label_2")
        self.seasonSpin = QtWidgets.QSpinBox(self.groupBox)
        self.seasonSpin.setGeometry(QtCore.QRect(110, 70, 61, 22))
        self.seasonSpin.setMinimum(1)
        self.seasonSpin.setMaximum(100)
        self.seasonSpin.setObjectName("seasonSpin")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 51, 21))
        self.label_3.setObjectName("label_3")
        self.episodeSpin = QtWidgets.QSpinBox(self.groupBox)
        self.episodeSpin.setGeometry(QtCore.QRect(110, 110, 61, 22))
        self.episodeSpin.setMinimum(1)
        self.episodeSpin.setMaximum(100)
        self.episodeSpin.setObjectName("episodeSpin")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 331, 148))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.label_4.setObjectName("label_4")
        self.movieTitle = QtWidgets.QLineEdit(self.groupBox_2)
        self.movieTitle.setGeometry(QtCore.QRect(60, 30, 251, 20))
        self.movieTitle.setObjectName("movieTitle")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 60, 231, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.todayCheck = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todayCheck.sizePolicy().hasHeightForWidth())
        self.todayCheck.setSizePolicy(sizePolicy)
        self.todayCheck.setMinimumSize(QtCore.QSize(91, 21))
        self.todayCheck.setChecked(True)
        self.todayCheck.setObjectName("todayCheck")
        self.verticalLayout.addWidget(self.todayCheck)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.selectDateCheck = QtWidgets.QRadioButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectDateCheck.sizePolicy().hasHeightForWidth())
        self.selectDateCheck.setSizePolicy(sizePolicy)
        self.selectDateCheck.setObjectName("selectDateCheck")
        self.horizontalLayout_3.addWidget(self.selectDateCheck)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_2)
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(250, 160, 75, 31))
        self.addButton.setObjectName("addButton")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 160, 181, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tvShowCheck = QtWidgets.QRadioButton(self.layoutWidget1)
        self.tvShowCheck.setChecked(True)
        self.tvShowCheck.setObjectName("tvShowCheck")
        self.horizontalLayout.addWidget(self.tvShowCheck)
        self.movieCheck = QtWidgets.QRadioButton(self.layoutWidget1)
        self.movieCheck.setObjectName("movieCheck")
        self.horizontalLayout.addWidget(self.movieCheck)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        self.selectDateCheck.clicked['bool'].connect(self.dateEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add A New Title Entry"))
        self.groupBox.setTitle(_translate("Dialog", "Add A New TV Show You Are Seeing."))
        self.label.setText(_translate("Dialog", "Title :"))
        self.tvShowTitleEntry.setPlaceholderText(_translate("Dialog", " Tv Show Title"))
        self.label_2.setText(_translate("Dialog", "Season :"))
        self.label_3.setText(_translate("Dialog", "Episode :"))
        self.groupBox_2.setTitle(_translate("Dialog", "Add A New Movie You Are Seeing."))
        self.label_4.setText(_translate("Dialog", "Title :"))
        self.movieTitle.setPlaceholderText(_translate("Dialog", " Tv Show Title"))
        self.label_5.setText(_translate("Dialog", "Date Seen : "))
        self.todayCheck.setText(_translate("Dialog", "Today."))
        self.selectDateCheck.setText(_translate("Dialog", "Select Date : "))
        self.addButton.setText(_translate("Dialog", "ADD"))
        self.tvShowCheck.setText(_translate("Dialog", "Tv Show"))
        self.movieCheck.setText(_translate("Dialog", "Movie "))
