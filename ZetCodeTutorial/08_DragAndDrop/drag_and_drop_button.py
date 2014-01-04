import sys
from PyQt4 import QtGui, QtCore


class Button(QtGui.QPushButton):
    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return

        mime_data = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        drop_action = drag.start(QtCore.Qt.MoveAction)

    def mousePressEvent(self, e):
        super(Button, self).mousePressEvent(e)

        if e.buttons() == QtCore.Qt.LeftButton:
            print("press")


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setAcceptDrops(True)

        self.button = Button("Button", self)
        self.button.move(100, 65)

        self.setWindowTitle("Clicke or Move")
        self.setGeometry(300, 300, 280, 150)
        self.show()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
