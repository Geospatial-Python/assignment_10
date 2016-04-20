import sys
from PyQt4 import QtGui, QtCore, QtWebKit
import folium
import io_geojson
import tweet
import point
import random

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        #textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(textEdit)
        
        map_osm = folium.Map(location=[33.59359997467155, -111.94546800838894])
        map_osm.save(r"./map.html")
        
        
        
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        self.webView = QtWebKit.QWebView()
        self.webView.setHtml(open(r"./map.html").read())
        self.setCentralWidget(self.webView)
        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)    
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exitAction)
        

        toolbar = self.addToolBar('Open')
        toolbar.addAction(openFile)
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Assignment 10')    
        self.show()
        self.webView.show()

    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname == '':
            return
        tweets=io_geojson.read_tweets(fname)
    
        tweets_data=[]
        for i in tweets:
            tweets_data.append(tweet.Tweet(i))
            
        average_lat = 0
        average_lon = 0
        count_tweets = 0
        
        random.seed(1234)
        
        
        
        for i in tweets_data:
            lat, lon = i.gen_point_in_bounds()
            average_lat += lat
            average_lon += lon
            count_tweets += 1
    
        average_lon /= len(tweets_data)
        average_lat /= len(tweets_data)
        map_1 = folium.Map(location=[average_lat, average_lon])
        
        countttz = 0
        for i in tweets_data:
            lat, lon = i.gen_point_in_bounds()
            if countttz < 400:
                #print(i.username)
                folium.Marker([lat, lon], popup = "Test").add_to(map_1)
            countttz+=1
        
        map_1.save(r"./map.html")
        self.webView.setHtml(open("./map.html").read())
        self.webView.show()
        
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()