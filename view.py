#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import folium
import io_geojson
from tweet import *
from point import *
from PyQt4 import QtGui, QtCore, QtWebKit

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        #self.webView = QtWebKit.QWebView()
        #first just show a map without marks in the map
        #the data is the last time i compute the averge of the lat/lon
        map_osm = folium.Map(location=[33.59359997467155,-111.94546800838894])
        map_osm.save(r"./map.html")

        self.webView = QtWebKit.QWebView()
        self.webView.setHtml(open(r"./map.html").read())
        self.setCentralWidget(self.webView)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 750, 650)
        self.setWindowTitle('WebView')
        self.show()
        self.webView.show()
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname == '':
            return 
        tweets=io_geojson.read_tweet_json(fname)

        tweets_data=[]
        for tweet_data in tweets:
            tweets_data.append(io_geojson.ingest_twitter_data(tweet_data))

        self.show_map_into_webview(tweets_data)


    def show_map_into_webview(self,tweets_data):

        #first map tweet class list

        tweets = [Tweet(Point(tweet["point"][0],tweet["point"][1]),tweet["text"],tweet["source"],tweet["id_str"],tweet["lang"],tweet["created_time"]) for tweet in tweets_data]

        #compute the  mean center of the points.
        lat_all=[]
        lon_all=[]
        for tweet in tweets:
            lat_all.append(tweet.get_spatial_information()[0])
            lon_all.append(tweet.get_spatial_information()[1])

        avg_lat=sum(lat_all)/len(lat_all)
        avg_lon=sum(lon_all)/len(lon_all)

        #set a map with the avg_lat,avg_lon
        map_1 = folium.Map(location=[avg_lat, avg_lon])

        #set markers in the map
        for tweet in tweets:
            folium.Marker(list(tweet.get_spatial_information()), popup=tweet.id_str).add_to(map_1)
        map_1.save(r"./map.html")

        #set the webView with the map html
        self.webView.setHtml(open("./map.html").read())
        self.webView.show()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
