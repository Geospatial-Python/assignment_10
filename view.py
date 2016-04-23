import sys
from PyQt4 import QtGui, QtCore, QtWebKit
import tweet
import folium
import io_geojson
from nose.tools import set_trace

class View(QtGui.QMainWindow):

	def __init__(self):

		super(View, self).__init__()
		self.initUI()

	def initUI(self):

		map_ = folium.Map(location=[33.4484, -112.0740])
		map_.save(r"./index.html")

		exit = QtGui.QAction(QtGui.QIcon('exit.png'), 'Quit', self)
		exit.setStatusTip('Exit')
		exit.triggered.connect(self.close)
		exit.setShortcut('Ctrl+Q')

		open_ = QtGui.QAction(QtGui.QIcon('open.png'), 'Open File', self)
		open_.setShortcut('Ctrl+F')
		open_.setStatusTip('Import JSON')
		open_.triggered.connect(self.mapTweets)

		self.webView = QtWebKit.QWebView()
		self.webView.setHtml(open(r"./index.html").read())
		self.setCentralWidget(self.webView)

		menubar = self.menuBar()
		menu = menubar.addMenu('&File')
		menu.addAction(exit)
		menu.addAction(open_)

		toolbar = self.addToolBar('Quit')
		toolbar.addAction(exit)
		toolbar = self.addToolBar('Open File')
		toolbar.addAction(open_)

		self.setGeometry(300, 400, 700, 500)
		self.setWindowTitle('Map o Tweets')
		self.show()
		self.webView.show()


	def mapTweets(self):
		map_ = folium.Map(location=[33.4484, -112.0740])

		file = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '~')
		if file == '':
			return
		
		tweets = io_geojson.read_tweets(file)
		for t in tweets:
			data = tweet.Tweet(t)
			folium.Marker([data.bounds[0][1], data.bounds[0][0]], popup = data.text).add_to(map_)

		map_.save(r"./index.html")
		self.webView.setHtml(open("./index.html").read())
		self.webView.show()

def main():
	app = QtGui.QApplication(sys.argv)

	view = View()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()