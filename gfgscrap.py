import os                            # to manage files into system
from PyQt5.QtWidgets import *        #to inherit qt main window class
from PyQt5 import QtCore             #to create signal of switching for two windows
from PyQt5.QtCore import QCoreApplication #to assign some data into widgets
from gui import Ui_MainWindow        #import file gui to use created gui window
import requests                      #for fetching data from server
from bs4 import BeautifulSoup        #for extracting data from page
from googlesearch import search      #to use result of google search for finding website
import threading                     #to create threads for handling image loading
import time                          
import sys
# class for interactive response for gfg scraper
class MainWindow(QMainWindow, Ui_MainWindow):

    switch_window = QtCore.pyqtSignal()         #creating object for signal of switch window
    # constructor for utilizing gui created in gui.py file and onclick action of search button
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)   #calling function of super class to initiate window gui for gfgscrap(this file)

        # onclick action for search button which calls search_content function
        self.Search_Button.clicked.connect(self.Search_content)

        # giving title to window by assigning value into lable
        self.Title.setText(QCoreApplication.translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Search Any GFG Article Here!</span></p></body></html>"))

        self.thread=threading.Thread(target=self.backgroundImageDelete, args=())#new thread for deleting images that are fetched during scraping
        self.imglist=[]#list to store urls of images
        self.thread.daemon = True
        self.newSearchStart=False#varible to tell thread whether a new search query is initiated or not
        self.thread.start()#starting thread
    # function will be executed to print output when search button is clicked
    def Search_content(self):
        try:                 #try block to handle server problems
            print("Printing in console is meant for debugging/tracking the process of threads only. So please ignore the prints below")
            # taking value of textedit box which is entered by user for search
            search_topic = self.Search_item.toPlainText()

            # searching for the related site by the use of google and fetching first five results
            res = list(search(search_topic + " gfg", tld="co.in", num=5, stop=5, pause=2))
            flag = False
            i = 0
            for url in res:    #loop to find result related to gfg frm urls of top five google search
                if flag:
                    break      #if scrap on website done than break the loop

                if url.split('/')[2] == 'www.geeksforgeeks.org':   #if gfg url found

                    flag = True
                    page = requests.get(url)     #request for page of gfg by request method
                    soup = BeautifulSoup(page.content, 'html.parser')   #taking data of source code of gfg page
                    content = soup.find('div', class_='article--viewer_content')  #for content fetch
                    if (content==None):
                        content = soup.find('div', class_='entry-content').prettify()#arranging data
                        carr=content.splitlines()
                        mainc=""
                        #print(carr)
                        for i in range(len(carr)):#going through each tag
                            string=carr[i]
                            if(string==None):
                                continue
                            if(string.find('<img')!=-1):#incase we get an image
                                string=string + '<\\img>'
                                #print(string+'hello')
                                stmp=BeautifulSoup(string,'html.parser')#coverting to bs4 object
                                response = requests.get(stmp.img['src'])#fetching main source/url of image
                                name='image'+str(i)#setting up local name for image
                                self.imglist.append(name)#storing local name in list
                                file = open(name, "wb")
                                file.write(response.content)  # downloading image into system
                                file.close()
                                carr[i]='<br/><img src=\"'+name+'\">'#setting up html code
                                #in case of spams/not fruitful content which appers at end of document hence breaking
                            elif(string.find('My Personal')!=-1):
                                break
                            elif(string.find('This blog is contributed')!=-1):
                                break
                            elif(string.find('To begin with, your interview')!=-1):
                                break
                            elif(string.find('Attention')!=-1):
                                break
                            elif(string.find('This article is contributed')!=-1):
                                break
                            elif(string.find('Please comment')!=-1):
                                break
                            elif(string.find('Please write')!=-1):
                                break
                            elif(string.find('arrow_drop')!=-1):
                                break
                            elif(string.find('Save')!=-1):
                                break
                            mainc=mainc + carr[i]
                        

                        self.Output.setHtml(mainc) #viewing the content in our gui
                        print('done')#for console
                        self.Output.setOpenExternalLinks(True)#on click on links go to web browser
                        self.newSearchStart=True#as new search was initiated now its time to deleted image file fectched to local system
                    else :
                        #get title of article
                        title=content.find('div',class_='title').prettify()
                        mainc=title
                        #get status of article-difficulty,updateion publition etc
                        status=content.find('div',class_='media').prettify()
                        mainc=mainc+status
                        #get content
                        content = content.find('div', class_='text').prettify()
                        #slipt content into different lines so that we could traverse and get fruitful content
                        carr=content.splitlines()
                        #print(carr)
                        for i in range(len(carr)):
                            string=carr[i]
                            if(string==None):
                                continue
                            if(string.find('<br')!=-1):
                                continue
                            #in case of image
                            if(string.find('<img')!=-1):
                                string=string + '<\\img>'
                                #print(string+'hello')
                                stmp=BeautifulSoup(string,'html.parser')#convert to bs4 object
                                response = requests.get(stmp.img['src'])#get main url to image
                                name='image'+str(i)#set local copy name
                                self.imglist.append(name)#append name 
                                file = open(name, "wb")
                                file.write(response.content)  # downloading image into system
                                file.close()
                                carr[i]='<br/><img src=\"'+name+'\">'#set up code for new image
                                #print(carr[i])
                            #spams ignored (not fruitful content now availble hence break)
                            elif(string.find('My Personal')!=-1):
                                break
                            elif(string.find('This blog is contributed')!=-1):
                                break
                            elif(string.find('To begin with, your interview')!=-1):
                                break
                            elif(string.find('Attention')!=-1):
                                break
                            elif(string.find('This article is contributed')!=-1):
                                break
                            elif(string.find('Please comment')!=-1):
                                break
                            elif(string.find('Please write')!=-1):
                                break
                            elif(string.find('arrow_drop')!=-1):
                                break
                            elif(string.find('Save')!=-1):
                                break
                            mainc=mainc + carr[i]
                        
                        #display the content gui
                        self.Output.setHtml(mainc)
                        print('done')#for console
                        self.Output.setOpenExternalLinks(True)#open links in ext. web browser
                        self.newSearchStart=True#tell backgroun thread to start deletion process
            if flag == False:  #if searched content not found on gfg
                error = "No GeeksForGeeks Article Found!\nWe see you are not searching for something that belongs to computer science.\n\n\n"
                self.Output.setText(error)
            self.Output.append('\n\n\n')
        except Exception as e:
            print(e)
            # set value of output box as error message if some issue related to server or content found
            self.Output.setText("We encountered an error. Sorry.\n Please try again after some time.")
        # to set scroll bar at the top when first time content is retrieved
        self.Output.verticalScrollBar().setSliderPosition(0)

        self.show()  #display all the content into output box or simple refresh our window

    def gfg(self):
        self.switch_window.emit()  # to switch window

    #function to delete images in background without intruppting gui and main function
    def backgroundImageDelete(self):
        while (True):
            if(self.newSearchStart==True):#signal passed that new search was initiated
                if(len(self.imglist)==0):#no images feteched
                    self.newSearchStart=False#signal converted to null as task is done
                else : 
                    time.sleep(5)#let thread sleep and give the time to main function to let the images display as i/o is slow
                    for i in self.imglist:
                        time.sleep(1)#in every one second delted one image(time is given as io is slow and images may be left to display)
                        os.remove(i)#remove file
                        print(f"Deleted {i}")
                    self.imglist=[]
                    self.newSearchStart=False#set signal to null as task is done