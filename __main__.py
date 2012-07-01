#!/usr/bin/python

__author__="tahhan"
__date__ ="$Mar 16, 2012 12:56:40 AM$"

from PyQt4 import QtGui, QtCore
import sys

from chart import chart
from imagePreProcessor import imagePreProcessor

class MainWindow(QtGui.QMainWindow):
    """" main window class"""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        mainWidget = QtGui.QWidget()
        hbox = QtGui.QHBoxLayout(mainWidget)

        self.rightbottom = QtGui.QWidget(mainWidget)
        #self.rightbottom.setFixedHeight(400)

        grid = QtGui.QGridLayout()
        self.rightbottom.setLayout(grid)

        btnStretch = QtGui.QPushButton('Stretch Histogram',self.rightbottom)
        btnStretch.clicked.connect(self.stretchHisto)
        grid.addWidget(btnStretch, 0,0)

        btnShrink = QtGui.QPushButton('Shrink Histogram', self.rightbottom)
        btnShrink.clicked.connect(self.shrinkHisto)
        grid.addWidget(btnShrink, 1,0)

        btnSlidesLeft = QtGui.QPushButton('Slides Left Histogram', self.rightbottom)
        btnSlidesLeft.clicked.connect(self.slidesLeftHisto)
        grid.addWidget(btnSlidesLeft, 2,0)

        btnSlidesRight = QtGui.QPushButton('Slides Right Histogram', self.rightbottom)
        btnSlidesRight.clicked.connect(self.slidesRightHisto)
        grid.addWidget(btnSlidesRight, 3,0)

        btnNegative = QtGui.QPushButton('Negative', self.rightbottom)
        btnNegative.clicked.connect(self.negative)
        grid.addWidget(btnNegative, 4,0)

        btnHistogramEq = QtGui.QPushButton('Histogram Equalization', self.rightbottom)
        btnHistogramEq.clicked.connect(self.histogramEqualization)
        grid.addWidget(btnHistogramEq, 6,0)

        btnMeanFilter = QtGui.QPushButton('Local Operations(mean)', self.rightbottom)
        btnMeanFilter.clicked.connect(self.meanFilter)
        grid.addWidget(btnMeanFilter, 7,0)

        btnMedianFilter = QtGui.QPushButton('Local Operations(median)', self.rightbottom)
        btnMedianFilter.clicked.connect(self.medianFilter)
        grid.addWidget(btnMedianFilter, 8,0)

        btnEdgeDetection = QtGui.QPushButton('Edge Detection', self.rightbottom)
        btnEdgeDetection.clicked.connect(self.edgeDetection)
        grid.addWidget(btnEdgeDetection, 9,0)

        #btnRest = QtGui.QPushButton('Rest', self.rightbottom)
        #grid.addWidget(btnRest, 9,0)

        lblSlidesLeft = QtGui.QLabel('By:')
        grid.addWidget(lblSlidesLeft, 2,1)
        
        self.slidesLeftEdit = QtGui.QLineEdit()
        grid.addWidget(self.slidesLeftEdit, 2,2)

        lblSlidesRight = QtGui.QLabel('By:')
        grid.addWidget(lblSlidesRight, 3,1)

        self.slidesRightEdit = QtGui.QLineEdit()
        grid.addWidget(self.slidesRightEdit, 3,2)

        lblMaxR = QtGui.QLabel('Max:')
        grid.addWidget(lblMaxR, 1,1)

        self.maxREdit = QtGui.QLineEdit()
        grid.addWidget(self.maxREdit, 1,2)
        
        lblMinR = QtGui.QLabel('Min:')
        grid.addWidget(lblMinR, 1,3)

        self.minREdit = QtGui.QLineEdit()
        grid.addWidget(self.minREdit, 1,4)

        #hide it, its empty
        self.rightbottom.hide()

        self.imgPreProc = imagePreProcessor()
        #self.imgPreProc.setFixedSize(800,650)
        
        self.histoChart = chart()
        #self.histoChart.setFixedHeight(180)
        
        splitter1 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter1.addWidget(self.histoChart)
        splitter1.addWidget(self.rightbottom)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter2.addWidget(self.imgPreProc)
        splitter2.addWidget(splitter1)
        
        hbox.addWidget(splitter2)
        mainWidget.setLayout(hbox)
        """
        #new stuff
        splitter1 = QtGui.QSplitter(QtCore.Qt.Vertical)# down right
        splitter1.addWidget(self.rightbottom) #controls
        splitter1.addWidget(self.histoChart) #right chart 

        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical) # down
        splitter2.addWidget(self.histoChart) # left chart
        splitter2.addWidget(splitter1)

        splitter3 = QtGui.QSplitter(QtCore.Qt.Vertical) # up
        splitter3.addWidget(self.imgPreProc) #left image
        splitter3.addWidget(self.imgPreProc) #right image

        splitter4 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter4.addWidget(splitter3)
        splitter4.addWidget(splitter2)

        hbox.addWidget(splitter4)
        mainWidget.setLayout(hbox)
        #end new stuff
        """
        self.setCentralWidget(mainWidget)

        self.setupMenu()

        #self.setGeometry(300, 300, 1200, 700)
        self.showMaximized()
        self.setWindowTitle('Image Processing')
        self.setWindowIcon(QtGui.QIcon('IP.gif'))
        self.show()
        
    def setupMenu(self):
        """Creates the menu bar and binds actions to methods."""
        file_menu = self.menuBar().addMenu('&File')
        file_menu.addAction('&Open...', self.showOpen).setShortcut('Ctrl+O')

    def showOpen(self):
        """Shows the file opening dialog."""
        filepath = QtGui.QFileDialog.getOpenFileName(
        self, 'Open File', '', 'All Files (*.*);;jpeg (*.jpeg);;jpg (*.jpg);;png (*.png)')

        if filepath:
            self.open(filepath)

    def open(self, filepath):
		self.imgPreProc.loadImage(str(filepath))
		self.rebuildHisto()
		self.rightbottom.show()

    def rebuildHisto(self):
		self.histoChart.setData(self.imgPreProc.histo)

    def stretchHisto(self):
		self.imgPreProc.stretchHisto()	
		self.rebuildHisto()

    def shrinkHisto(self):
        if self.minREdit.text().isEmpty():
            QtGui.QMessageBox.critical(self, "Error", "You have to fill the Min")
        else :
            minR = int(self.minREdit.text())
            if self.maxREdit.text().isEmpty():
                QtGui.QMessageBox.critical(self, "Error", "You have to fill the Max")
            else :
                maxR = int(self.maxREdit.text())
                self.imgPreProc.shrinkHisto(minR, maxR)
                self.rebuildHisto()
	
    def slidesLeftHisto(self):
        if self.slidesLeftEdit.text().isEmpty():
            QtGui.QMessageBox.critical(self, "Error", "You have to fill the By")
        else :
            amount  = int(self.slidesLeftEdit.text())
            self.imgPreProc.slidesLeftHisto(amount)
            self.rebuildHisto()

    def slidesRightHisto(self):
        if self.slidesRightEdit.text().isEmpty():
            QtGui.QMessageBox.critical(self, "Error", "You have to fill the By")
        else :
            amount  = int(self.slidesRightEdit.text())
            self.imgPreProc.slidesRightHisto(amount)
            self.rebuildHisto()

    def negative(self):
        self.imgPreProc.negative()
        self.rebuildHisto()

    def histogramEqualization(self):
        self.imgPreProc.histogramEqualization()
        self.rebuildHisto()

    def meanFilter(self):
        self.imgPreProc.meanFilter()
        self.rebuildHisto()

    def medianFilter(self):
        self.imgPreProc.medianFilter()
        self.rebuildHisto()

    def edgeDetection(self):
        self.imgPreProc.edgeDetection()
        self.rebuildHisto()

def main():
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
