import requests
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
from gui import Ui_MainWindow
from bs4 import BeautifulSoup

import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Search_Button.clicked.connect(self.Search_News)
        self.Title.setText(QCoreApplication.translate("MainWindow",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Search News of Any city!</span></p></body></html>"))

    def Search_News(self):
        city = self.Search_item.toPlainText()
        city += '-news'
        url = 'https://www.ndtv.com/' + city
        page = requests.get(url)
        if page.status_code == 404:
            page = requests.get('https://www.ndtv.com/others-news')

        soup = BeautifulSoup(page.content, 'html.parser')

        items = soup.find_all('div', class_='news_Itm')
        self.Output.setText("")
        for news in items:
            heading = news.find('h2', class_='newsHdng')
            if heading != None:
                heading = heading.find('a').text
                self.Output.append("Heading: "+heading.strip()+'\n')

            postedBy = news.find('span', class_='posted-by')
            if postedBy != None:
                postedBy = postedBy.text
                self.Output.append("Posted By:n"+postedBy.strip()+'\n')

            content = news.find('p', class_='newsCont')
            if content != None:
                content = content.text
                self.Output.append("Content: "+content.strip()+'\n')
        self.Output.verticalScrollBar().setSliderPosition(0)
        self.show()

    def News(self):
        self.switch_window.emit()
