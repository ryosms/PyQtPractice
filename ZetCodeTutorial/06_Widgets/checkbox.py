import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        cb = QtGui.QCheckBox("Show title", self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.change_title)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("QtGui.QCheckBox")
        self.show()

    def change_title(self, state):
        if state:
            self.setWindowTitle("QtGui.QCheckBox")
        else:
            self.setWindowTitle("")


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
