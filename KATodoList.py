import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication
from signIn import SignIn
from signUp import SignUp
from admin import Admin
from user import User

#function
def login():
    username = signIn.useNameFill.text()
    password = signIn.passwordFillIn.text()    
    if username == "admin":
        if password == "admin123":
            widget.setCurrentIndex(3)
        else:
            widget.setCurrentIndex(2)
    else:
        widget.setCurrentIndex(1)


#sign in interface
signIn = SignIn()
widget = QtWidgets.QStackedWidget()
widget.addWidget(signIn)
signIn.btnSignIn_In.clicked.connect(login)

#sign up interface
signUp = SignUp()
widget.addWidget(signUp)

#user interface
user = User()
widget.addWidget(user)

#admin interface
admin = Admin()
widget.addWidget(admin)

#main
app = QApplication(sys.argv)
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.setFixedHeight(590)
widget.setFixedWidth(805)
widget.show()
sys.exit(app.exec_())
