import sys
from PyQt4 import QtGui


class View(QtGui.QMainWindow):

    def __init__(self):
        super(View, self).__init__()
        self.init_ui

    def init_ui(self):
        #central widget
        text_box = QtGui.QTextEdit()
        self.setCentralWidget(text_box)

        #Exit actions
        exit_action = QtGui.QAction(QtGui.QIcon('exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        self.statusBar()

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Assignment_09')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()