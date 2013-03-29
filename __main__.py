#!/usr/bin/python
""" imageProc is an application to do several simple operations in image processing"""
__author__="tahhan"
__date__ ="$Mar 16, 2012 12:56:40 AM$"

from PyQt4 import QtGui
import sys
from gui import MainWindow
from optparse import OptionParser


def runGui(app, fileName=None):
    ui = MainWindow()
    if fileName :
        ui.open(fileName)
    
    sys.exit(app.exec_())
    
def runCli():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose", default=True,
                      help="don't print status messages to stdout")

    (options, args) = parser.parse_args()
    sys.exit(0)
    
def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('imageProc')
    
    if len(sys.argv) == 1:
        runGui(app)
    if len(sys.argv) == 2:
        runGui(app, sys.argv[1])
    if len(sys.argv) > 2:
        runCli()
    
if __name__ == '__main__':
    main()
