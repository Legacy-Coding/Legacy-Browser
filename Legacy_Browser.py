"""
I have made a simple browser using PyQt5 module it doesnot have unique features but have all the basics features.
If any problem in installation of module then please read Readme.md file .
"""
#module required
import sys
from PyQt5.QtCore import *  #pip install PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebKitWidgets import *

import os

#basic web browser setting
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #setting information of Developer
        # self.show()
        # self.setWindowIcon(QIcon=os.path.join('icons', 'logo.jfif'))
        # self.setWindowTitle("Abhinav Kumar")

        # navbar


        # self.setWindowTitle("Abhinav kumar")
        self.setWindowIcon(QIcon(os.path.join('icons', 'logo.jfif')))
        self.show()
        navbar = QToolBar()
        self.addToolBar(navbar)



        #backward button
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        #forward button
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        #reload button
        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        #home button
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        #fixing back button or forward not showing real url
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    #setting url for home
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://github.com/Legacy-Coding'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    #setting function for #fixing back button or forward not showing real url
    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Finidh setting up the browser
app = QApplication(sys.argv)
QApplication.setApplicationName('Legacy Browser')
QApplication.setOrganizationName("Abhinav Kumar")

window = MainWindow()
app.exec_()