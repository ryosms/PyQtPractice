import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    close_app = QtCore.pyqtSignal()

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.close_app.connect(self.close)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Emit signal")
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self.close_app.emit()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
