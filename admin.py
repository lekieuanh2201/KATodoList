import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication

class Admin(QDialog):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi("ui/adminInterface.ui", self)
        self.listOfUser.setColumnWidth(0, 400)
        self.listOfUser.setColumnWidth(1, 300)
        self.btnaddUser.clicked.connect(self.addUser)
        self.btndeleteUser.clicked.connect(self.deleteUser)

    def addUser(self):
        self.listOfUser.insertRow(self.listOfUser.rowCount())

    def deleteUser(self):
        if self.listOfUser.rowCount()>0:
            currentRow = self.listOfUser.currentRow()
            self.listOfUser.removeRow(currentRow)

# app = QApplication(sys.argv)
# admin = Admin()
# widget = QtWidgets.QStackedWidget()
# widget.setWindowTitle('KATodoList')
# widget.setWindowIcon(QtGui.QIcon('img/AppIcon.png'))
# widget.addWidget(admin)
# widget.setFixedHeight(590)
# widget.setFixedWidth(805)
# widget.show()
# sys.exit(app.exec_())
