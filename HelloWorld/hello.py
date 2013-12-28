import sys
from PyQt4 import QtCore, QtGui


def main():

    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    hello_button = QtGui.QPushButton(u"波浪ワールド")
    main_window.setCentralWidget(hello_button)
    main_window.show()
    app.exec()

if __name__ == '__main__':
    main()

