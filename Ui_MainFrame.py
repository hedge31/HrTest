# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\myPython\Test\MainFrame.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(535, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/20151118111705.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.centralWidget.setMaximumSize(QtCore.QSize(600, 400))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 271))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.MainBox = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.MainBox.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.MainBox.setMargin(1)
        self.MainBox.setObjectName(_fromUtf8("MainBox"))
        self.conditionBox1 = QtGui.QHBoxLayout()
        self.conditionBox1.setContentsMargins(-1, -1, -1, 2)
        self.conditionBox1.setObjectName(_fromUtf8("conditionBox1"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.conditionBox1.addItem(spacerItem)
        self.conditionLabel1 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionLabel1.sizePolicy().hasHeightForWidth())
        self.conditionLabel1.setSizePolicy(sizePolicy)
        self.conditionLabel1.setMinimumSize(QtCore.QSize(100, 0))
        self.conditionLabel1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conditionLabel1.setObjectName(_fromUtf8("conditionLabel1"))
        self.conditionBox1.addWidget(self.conditionLabel1)
        self.comboBox_1 = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_1.sizePolicy().hasHeightForWidth())
        self.comboBox_1.setSizePolicy(sizePolicy)
        self.comboBox_1.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_1.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.conditionBox1.addWidget(self.comboBox_1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.conditionBox1.addItem(spacerItem1)
        self.conditionBox1.setStretch(1, 1)
        self.conditionBox1.setStretch(2, 2)
        self.conditionBox1.setStretch(3, 1)
        self.MainBox.addLayout(self.conditionBox1)
        self.conditionBox2 = QtGui.QHBoxLayout()
        self.conditionBox2.setContentsMargins(-1, -1, -1, 2)
        self.conditionBox2.setObjectName(_fromUtf8("conditionBox2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.conditionBox2.addItem(spacerItem2)
        self.conditionLabel2 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionLabel2.sizePolicy().hasHeightForWidth())
        self.conditionLabel2.setSizePolicy(sizePolicy)
        self.conditionLabel2.setMinimumSize(QtCore.QSize(100, 0))
        self.conditionLabel2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conditionLabel2.setObjectName(_fromUtf8("conditionLabel2"))
        self.conditionBox2.addWidget(self.conditionLabel2)
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.conditionBox2.addWidget(self.comboBox_2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.conditionBox2.addItem(spacerItem3)
        self.conditionBox2.setStretch(1, 1)
        self.conditionBox2.setStretch(2, 2)
        self.conditionBox2.setStretch(3, 1)
        self.MainBox.addLayout(self.conditionBox2)
        self.conditionBox3 = QtGui.QHBoxLayout()
        self.conditionBox3.setContentsMargins(-1, -1, -1, 2)
        self.conditionBox3.setObjectName(_fromUtf8("conditionBox3"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.conditionBox3.addItem(spacerItem4)
        self.conditionLabel3 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionLabel3.sizePolicy().hasHeightForWidth())
        self.conditionLabel3.setSizePolicy(sizePolicy)
        self.conditionLabel3.setMinimumSize(QtCore.QSize(100, 0))
        self.conditionLabel3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conditionLabel3.setObjectName(_fromUtf8("conditionLabel3"))
        self.conditionBox3.addWidget(self.conditionLabel3)
        self.comboBox_3 = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.conditionBox3.addWidget(self.comboBox_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.conditionBox3.addItem(spacerItem5)
        self.conditionBox3.setStretch(1, 1)
        self.conditionBox3.setStretch(2, 2)
        self.conditionBox3.setStretch(3, 1)
        self.MainBox.addLayout(self.conditionBox3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.conditionLabel4 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionLabel4.sizePolicy().hasHeightForWidth())
        self.conditionLabel4.setSizePolicy(sizePolicy)
        self.conditionLabel4.setMinimumSize(QtCore.QSize(100, 0))
        self.conditionLabel4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionLabel4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conditionLabel4.setObjectName(_fromUtf8("conditionLabel4"))
        self.horizontalLayout.addWidget(self.conditionLabel4)
        self.comboBox_4 = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.horizontalLayout.addWidget(self.comboBox_4)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.MainBox.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.conditionLabel5 = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conditionLabel5.sizePolicy().hasHeightForWidth())
        self.conditionLabel5.setSizePolicy(sizePolicy)
        self.conditionLabel5.setMinimumSize(QtCore.QSize(100, 0))
        self.conditionLabel5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.conditionLabel5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.conditionLabel5.setObjectName(_fromUtf8("conditionLabel5"))
        self.horizontalLayout_2.addWidget(self.conditionLabel5)
        self.comboBox_5 = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_5.setMaximumSize(QtCore.QSize(400, 16777215))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.horizontalLayout_2.addWidget(self.comboBox_5)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.MainBox.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.QurryButton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QurryButton.sizePolicy().hasHeightForWidth())
        self.QurryButton.setSizePolicy(sizePolicy)
        self.QurryButton.setObjectName(_fromUtf8("QurryButton"))
        self.horizontalLayout_3.addWidget(self.QurryButton)
        self.MainBox.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.MainBox)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "广西区三建员工持证使用情况查询", None))
        self.conditionLabel1.setText(_translate("MainWindow", "证件类型1", None))
        self.conditionLabel2.setText(_translate("MainWindow", "证件类型2", None))
        self.conditionLabel3.setText(_translate("MainWindow", "证件类型3", None))
        self.conditionLabel4.setText(_translate("MainWindow", "证件类型4", None))
        self.conditionLabel5.setText(_translate("MainWindow", "证件类型5", None))
        self.QurryButton.setText(_translate("MainWindow", "查询", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

