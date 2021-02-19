# Abhinav Kumar

# Legacy-Browser
I have created an awesome browser for internet surfing with Python

#intoduction of myself
I am Abhinav Kumar from India and I am in class 7th ICSE Board Student. I am learning python for unbelieveable projects and increasing my capacity.

# Introduction of Legacy-Browser
This is a fully functional internet surfing browser programmed using python.
You can surf internet and search any things in internet.
I have used search Engine as Google but, if you want you can change

# Features
It has many basic features as:
*It has default and beatuifull search engine in front of the browser
*You can search any url as search bar is given there.
* It has forward button . So, you can open the previous opened tabs. 
* It has backward button . So, you can open the previous opened tabs. 
* It has reload button . So, you can reloas tabs. 
* It has Home button . So, you can directly go to the Home tab. 

# module Required

# import sys
# from PyQt5.QtCore import *  #pip install PyQt5
# from PyQt5.QtWidgets import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtGui import *
  
  # installation of module
pip install PyQt5




# How to fix # ModuleNotFoundError: No module named 'PyQt5.QtWebEngineWidgets'
It has been moved to a separated package.

Based on this answer and my own experience, Just execute in a terminal:

pip install PyQtWebEngine
If you still got problems with PyQt, try uninstalling all of the PyQt related libraries:

pip uninstall PyQt5
pip uninstall PyQt5-sip
pip uninstall PyQtWebEngine
Then install them again, which should fix the following errors:

ModuleNotFoundError: No module named 'PyQt5.sip'
ModuleNotFoundError: No module named 'PyQt5.QtWebEngineWidgets'

# How to make this browser Legacy-Browser.py  to Legacy-Browser.exe
*First of all, Yoy required a module named pyinstaller.
*then open you Powershell or CMD then write # Pyinstaller Legacy-Browser.py 
*Thats all your Browser is converte to .exe 
Now , Go to the dist and click .exe file Your Browser will open
* You can also bind it in a single file and set an icon also.

# creadits
I am very thankfull of the module Develoer of PyQt5.

# Thanks
Thank you for visiting my profile and for watching my repository .
Please follow me and support me.

# Update the browser
I request you that if you have developed the browser better than mine .
Then please pull request or send me you repository link because that is the way to become Great Programmer.
