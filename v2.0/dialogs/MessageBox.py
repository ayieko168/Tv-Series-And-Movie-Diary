from PyQt4.QtGui import *

def showMessage():

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

def msgbtn(i):
#    print ("Button pressed is:", i.text())
   return i.text()