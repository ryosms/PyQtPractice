import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        btn1 = QtGui.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Event sender")
        self.show()

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was pressed")


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
