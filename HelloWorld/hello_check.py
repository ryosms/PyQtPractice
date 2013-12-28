import sys
from PyQt4 import QtCore, QtGui


def print_state(state):
    if state == 0:
        print("Unchecked")
    else:
        print("Checked")


def main():
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    check_box = QtGui.QCheckBox("Check Box")

    check_box.stateChanged.connect(print_state)

    main_window.setCentralWidget(check_box)
    main_window.show()
    app.exec()

if __name__ == '__main__':
    main()

