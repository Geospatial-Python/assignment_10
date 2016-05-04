from PyQt4 import QtGui, QtWebKit, QtCore
import os, sys, folium, tweet, io_geojson, random


class View(QtGui.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.map = None
        self.web_view = None
        self.map_dir = 'temp/tweet_map.html'
        self.init_ui()

    def init_ui(self):
    
        #Make Directory for map
        os.makedirs('temp', exist_ok=True)
        self.web_view = QtWebKit.QWebView()
        
        #Set location to sky harbor
        self.map = folium.Map(location=[33.4373, -112.0078])
        
        #zoom out enough to see the entire greater phoenix area
        self.map.zoom_start = 9
        self.map.save('temp/tweet_map.html')
        self.web_view.load(QtCore.QUrl('temp/tweet_map.html'))
        self.setCentralWidget(self.web_view)

        #create a tool bar with the option of opening the Json file
        open_action = QtGui.QAction('Open Json Twitter File', self)
        
        #the action triggered will cause the open function to execute
        open_action.triggered.connect(self.open)
        tool_bar = self.addToolBar('Open')
        tool_bar.addAction(open_action)

        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Arizona Tweet Map')
        self.show()


    def open(self):
        file = QtGui.QFileDialog.getOpenFileName(self, caption='Open Json Twitter File')

        if not file:
            return

        tweets = []
        tweet_data = io_geojson.read_geojson(file)
        for _ in tweet_data:
            tweets.append(tweet.Tweet(_))
        self.show_folium_marks(tweets)

    def show_folium_marks(self, tweets):

        self.map.zoom_start = 9
        
        tweet_lat=0
        tweet_lon=0
        for tweet in tweets:
            tweet_coords = tweet.gen_rand_pt()
            tweet_lat+=tweet_coords.getx()
            tweet_lon+=tweet_coords.gety()
            folium.Marker([tweet_coords.getx(), tweet_coords.gety()]).add_to(self.map)
        
        #make sure to recenter the map to the average of the tweet coordinates
        self.map.location=[tweet_lat/len(tweets),tweet_lon/len(tweets)]
        #self.map = folium.Map([tweet_lat/len(tweets),tweet_lon/len(tweets)])
        self.map.save('temp/tweet_map.html')
        self.web_view.load(QtCore.QUrl('temp/tweet_map.html'))

def main():
    app = QtGui.QApplication(sys.argv)
    view=View()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
