#!/usr/bin/python
""" imageProc is an application to do several simple operations in image processing"""
__author__="tahhan"
__date__ ="$Mar 16, 2012 12:56:40 AM$"

from PyQt4 import QtGui
import sys
from gui import MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
