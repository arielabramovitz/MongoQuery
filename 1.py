from Connection import *
from MongoDocuments import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 557)
        MainWindow.setMinimumSize(QtCore.QSize(882, 557))
        MainWindow.setMaximumSize(QtCore.QSize(882, 557))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 11, 871, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connect_to_db()
        self.add_rows('Users')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def connect_to_db(self):
        Connection()

    def add_rows(self,coll):
        if coll == 'Users':
            for i in range(len(Connection.get_objects(Connection.current_active, 'UsersInfo', 'Users'))):
                self.tableWidget.insertRow(i)
            for i in MongoDocuments.Users.fields():
                current_column_count = self.tableWidget.columnCount()
                self.tableWidget.insertColumn(current_column_count)
                self.tableWidget.setHorizontalHeaderItem()




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    MainWindow.show()
    sys.exit(app.exec_())
