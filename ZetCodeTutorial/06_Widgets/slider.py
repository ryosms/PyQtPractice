import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.change_value)

        self.lbl = QtGui.QLabel(self)
        self.lbl.setPixmap(QtGui.QPixmap("qt.png"))
        self.lbl.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QtGui.QSlider")
        self.show()

    def change_value(self, value):
        if value == 0:
            self.lbl.setPixmap(QtGui.QPixmap("qt.png"))
        else:
            self.lbl.setText("%d" % value)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
