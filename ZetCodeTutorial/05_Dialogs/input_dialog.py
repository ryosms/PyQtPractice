import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.btn = QtGui.QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.show_dialog)

        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Input dialog")
        self.show()

    def show_dialog(self):
        text, ok = QtGui.QInputDialog.getText(self, "Input Dialog",
                                              "Enter your name:")

        if ok:
            self.le.setText(str(text))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()