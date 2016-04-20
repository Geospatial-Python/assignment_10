import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4 import QtCore
from . import io_geojson
from . import twitter
import folium
import random

map_osm = folium.Map(location=[33.4484, -112.0178])

class View(QtGui.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.map = None
        self.web_view = None
        map_osm.save('/tmp/map.html')
        self.init_ui

    def init_ui(self):
        #central widget
        self.web_view = QtWebkit.QWebView()
        self.map = folium.Map(location=[33.4484, -112.0178]
        self.map.zoom_start = 10
        self.map.save(map_osm.save('/tmp/map.html'))
        self.web_view.load
        self.setCentralWidget(self.web_view)

        #Open actions
        open_action = QtGui.QAction(QtGui.QIcon('Open_Folder.ico'), 'Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open)
        
        #Exit actions
        exit_action = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        self.statusBar()

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Title Window')
        self.show()

def open_tweets(self):
    file_name = QfileDialog.getOpenFileName(self, caption='Open File', directory='', filter='*.json')
    if not file_name:
        return
    
    tweets = []
    tmp_tweets = io_geojson.read_twitter(file_name):
        for i in tmp_tweets:
            tweets.append(
                
def show_tweets(self, tweets):
    
    for tweet in tweets:
        lat = 

def main():
    app = QtGui.QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
