import requests  # for fetching data from server
from PyQt5 import QtCore  # to create signal of switching for two windows
from PyQt5.QtCore import QCoreApplication  # to assign some data into widgets
from PyQt5.QtWidgets import *  # to inherit qt main window class
from gui import Ui_MainWindow
import config
api_key = config.api_key

base_url = "http://api.openweathermap.org/data/2.5/weather?"


# class for interactive response for weather scraper
class MainWindow(QMainWindow, Ui_MainWindow):
    # creating object for signal of switch window
    switch_window = QtCore.pyqtSignal()

    # constructor for utilizing gui created in gui.py file and onclick action of search button
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # calling function of super class to initiate window gui for weather scrap(this file)
        self.setupUi(self)

        # onclick action for search button which calls search_content function
        self.Search_Button.clicked.connect(self.Search_Whether)

        # giving title to window by assigning value into lable
        self.Title.setText(QCoreApplication.translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Search Weather Here!</span></p></body></html>"))

    # function will be executed to print output when search button is clicked
    def Search_Whether(self):

        # taking name of city textedit box which is entered by user for search
        city_name = self.Search_item.toPlainText()

        # complete url for requesting data from api
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # making a request
        response = requests.get(complete_url)

        # converting received data into a json file
        # it is like a python dictionary, so extracting required data from its
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]  # temperature
            current_pressure = y["pressure"]  # pressure
            current_humidiy = y["humidity"]  # humidity
            feels_like = y["feels_like"]
            windspeed = x["wind"]["speed"]  # windspeed
            z = x["weather"]
            weather_description = z[0]["description"]  # description

            # main string which is to be displayed
            content = (" Place : " +
                       str(city_name.title()) +
                       "\n Temperature : " +
                       str(round(current_temperature-273.15, 2)) + "°C" +
                       "\n Feels like : " +
                       str(round(feels_like - 273.15, 2)) + "°C" +
                       "\n Wind Speed : " +
                       str(windspeed)+" m/s" +
                       "\n Atmospheric Pressure : " +
                       str(current_pressure) + " hPa"
                       "\n Humidity : " +
                       str(current_humidiy) + "%" +
                       "\n Description : " +
                       str(str(weather_description).title()))
        else:
            # when entered city was incorrect
            content = (" No such city, state, country or continent found! Please check for any typos. ")
        self.Output.setText(content)

        # to set scroll bar at the top when first time content is retrieved
        self.Output.verticalScrollBar().setSliderPosition(0)
        self.show()  # display all the content into output box or simple refresh our window

    def weather(self):
        # to switch window
        self.switch_window.emit()
