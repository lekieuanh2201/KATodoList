import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

class SignIn(QDialog):
    def __init__(self):
        super(SignIn, self).__init__()
        loadUi("ui/signIn.ui", self)
        self.passwordFillIn.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSignUp_In.clicked.connect(self.gotoSignUp)
        self.btnSignIn_In.clicked.connect(self.login)

    def gotoSignUp(self):
        # goto_signUp = SignUp()
        # widget.addWidget(goto_signUp)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def login(self):
        # _login = User()
        # widget.addWidget(_login)
        widget.setCurrentIndex(widget.currentIndex()+2)

class SignUp(QDialog):
    def __init__(self):
        super(SignUp, self).__init__()
        loadUi("ui/signUp.ui", self)
        self.passwordFillUp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verifyPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnSignIn_Up.clicked.connect(self.gotoSignIn)
        self.btnSignUp_Up.clicked.connect(self.login)

    def gotoSignIn(self):
        # goto_signIn = SignIn()
        # widget.addWidget(goto_signIn)
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def login(self):
        # _login = User()
        # widget.addWidget(_login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class User(QDialog):
    def __init__(self):
        super(User, self).__init__()
        loadUi("ui/userInterface.ui", self)
        self.listOfTask.setColumnWidth(0, 300)
        self.listOfTask.setColumnWidth(1, 190)
        self.listOfTask.setColumnWidth(2, 120)
        self.listOfTask.setColumnWidth(3, 90)
        self.btnAddTask.clicked.connect(self.addTask)
        self.btnDeleteTask.clicked.connect(self.deleteTask)
        self.btnSignOut_user.clicked.connect(self.gotoLogin)

    def addTask(self):
        self.listOfTask.insertRow(self.listOfTask.rowCount())

        # create checkbox
        for row in range(self.listOfTask.rowCount()):
            chkBoxItem = QtWidgets.QTableWidgetItem("Done")
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.listOfTask.setItem(row, 3, chkBoxItem)
            
    def deleteTask(self):
        if self.listOfTask.rowCount()>0:
            currentRow = self.listOfTask.currentRow()
            self.listOfTask.removeRow(currentRow)
    
    def gotoLogin(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

#main
app = QApplication(sys.argv)
signIn = SignIn()
signUp = SignUp()
user = User()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.addWidget(signIn)
widget.addWidget(signUp)
widget.addWidget(user)
widget.setFixedHeight(590)
widget.setFixedWidth(805)
widget.show()
sys.exit(app.exec_())
