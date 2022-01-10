import pickle
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

from admin import Admin
from user import User
from signUp import SignUp

class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("ui/signIn.ui", self)
        self.btnSignUp_In.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSignUp_In.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignIn_In.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignIn_In.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.passwordFillIn.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSignUp_In.clicked.connect(self.gotoSignUp)
        self.btnSignIn_In.clicked.connect(self.login)

    def gotoSignUp(self):
        signup = SignUp(widget)
        widget.removeWidget(self)
        widget.addWidget(signup)
        widget.setCurrentWidget(signup)


    def login(self):
        username = self.useNameFill.text()
        password = self.passwordFillIn.text()

        if username == "admin":
            if password == "admin123":
                admin = Admin()
                widget.removeWidget(self)
                widget.addWidget(admin)
                widget.setCurrentWidget(admin)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Incorrect password!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()
        else:
            with open ('data/user.dat', 'rb') as userdata:
                while True:
                    try:
                        row = pickle.load(userdata)
                        if row[0] == username:
                            if row[1] == password:
                                user = User()
                                user.setTable(row[0])
                                widget.addWidget(user)
                                widget.setCurrentIndex(widget.currentIndex()+3)
                                break
                            else:
                                msg = QtWidgets.QMessageBox()
                                msg.setIcon(QtWidgets.QMessageBox.Warning)
                                msg.setText("Incorrect password!")
                                msg.setWindowTitle("Warning")
                                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                                msg.exec_()
                        else:
                            msg = QtWidgets.QMessageBox()
                            msg.setIcon(QtWidgets.QMessageBox.Warning)
                            msg.setText("Invalid account!")
                            msg.setWindowTitle("Warning")
                            msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                            msg.exec_()
                    except EOFError:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText("Invalid account!")
                        msg.setWindowTitle("Warning")
                        msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                        msg.exec_()
                        break
        
#main
app = QApplication(sys.argv)
signIn = SignIn()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.addWidget(signIn)
widget.setFixedHeight(920)
widget.setFixedWidth(1620)
widget.show()
sys.exit(app.exec_())

