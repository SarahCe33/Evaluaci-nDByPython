# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\EvaluacionAna.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.Qt import QSqlDatabase
import sqlite3
from pprint import pprint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(120, 10, 900, 331))
        self.tableView.setObjectName("tableView")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 101, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_viewdata = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_viewdata.setObjectName("pushButton_viewdata")
        self.verticalLayout.addWidget(self.pushButton_viewdata)
        self.pushButton_addRow = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.verticalLayout.addWidget(self.pushButton_addRow)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.verticalLayout.addWidget(self.pushButton_deleteRow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #------------------Create DB-----------------
        self.create_DB()
        self.pushButton_viewdata.clicked.connect(self.print_data)
        self.model = None
        self.pushButton_viewdata.clicked.connect(self.sql_table_view_model)
        self.pushButton_addRow.clicked.connect(self.sql_add_row)
        self.pushButton_deleteRow.clicked.connect(self.sql_delete_row)



    def sql_delete_row(self):
            if self.model:
                self.model.removeRow(self.tableView.currentIndex().row())
            else:
                self.sql_tableview_model
       
            
    def sql_add_row(self):
            if self.model:
                self.model.insertRows(self.model.rowCount(),1)
            else:
                self.sql_tableview_model()
        
                 
    def sql_table_view_model(self):
       
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('TRACKS.db')
            
            tableview=self.tableView
            self.model= QtSql.QSqlTableModel()
            tableview.setModel(self.model)
            
            self.model.setTable('TRACK')
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "TrackId")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "AlbumId")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "MediaTypeId")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "GenreId")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Composer")
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Milliseconds")
            self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Bytes")
            self.model.setHeaderData(8, QtCore.Qt.Horizontal, "UnitPrice")

                
    def print_data(self):
            sqlite_file='TRACKS.db'
            conn=sqlite3.connect(sqlite_file)
            cursor= conn.cursor()
            
            cursor.execute("SELECT * FROM 'TRACK' ORDER BY TrackId")
            all_rows = cursor.fetchall()
            pprint(all_rows)
            
            conn.commit()
            conn.close()
            
        
            
        
        
    def create_DB(self):
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('TRACKS.db')
            db.open() 
            
            query = QtSql.QSqlQuery() 
            
            query.exec_("create table TRACK(TrackId int primary key, Name varchar(20), AlbumId int(8), MediaTypeId int(8), GenreId int(8), Composer varchar(20), Milliseconds int(6), Bytes int(5), UnitePrice float(5))")
            query.exec_("insert into TRACK values(1000, 'Red point', '2010', '4514', '1414', 'Teen Top', '12010', '24', '205.69')")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_viewdata.setText(_translate("MainWindow", "View Data"))
        self.pushButton_addRow.setText(_translate("MainWindow", "Add Row"))
        self.pushButton_deleteRow.setText(_translate("MainWindow", "Delete Row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
