# -*- coding: utf-8 -*-
from Ui_MainFrame import *
from PyQt4 import QtGui
import loadingData

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    loadingData.readGWLB(ui.comboBox_1)
    loadingData.readGWLB(ui.comboBox_1)
    loadingData.readGWLB(ui.comboBox_2)
    loadingData.readGWLB(ui.comboBox_3)
    loadingData.readGWLB(ui.comboBox_4)
    loadingData.readGWLB(ui.comboBox_5)
    MainWindow.show()
    sys.exit(app.exec_())
