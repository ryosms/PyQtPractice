import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.text_edit = QtGui.QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QtGui.QAction(QtGui.QIcon("qt.png"), "Open", self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip("Open new File")
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File dialog")
        self.show()

    def show_dialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, "Open file", "/home")
        f = open(fname, "r")

        with f:
            data = f.read()
            self.text_edit.setText(data)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
