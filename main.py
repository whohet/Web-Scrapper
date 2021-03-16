from PyQt5 import QtCore
from mainmenu import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys
import gfgscrap
import newsscrap
import weatherscrap

class MainWindow(QMainWindow, Ui_MainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.gfgSearch.clicked.connect(self.gfgWindow)
        self.weatherSearch.clicked.connect(self.weatherWindow)
        self.newsSearch.clicked.connect(self.newsWindow)

    def gfgWindow(self):
        self.gfg=gfgscrap.MainWindow()
        self.gfg.show()

    def weatherWindow(self):
        self.weather=weatherscrap.MainWindow()
        self.weather.show()

    def newsWindow(self):
        self.news=newsscrap.MainWindow()
        self.news.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())