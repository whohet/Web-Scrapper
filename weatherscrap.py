import requests
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
import config
api_key = config.api_key

base_url = "http://api.openweathermap.org/data/2.5/weather?"

class MainWindow(QMainWindow, Ui_MainWindow):
    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Search_Button.clicked.connect(self.Search_Whether)
        self.Title.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Search Weather Here!</span></p></body></html>"))

    def Search_Whether(self):
        city_name = self.Search_item.toPlainText()

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            feels_like = y["feels_like"]
            windspeed=x["wind"]["speed"]
            z = x["weather"]
            weather_description = z[0]["description"]
            content=(" Place : " +
                  city_name+
                  "\n Temperature : " +
                  str(round(current_temperature-273.15,2)) +"°C"+
                     "\n Feels like : " +
                     str(round(feels_like - 273.15,2)) + "°C"+
                     "\n Wind Speed : " +
                    str(windspeed)+" m/s"+
                  "\n Atmospheric Pressure : " +
                  str(current_pressure) +" hPa"
                  "\n Humidity : " +
                  str(current_humidiy) +"%"+
                  "\n Description : " +
                  str(weather_description))
        else:
            content=(" City Not Found. Please check for any typos. ")
        self.Output.setText(content)
        self.Output.verticalScrollBar().setSliderPosition(0)
        self.show()

    def weather(self):
        self.switch_window.emit()