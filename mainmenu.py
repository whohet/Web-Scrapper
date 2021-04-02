# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
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
        MainWindow.setStyleSheet("background-color: rgb(120, 104, 230);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gfgSearch = QtWidgets.QPushButton(self.centralwidget)
        self.gfgSearch.setGeometry(QtCore.QRect(520, 260, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gfgSearch.setFont(font)
        self.gfgSearch.setStyleSheet("background-color: rgb(239, 251, 255);")
        self.gfgSearch.setObjectName("gfgSearch")
        self.weatherSearch = QtWidgets.QPushButton(self.centralwidget)
        self.weatherSearch.setGeometry(QtCore.QRect(520, 330, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(12)
        self.weatherSearch.setFont(font)
        self.weatherSearch.setStyleSheet("background-color: rgb(239, 251, 255);")
        self.weatherSearch.setObjectName("weatherSearch")
        self.newsSearch = QtWidgets.QPushButton(self.centralwidget)
        self.newsSearch.setGeometry(QtCore.QRect(520, 400, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(12)
        self.newsSearch.setFont(font)
        self.newsSearch.setStyleSheet("background-color: rgb(239, 251, 255);")
        self.newsSearch.setObjectName("newsSearch")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 180, 1291, 51))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"font: 87 18pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 1291, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 610, 1291, 81))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1291, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Scrapper"))
        self.gfgSearch.setText(_translate("MainWindow", "GeeksforGeeks Articles"))
        self.weatherSearch.setText(_translate("MainWindow", "Current Weather"))
        self.newsSearch.setText(_translate("MainWindow", "News"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">What do you want to search?</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Web-Scrapper </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Technologies Used - Python<br/>Libraries Used - BeautifulSoup4, QT5, Requests, Google</span></p><p align=\"center\"><span style=\" font-weight:600;\">APIs Used - OpenWeatherAPI </span></p></body></html>"))

