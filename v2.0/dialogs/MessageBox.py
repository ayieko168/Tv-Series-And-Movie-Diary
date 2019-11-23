from PyQt4.QtGui import *

def showMessage(_type="INFO", title="INFORMATION", message="", detailed="", ):

    def msgbtn(i):
        return i.text()

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    textResalt = msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()
    print ("value of pressed message box button:", retval)

    return textResalt

def showInfoMessage(message=""):

    def msgbtn(i):
        global textResalt
        textResalt = i.text().replace("&", "")

    msg = QMessageBox()

    msg.setIcon(QMessageBox.Information)
    msg.setText(message)
    msg.setWindowTitle("INFORMATION")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()

    return textResalt

def showWarningMessage(message=""):

    def msgbtn(i):
        global textResalt
        textResalt = i.text().replace("&", "")

    msg = QMessageBox()

    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("WARNING")
    msg.setStandardButtons(QMessageBox.Yes  | QMessageBox.No)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()

    return textResalt

def showErrorMessage(message="", details=""):

    def msgbtn(i):
        global textResalt
        textResalt = i.text().replace("&", "")

    msg = QMessageBox()

    if details != "":
        msg.setDetailedText(details)
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle("ERROR")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()

    return textResalt
















