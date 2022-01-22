import os
import sys, pickle
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QCheckBox, QDialog, QApplication

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
        signup = SignUp()
        widget.addWidget(signup)
        widget.removeWidget(self)
        widget.setCurrentWidget(signup)

    def login(self):
        username = self.useNameFill.text()
        password = self.passwordFillIn.text()

        if username == "admin":
            if password == "admin123":
                admin = Admin()
                widget.addWidget(admin)
                widget.removeWidget(self)
                widget.setCurrentWidget(admin)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Incorrect password!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()
        else:
            if os.path.getsize('data/user.dat') == 0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Account does not exist!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()

            else:
                userdata = open('data/user.dat','rb')
                users = pickle.load(userdata)
                userdata.close()
                if username in users.keys():
                    if password != users[username]:
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Warning)
                        msg.setText("Incorrect password!")
                        msg.setWindowTitle("Warning")
                        msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                        msg.exec_()
                    else:
                        user = User()
                        widget.removeWidget(self)
                        widget.addWidget(user)
                        widget.setCurrentWidget(user)
                        user.setupTable(username)
                else: 
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Account does not exist!")
                    msg.setWindowTitle("Warning")
                    msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                    msg.exec_()
                                        
class SignUp(QDialog):
    def __init__(self):
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
        self.btnSignUp_Up.clicked.connect(self.createAccount)

    def gotoSignIn(self):
        goto_signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(goto_signIn)
        widget.setCurrentWidget(goto_signIn)
    
    def createAccount(self):
        userName = self.useNameFill.text()
        password = self.passwordFillUp.text()
        verifyPass = self.verifyPassword.text()
        if userName == 'admin':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Existed account!")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
            msg.exec_()
        if os.path.getsize('data/user.dat') == 0:
            userdata = open('data/user.dat','wb')
            users = dict()
            if password != verifyPass:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Verify Password is incorrect!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()

            elif password == verifyPass:
                users[userName]= password
                pickle.dump(users, userdata)
                userdata.close()
                signin = SignIn()
                widget.removeWidget(self)
                widget.addWidget(signin)
                widget.setCurrentWidget(signin)

        else: 
            userdata = open('data/user.dat','rb+')
            users = pickle.load(userdata)
            print(users)
          
            if userName in users.keys():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("Username existed!")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                msg.exec_()
            else:
                if password != verifyPass:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("Verify Password is incorrect!")
                    msg.setWindowTitle("Warning")
                    msg.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
                    msg.exec_()

                elif password == verifyPass:
                    users[userName]= password
                    print(users)
                    userdata.seek(0)
                    userdata.truncate()
                    pickle.dump(users, userdata)
                    userdata.close()
                    signin = SignIn()
                    widget.removeWidget(self)
                    widget.addWidget(signin)
                    widget.setCurrentWidget(signin)

class User(QDialog):
    def __init__(self):
        super(User, self).__init__()
        loadUi("ui/userInterface.ui", self)

        self.btnSignOut_user.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnSignOut_user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnSaveAll.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnSaveAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnAddTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnAddTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnDeleteTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnDeleteTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.listOfTask.setColumnWidth(0, 550)
        self.listOfTask.setColumnWidth(1, 350)
        self.listOfTask.setColumnWidth(2, 220)
        self.listOfTask.setColumnWidth(3, 220)
        self.btnAddTask.clicked.connect(self.addTask)
        self.btnDeleteTask.clicked.connect(self.deleteTask)
        self.btnSignOut_user.clicked.connect(self.gotoLogin)
        self.btnSaveAll.clicked.connect(self.saveAll)
    
    def setupTable(self, username):
        self.uName = username
        if os.path.getsize('data/task.dat') != 0:
            taskFile = open('data/task.dat', 'rb')
            tasks = pickle.load(taskFile)
            taskFile.close()
            if username in tasks.keys():
                for row in range(len(tasks[username])):
                    task = QtWidgets.QTableWidgetItem(tasks[username][row]['task'])
                    address = QtWidgets.QTableWidgetItem(tasks[username][row]['address'])
                    timeStart = QtWidgets.QTableWidgetItem(tasks[username][row]['time'])
                    timeEnd = QtWidgets.QTableWidgetItem(tasks[username][row]['time'])
                    chkBoxItem = QCheckBox('Done')
                    if not tasks[username][row]['done'] :
                        chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    else:
                        chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    self.listOfTask.insertRow(self.listOfTask.rowCount())
                    self.listOfTask.setItem(row, 0, task)
                    self.listOfTask.setItem(row, 1, address)
                    self.listOfTask.setItem(row, 2, timeStart)
                    self.listOfTask.setItem(row, 3, timeEnd)
                    self.listOfTask.setCellWidget(row, 4, chkBoxItem)

    def saveAll(self):
        if os.path.getsize('data/task.dat') != 0:
            taskfile = open('data/task.dat','rb+')
            tasks = pickle.load(taskfile)
            taskfile.seek(0)
            taskfile.truncate()
            taskfile.close()
            for row in range(self.listOfTask.rowCount()):
                # tk=self.listOfTask.item(row,1).text()
                tasks[self.uName][row]=dict()
                tasks[self.uName][row]['task']=self.listOfTask.item(row,0).text()
                tasks[self.uName][row]['address']=self.listOfTask.item(row,1).text()
                tasks[self.uName][row]['time']=self.listOfTask.item(row,2).text()
                if self.listOfTask.cellWidget(row,3).isChecked():
                    tasks[self.uName][row]['done']= True
                else:  tasks[self.uName][row]['done']= False
                print(self.listOfTask.item(row,0).text())
            file = open('data/task.dat','wb')
            pickle.dump(tasks, file)
            file.close()
        else:
            tasksDict = dict()
            tasksDict[self.uName]=dict()
            for row in range(self.listOfTask.rowCount()):
                tasksDict[self.uName][row]=dict()
                tasksDict[self.uName][row]['task']=self.listOfTask.item(row,0).text()
                tasksDict[self.uName][row]['address']=self.listOfTask.item(row,1).text()
                print(self.listOfTask.cellWidget(row,3).isChecked())
                tasksDict[self.uName][row]['time']=self.listOfTask.item(row,2).text()
                    
                if self.listOfTask.cellWidget(row,3).isChecked():
                    tasksDict[self.uName][row]['done']= True
                else:  tasksDict[self.uName][row]['done']= False
                    
            fileTasks = open('data/task.dat', 'wb')
            pickle.dump(tasksDict, fileTasks)
            fileTasks.close()
        
    def addTask(self):
        self.listOfTask.insertRow(self.listOfTask.rowCount())
        row = self.listOfTask.rowCount()-1
        chkBoxItem = QCheckBox('Done')
        chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
        self.listOfTask.setCellWidget(row, 3, chkBoxItem)

        dateTimeStart=QtWidgets.QTableWidgetItem(QtCore.QDateTime.currentDateTime().toString('dd.MM.yyyy - hh:mm'))
        self.listOfTask.setItem(row, 2, dateTimeStart)
        dateTimeEnd=QtWidgets.QTableWidgetItem(QtCore.QDateTime.currentDateTime().toString('dd.MM.yyyy - hh:mm'))
        self.listOfTask.setItem(row, 3, dateTimeEnd)

    def deleteTask(self):
        if self.listOfTask.rowCount()>0:
            currentRow = self.listOfTask.currentRow()
            self.listOfTask.removeRow(currentRow)

    
    def gotoLogin(self):
        signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(signIn)
        widget.setCurrentWidget(signIn)

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi("ui/adminInterface.ui", self)
        self.btnsignOutAdmin.setStyleSheet("QPushButton""{""color: #fff; background-color: rgb(0, 85, 127);border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #fff; color: rgb(0, 85, 127)""}" )
        self.btnsignOutAdmin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.btnaddUser.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnaddUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnsaveUser.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnsaveUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btndeleteUser.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btndeleteUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.listOfUser.setColumnWidth(0, 720)
        self.listOfUser.setColumnWidth(1, 650)
        self.btnaddUser.clicked.connect(self.addUser)
        self.btndeleteUser.clicked.connect(self.deleteUser)
        self.btnsaveUser.clicked.connect(self.saveAll)
        self.btnsignOutAdmin.clicked.connect(self.logout)
        self.setUpTable()

    def setUpTable(self):
        fileUser = open ('data/user.dat', 'rb')
        users = pickle.load(fileUser)
        row = 0
        for user in users.keys():
            username = QtWidgets.QTableWidgetItem(user)
            password = QtWidgets.QTableWidgetItem(users[user])
            self.listOfUser.insertRow(self.listOfUser.rowCount())
            self.listOfUser.setItem(row, 0, username)
            self.listOfUser.setItem(row, 1, password)
            row += 1
        fileUser.close()


    def addUser(self):
        self.listOfUser.insertRow(self.listOfUser.rowCount())

    def deleteUser(self):
        if self.listOfUser.rowCount()>0:
            currentRow = self.listOfUser.currentRow()
            self.listOfUser.removeRow(currentRow)

    def saveAll(self):
        users = dict()
        for row in range(self.listOfUser.rowCount()):
            userName = self.listOfUser.item(row, 0).text()
            password = self.listOfUser.item(row, 1).text()
            users[userName]=password
        fileUser = open('data/user.dat','wb')
        pickle.dump(users,fileUser)
        fileUser.close()

    def logout(self):
        signIn = SignIn()
        widget.removeWidget(self)
        widget.addWidget(signIn)
        widget.setCurrentWidget(signIn)
        
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
