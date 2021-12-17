import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

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
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
app = QApplication(sys.argv)
user = User()
widget = QtWidgets.QStackedWidget()
widget.addWidget(user)
widget.setFixedHeight(590)
widget.setFixedWidth(805)
widget.show()
sys.exit(app.exec_())
