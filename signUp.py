import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

from signIn import SignIn
from user import User

class SignUp(QDialog):
    def __init__(self,widget):
        super(SignUp, self).__init__()
        loadUi("ui/signUp.ui", self)
        self.btnSignIn_Up.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSignIn_Up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignUp_Up.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignUp_Up.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordFillUp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verifyPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSignIn_Up.clicked.connect(self.gotoSignIn)
        self.btnSignUp_Up.clicked.connect(self.login)

    def gotoSignIn(self,widget):
        goto_signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(goto_signIn)
        widget.setCurrentWidget(goto_signIn)
    
    def login(self,widget):
        user = User(widget)
        widget.removeWidget(self)
        widget.addWidget(user)
        widget.setCurrentWidget(user)
        
#test display interface
# app = QApplication(sys.argv)
# signIn = SignUp()
# widget = QtWidgets.QStackedWidget()
# widget.setWindowTitle('KATodoList')
# widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
# widget.addWidget(signIn)
# widget.setFixedHeight(920)
# widget.setFixedWidth(1620)
# widget.show()
# sys.exit(app.exec_())

