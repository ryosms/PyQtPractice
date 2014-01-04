import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.text = u"""\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
                        \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
                        \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430"""

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Draw text")
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_text(e, qp)
        qp.end()

    def draw_text(self, event, qp):
        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont("Decorative", 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
