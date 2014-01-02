import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        exit_action = QtGui.QAction(QtGui.QIcon("qt.png"), "&Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(exit_action)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Menubar")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
