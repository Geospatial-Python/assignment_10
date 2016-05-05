#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This program creates a skeleton of
a classic GUI application with a menubar,
toolbar, statusbar and a central widget.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtWebKit, QtCore
import folium
import os


class View(QtGui.QMainWindow):

    def __init__(self):                 #calling the parent constructor
        super(View, self).__init__()

        self.initUI()


    def initUI(self):

        self.resize(350,250)
        self.center()
        os.makedirs('temp',exist_ok=True) #for saving directory
        #textEdit = QtGui.QTextEdit()         #adding a QTextEdit as the central widget
        self.web_view = QtWebKit.QWebView()
        self.map_dir = 'temp/folium_map.html' #so it knows where to save

        #now embed the folium map
        self.map = folium.Map(location=[-112.323914,-33.29026],zoom_start=10)
        self.map.save(self.map_dir)
        self.web_view.load(QtCore.QUrl(self.map_dir))

        self.setCentralWidget(self.web_view)

        #creates a toolbar to exit, along with adding a keyboard shortcut
        exitAction = QtGui.QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        #added a ready message to the status bar
        self.statusBar().showMessage('Ready')

        #creating the file menu, and adding exit as an option
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        #creating a toolbar with an exit function
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        #setting the window name
        self.setWindowTitle('Assignment 9')
        self.show()

    #making it appear in the center of the screen
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
def main():

    app = QtGui.QApplication(sys.argv)
    ex = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()