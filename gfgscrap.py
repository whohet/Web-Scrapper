import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
from gui import Ui_MainWindow
import requests
from bs4 import BeautifulSoup
from googlesearch import search


class MainWindow(QMainWindow, Ui_MainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Search_Button.clicked.connect(self.Search_content)
        self.Title.setText(QCoreApplication.translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Search Any GFG Article Here!</span></p></body></html>"))

    def Search_content(self):
        try:
            search_topic = self.Search_item.toPlainText()
            res = list(search(search_topic + " gfg", tld="co.in", num=5, stop=5, pause=2))
            flag = False
            i = 0
            for url in res:
                if flag:
                    break

                if url.split('/')[2] == 'www.geeksforgeeks.org':

                    flag = True
                    page = requests.get(url)
                    soup = BeautifulSoup(page.content, 'html.parser')

                    title = soup.find('div', class_='title').text.strip()
                    status = soup.find('div', class_='media')

                    # This while to handle main page different style
                    if status is None:
                        content = soup.find('div', class_='entry-content').text.split('\n')
                        stringappend = ''
                        for c in content:
                            if len(c) == 0:
                                continue
                            stringappend = stringappend + '\n' + c
                        self.Output.setText(stringappend)

                    else:
                        status = status.text.split('\n')

                        st = "Title: " + title + '<br /><br />'
                        st += "Article Status: <br />"

                        for s in status:
                            if len(s) == 0:
                                continue
                            st += s + '<br />'

                        content = soup.find('div', class_='article--viewer_content')
                        content_img = content.find('div', class_='text')

                        index_of_images = list()
                        index_of_images_after = list()
                        image_names = list()
                        contents = "start_offf!!!!"
                        p=1
                        for c in content_img:
                            if (c.find('img') is not None) and (c.find('img') != -1):
                                index_of_images.append(contents)
                                response = requests.get(c.img['src'])
                                name='image'+str(len(image_names))
                                file = open(name, "wb")
                                file.write(response.content)
                                file.close()
                                image_names.append(name)
                                p=0
                            else:
                                for lines in str(c).splitlines():
                                    try:
                                        start = lines.index(">")
                                        end = lines.index('<', start)
                                    except:
                                        continue
                                    start += 1
                                    contentsv = lines[start:end]
                                    if contentsv != "":
                                        contents = contentsv
                                    if p==0:
                                        p=1
                                        index_of_images_after.append(contents)

                        content = content_img.text.split('\n')
                        st += "<br />Content: <br />"

                        img_url = 0

                        while img_url < len(index_of_images) and index_of_images[img_url] == "start_offf!!!!":
                            st += "<br /><img src=\"{}\"/><br /><br />".format(image_names[img_url])
                            img_url += 1

                        for c in content:
                            if len(c) == 0 or c.startswith('Attention') or c == '\n':
                                continue
                            elif c.startswith('arrow_drop') or c.startswith('Save') or c.startswith('My'):
                                continue
                            elif c.startswith('This blog is contributed') or c.startswith('Please write'):
                                continue
                            elif c.startswith('To begin with, your interview') or c.startswith('Recent'):
                                continue
                            elif c.startswith('This article is contributed') or c.startswith('Please comment'):
                                continue

                            if img_url < len(index_of_images) and index_of_images_after[img_url] in c and len(c.strip()) != 0:
                                st += ("<br /><img src=\"{}\"><br /><br />".format(image_names[img_url]))+ c + "<br />"
                                img_url += 1
                                continue

                            st += c + "<br />"


                            if img_url < len(index_of_images) and index_of_images[img_url] in c and len(c.strip()) != 0:
                                st += ("<br /><img src=\"{}\"><br /><br />".format(image_names[img_url]))
                                img_url += 1
                                continue
                        while img_url<len(index_of_images):
                            st += ("<br /><img src=\"{}\"><br /><br />".format(image_names[img_url]))
                            img_url += 1
                        st+="<br /><br /><br />"
                        self.Output.setHtml(st)
                        for i in image_names:
                            os.remove(i)

            if flag == False:
                error = "No GeeksForGeeks Article Found!\nWe see you are not searching for something that belongs to computer science.\n\n\n"
                self.Output.setText(error)
            self.Output.append('\n\n\n')
        except:
            self.Output.setText("We encountered an error. Sorry.\n Please try again after some time.")
        self.Output.verticalScrollBar().setSliderPosition(0)
        self.show()

    def gfg(self):
        self.switch_window.emit()