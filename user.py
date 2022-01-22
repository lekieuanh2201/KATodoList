import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDateTimeEdit, QDialog, QApplication

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
        
        # self.btnEditTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
        #                                 "QPushButton::hover""{" "font-weight:bold; ""}"
        #                                 "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        # self.btnEditTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.btnDeleteTask.setStyleSheet("QPushButton""{""border-radius: 10px; border: 1px solid rgb(0, 85, 127);""}"
                                        "QPushButton::hover""{" "font-weight:bold; ""}"
                                        "QPushButton::pressed" "{" "background-color: #CCE5FF; ""}" )
        self.btnDeleteTask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.listOfTask.setColumnWidth(0, 500)
        self.listOfTask.setColumnWidth(1, 300)
        self.listOfTask.setColumnWidth(2, 220)
        self.listOfTask.setColumnWidth(3, 220)
        self.btnAddTask.clicked.connect(self.addTask)
        self.btnDeleteTask.clicked.connect(self.deleteTask)
        # self.btnSignOut_user.clicked.connect(self.signOut)

    # def signOut(self):
    #     login = SignIn()
    #     widget.removeWidget(self)
    #     widget.addWidget(login)
    #     widget.setCurrentWidget(login)

        
    def addTask(self):
        self.listOfTask.insertRow(self.listOfTask.rowCount())
        for row in range(self.listOfTask.rowCount()):
            chkBoxItem = QtWidgets.QTableWidgetItem("Done")
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
            self.listOfTask.setItem(row, 4, chkBoxItem)

            dateTimeStart= QDateTimeEdit(QtCore.QDateTime.currentDateTime())
            dateTimeStart.setFrame(False)
            dateTimeStart.setDisplayFormat('dd.MM.yyyy - hh:mm')
            self.listOfTask.setCellWidget(row, 2, dateTimeStart)

            dateTimeEnd = QDateTimeEdit(QtCore.QDateTime.currentDateTime())
            dateTimeEnd.setFrame(False)
            dateTimeEnd.setDisplayFormat('dd.MM.yyyy - hh:mm')
            self.listOfTask.setCellWidget(row, 3, dateTimeEnd)
            
            

    def deleteTask(self):
        if self.listOfTask.rowCount()>0:
            currentRow = self.listOfTask.currentRow()
            self.listOfTask.removeRow(currentRow)

        
#test interface display
app = QApplication(sys.argv)
user = User()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('KATodoList')
widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
widget.addWidget(user)
widget.setFixedHeight(920)
widget.setFixedWidth(1620)
widget.show()
sys.exit(app.exec_())
