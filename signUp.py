import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("ui/signUp.ui", self)
        self.btnSignIn_Up.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSignIn_Up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignUp_Up.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid;""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignUp_Up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordFillUp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verifyPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        
#test display interface
app = QApplication(sys.argv)
signIn = SignUp()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.addWidget(signIn)
widget.setFixedHeight(920)
widget.setFixedWidth(1620)
widget.show()
sys.exit(app.exec_())

