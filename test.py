import sys, pickle
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
        signup = SignUp()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def login(self):
        username = self.useNameFill.text()
        password = self.passwordFillIn.text()
        if username == "admin":
            if password == "admin123":
                widget.setCurrentIndex(3)
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
                                widget.setCurrentIndex(widget.currentIndex()+1)
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
    
    def setTable(self, username):
        with open ('data/user.dat', 'rb') as userdata:
            while True:
                row = pickle.load(userdata)
                    # if row[0] == username:
                    #     # set table

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

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi("ui/adminInterface.ui", self)
        self.listOfUser.setColumnWidth(0, 400)
        self.listOfUser.setColumnWidth(1, 300)
        self.btnaddUser.clicked.connect(self.addUser)
        self.btndeleteUser.clicked.connect(self.deleteUser)
        self.btnsignOutAdmin.clicked.connect(self.logout)

    def addUser(self):
        self.listOfUser.insertRow(self.listOfUser.rowCount())

    def deleteUser(self):
        if self.listOfUser.rowCount()>0:
            currentRow = self.listOfUser.currentRow()
            self.listOfUser.removeRow(currentRow)
    def logout(self):
        widget.setCurrentIndex(0)

#main
app = QApplication(sys.argv)
signIn = SignIn()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.addWidget(signIn)
widget.setFixedHeight(590)
widget.setFixedWidth(805)
widget.show()
sys.exit(app.exec_())
