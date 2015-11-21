# -*- coding: utf-8 -*-
from PyQt4.QtSql import *
from PyQt4.QtCore import  Qt, QCoreApplication
from PyQt4.QtGui import QCompleter

QCoreApplication.addLibraryPath("./plugins");


def openDatabase():
    if QSqlDatabase.contains('qt_sql_default_connection'):
        db = QSqlDatabase.database("qt_sql_default_connection")
    else:

        db = QSqlDatabase.addDatabase("QODBC")
        connectionString = "DRIVER={SQL Server};SERVER=172.16.200.3;UID=sa;PWD=gxqsj@12345=;DATABASE=GXSJ_EHR_2;"
        db.setDatabaseName(connectionString)
    
    if(db.open()):
        print u"连接成功！"
        return db
    else:
        print u"连接失败"
    

def readGWLB(combo):
    openDatabase()
    model = QSqlQueryModel()
    model.setQuery("select MC0000,BM0000 from BM_GWLB2 WHERE GRADE = 2")
    model.setHeaderData(0, Qt.Horizontal,u"证件类型名")
    model.setHeaderData(1, Qt.Horizontal,u"编码")
    completer = QCompleter(model)
    combo.clear()
    combo.setModel(model)
    combo.setEditable(True)
    combo.setCompleter(completer)
    #combo.setView(tableView)
    combo.show()

