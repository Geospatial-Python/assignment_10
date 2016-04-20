from PyQt5 import QtCore, QtWidgets, QtWebKitWidgets
import sys
import folium
import io_geojson
import Tweet
import random


phx_coords = [33.441957, -112.072913]

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(434, 316)

        self.map = folium.Map(location=phx_coords)
        self.map.zoom_start = 8
        self.mapFile = "osm_map.html"
        self.map.save(self.mapFile)

        self.setupUi()

    def setupUi(self):

        self.setupMenuBar()
        self.setupStatusBar()


        # place widgets here
        self.webView = QtWebKitWidgets.QWebView(MainWindow)
        self.webView.setHtml(open(self.mapFile,'r').read())



        self.MainWindow.setCentralWidget(self.webView)

    def setupMenuBar(self):

        # Exit
        exitAction = QtWidgets.QAction(self.MainWindow)
        exitAction.setText('Exit')
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(QtWidgets.qApp.quit)

        # Open
        openAction = QtWidgets.QAction(self.MainWindow)
        openAction.setText('Open')
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a tweet .json file')
        openAction.triggered.connect(self.openJFile)

        menubar = QtWidgets.QMenuBar(self.MainWindow)
        menuFile = QtWidgets.QMenu(menubar)
        menuFile.setTitle('File')
        self.MainWindow.setMenuBar(menubar)

        menuFile.addAction(exitAction)
        menuFile.addAction(openAction)
        menubar.addAction(menuFile.menuAction())

    def setupStatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.MainWindow.setStatusBar(self.statusbar)

    def openJFile(self):
        try:
            jfile = QtWidgets.QFileDialog.getOpenFileName(parent=MainWindow, caption='Open a tweet .json file',filter='*.json')[0]

        except:
            return

        self.processTweetFile(jfile)

    def processTweetFile(self, jfile):
        tweetObjs = []
        tweets = io_geojson.processTweets(jfile)
        for t in tweets:
            tweetObjs.append(Tweet.Tweet(t))

        random.seed(1212)

        # create new map for new file
        self.map = folium.Map(location=phx_coords)
        self.map.zoom_start = 8

        for tw in tweetObjs:
            latitude, longitude = tw.getRandPointInBoundingBox()
            folium.Marker([latitude, longitude], popup=tw.twScreenName).add_to(self.map)

        self.map.save(self.mapFile)
        self.webView.setHtml(open(self.mapFile,'r').read())




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
