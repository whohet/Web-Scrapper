# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1291, 757)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(120, 104, 230);\n"
"font: 9pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(1170, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Search_Button.setFont(font)
        self.Search_Button.setStyleSheet("background-color: rgb(239, 251, 255);\n"
"font: 12pt \"Microsoft YaHei\";")
        self.Search_Button.setObjectName("Search_Button")
        self.Output = QtWidgets.QTextBrowser(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(20, 110, 1251, 621))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Output.setFont(font)
        self.Output.setStyleSheet("background-color: rgb(239, 251, 255);\n"
"font: 12pt \"Ebrima\";")
        self.Output.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.Output.setObjectName("Output")
        self.Search_item = QtWidgets.QTextEdit(self.centralwidget)
        self.Search_item.setGeometry(QtCore.QRect(20, 70, 1141, 31))
        self.Search_item.setStyleSheet("background-color: rgb(239, 251, 255);\n"
"font: 9pt \"Arial\";")
        self.Search_item.setObjectName("Search_item")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(20, 29, 1251, 31))
        self.Title.setObjectName("Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scraper"))
        self.Search_Button.setStatusTip(_translate("MainWindow", "Click to search"))
        self.Search_Button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Click</span></p></body></html>"))
        self.Search_Button.setText(_translate("MainWindow", "Search"))
        self.Output.setStatusTip(_translate("MainWindow", "Output of your search"))
        self.Output.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Search Output</span></p></body></html>"))
        self.Search_item.setStatusTip(_translate("MainWindow", "Enter search item"))
        self.Search_item.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Search text</span></p></body></html>"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

