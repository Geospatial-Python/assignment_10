import os
import sys
from PyQt4 import QtGui
from PyQt4 import QtWebKit
from PyQt4 import QtCore
import folium
from src import tweet
from src import io_geojson


class View(QtGui.QMainWindow):

    def __init__(self):
        super(View, self).__init__()

        self.map = None
        self.web_view = None
        self.map_dir = 'tmp/map.html'
        self.default_tweets = []
        tweets = io_geojson.read_tweets('tweets.json')
        for _ in tweets:
            self.default_tweets.append(tweet.Tweet(_))

        print("Note: Pressing on a tweet marker will show the user's name.")

        self.init_ui()

    def init_ui(self):
        # This is the central empty widget, to be replaced in a future assignment.
        self.web_view = QtWebKit.QWebView()
        self.map = folium.Map(location=[33.4484, -112.0740])
        self.map.zoom_start = 10

        # The map will be saved in a temporary directory. Make sure it exists.
        os.makedirs('tmp', exist_ok=True)

        self.display_tweets(self.default_tweets)

        # Define the exit action for use in the toolbar and file menu.
        exit_action = QtGui.QAction(QtGui.QIcon('exit-24.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        # Add a status bar.
        self.statusBar()

        # Add a menu bar, and add a file menu to that.
        menu_bar = self.menuBar()
        # Set the mnemonic to Alt-F.
        # Details: https://msdn.microsoft.com/en-us/library/system.windows.forms.label.usemnemonic(v=vs.110).aspx
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        # Add an exit item to the toolbar.
        tool_bar = self.addToolBar('Exit')
        tool_bar.addAction(exit_action)

        # x, y, width, height
        self.setGeometry(300, 300, 750, 650)
        self.setWindowTitle('Main Window')
        self.show()

        # Put the window in the middle of the screen.
        self.center()

    def center(self):
        geometry = self.frameGeometry()
        center = QtGui.QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def display_tweets(self, tweets):
        """

        Parameters
        ----------
        tweets
        A list of Tweet objects.

        Returns
        -------

        """
        print("Loading tweets, please wait...")

        # Credit to http://stackoverflow.com/a/3160819 for helping me develop the loading bar.
        # Use a loading bar to show progress.
        loading_bar_count = 50
        count_per_bar = len(tweets)/50

        # Setup loading bar.
        sys.stdout.write("[%s]" % (" " * loading_bar_count))
        sys.stdout.flush()
        sys.stdout.write("\b" * (loading_bar_count+1)) # return to start of line, after '['

        loaded_tweets = 0

        average_lat = 0
        average_lon = 0

        for tweet in tweets:
            lat, lon = tweet.gen_point_in_bounds()
            average_lat += lat
            average_lon += lon
            folium.Marker([lat, lon], popup=tweet.username).add_to(self.map)

            loaded_tweets += 1
            if loaded_tweets == count_per_bar:
                loaded_tweets = 0
                sys.stdout.write("-")
                sys.stdout.flush()

        sys.stdout.write("\n")

        average_lon /= len(tweets)
        average_lat /= len(tweets)
        self.map.location = [average_lat, average_lon]

        self.map.save(self.map_dir)
        self.web_view.load(QtCore.QUrl(self.map_dir))
        self.setCentralWidget(self.web_view)


def main():
    app = QtGui.QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()