#!/usr/bin/python

__author__="tahhan"
__date__ ="$Mar 16, 2012 12:56:40 AM$"

from PyQt4 import QtGui, QtCore
import sys, os, random, math
import Image

HISTOGRAM_THRESHOLD = 50

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
        grid.addWidget(btnEdgeDetection, 8,0)

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

    def slidesRightHisto(amount):
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

class imagePreProcessor(QtGui.QWidget):
    def __init__(self):
        super(imagePreProcessor, self).__init__()
        self.Qimg = None

    def loadImage(self, imgFile, isGray=1):
        self.img = Image.open(imgFile)
    
        if isGray:
            self.img = self.img.convert("L")
            filename, self.ext = os.path.splitext(imgFile)
            imgFile = '/tmp/' + str(random.random()) + self.ext
            self.img.save(imgFile)

        self.Qimg = QtGui.QImage(imgFile)        
        #remove tmp file
        if isGray:
            os.remove(imgFile)

        self.findHistogram()
        self.repaint()
       
    def loadImageFromPIX(self, img):
        self.img = img
        imgFile = '/tmp/' + str(random.random()) + self.ext
        self.img.save(imgFile)
        self.Qimg = QtGui.QImage(imgFile)
        os.remove(imgFile)
        self.findHistogram()
        self.repaint()

    def findHistogram(self):
        #pixeling : the only purpose of this it to reduce the over head of im.getpixel()
        self.pixels = list(self.img.getdata())
        width, height = self.img.size
        self.pixels = [self.pixels[i * width:(i + 1) * width] for i in xrange(height)]
        #end pixeling

        self.histo = []
        for i in range(256):
            self.histo.append(0)

        for i in range(height):
            for j in range(width):
                self.histo[self.pixels[i][j]] = self.histo[self.pixels[i][j]]+1

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        if self.Qimg :
            painter.drawImage(event.rect(), self.Qimg, event.rect())
        painter.end()

    def minGrayLevel(self):
        min = 0
        for i in range(0, 255):
            if self.histo[i] >= HISTOGRAM_THRESHOLD:
                min = i
                break
        return min
   
    def maxGrayLevel(self):
        max = 255
        for i in range(self.histo.__len__()-1, 0, -1):
            if self.histo[i] >= HISTOGRAM_THRESHOLD:
                max = i
                break
        return max

    def stretchHisto(self):
        min = self.minGrayLevel()
        max = self.maxGrayLevel()
        self.histoMod(min, max, 0, 255)

    def shrinkHisto(self, minR, maxR):
        min = self.minGrayLevel()
        max = self.maxGrayLevel()
        self.histoMod(min, max, minR, maxR)

    def histoMod(self, min, max, minR, maxR):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel((i, j), ( (maxR - minR)/float(max - min) )* (self.img.getpixel((i,j)) - min) )

        self.loadImageFromPIX(self.img)

    def slidesLeftHisto(self, amount):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel( (i, j), self.img.getpixel( (i,j) ) - amount )
        
        self.loadImageFromPIX(self.img)

    def slidesRightHisto(self, amount):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel( (i, j), self.img.getpixel( (i,j) ) + amount )

        self.loadImageFromPIX(self.img)

    def negative(self):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel((i, j), 255 - self.img.getpixel((i,j))  )
        
        self.loadImageFromPIX(self.img)
        
    def histogramEqualization(self):
        runningSum = []
        dummyNumber = 0
        for i in range(0, 255):
            dummyNumber += self.histo[i]
            runningSum.append(dummyNumber)

        totalNumber = runningSum[-1]
        maxGrayLevel = self.maxGrayLevel()
        for i in range(0, 255):
            self.histo[i] = round((runningSum[i]/float(totalNumber)) * maxGrayLevel)
        
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel((i, j), self.histo[self.img.getpixel((i,j))]  )

        self.loadImageFromPIX(self.img)

    def meanFilter(self):
        width, height = self.img.size
        for i in range(1, width-1):
            for j in range(1, height-1):
                result = (
                self.img.getpixel( ( (i - 1), j-1) ) +
                self.img.getpixel( ( (i - 1), j ) ) +
                self.img.getpixel( ( (i - 1), j+1 ) ) +
                self.img.getpixel( ( i, j-1 ) ) +
                self.img.getpixel( ( i, j ) ) +
                self.img.getpixel( ( i, j+1 ) ) +
                self.img.getpixel( ( (i+1), j-1 ) ) +
                self.img.getpixel( ( (i+1), j ) ) +
                self.img.getpixel( ( (i+1), j+1 ) ) ) / 9

                self.img.putpixel( (i, j), result )

        self.loadImageFromPIX(self.img)

    def medianFilter(self):
        width, height = self.img.size
        for m in range(1, width-1):
            for n in range(1, height-1):
             # Pick up window elements
             window = []
             for j in range(m-1, m+2):
                for i in range(n-1, n+2):
                   window.append( self.img.getpixel((j , i)) )
             # Order elements (only half of them)
             for j in range(0, 5):
                # Find position of minimum element
                min = j
                for l in range(j + 1, 9):
                    if window[l] < window[min]:
                       min = l
                #Put found minimum element in its place
                temp = window[j];
                window[j] = window[min]
                window[min] = temp
             #   Get result - the middle element
             self.img.putpixel( ( (m-1) , n-1), window[4])

        self.loadImageFromPIX(self.img)

    def edgeDetection(self):
        newImg = Image.new("L", self.img.size)
        width, height = self.img.size
        for i in range(1, width-1):
            for j in range(1, height-1):
                # getting gray value of all surrounding pixels
                pixel_up = self.img.getpixel((i,j-1))
                pixel_down = self.img.getpixel((i,j+1))
                pixel_left = self.img.getpixel((i-1,j))
                pixel_right = self.img.getpixel((i+1,j))
                pixel_up_left = self.img.getpixel((i-1,j-1))
                pixel_up_right = self.img.getpixel((i+1,j-1))
                pixel_down_left = self.img.getpixel((i-1,j+1))
                pixel_down_right = self.img.getpixel((i+1,j+1))
                # appliying convolution mask
                conv_x = (pixel_up_right+(pixel_right*2)+pixel_down_right)-(pixel_up_left+(pixel_left*2)+pixel_down_left)
                conv_y = (pixel_up_left+(pixel_up*2)+pixel_up_right)-(pixel_down_left+(pixel_down*2)+pixel_down_right)
                # calculating the distance
                #gray = math.sqrt( (conv_x*conv_x+conv_y+conv_y) )
                gray = math.fabs(conv_x)+math.fabs(conv_y);
                newImg.putpixel((i,j), gray)

        self.loadImageFromPIX(newImg)

class chart(QtGui.QWidget):
    def __init__(self, chartData=[]):
        super(chart, self).__init__()
        self.chartData = chartData

    def setData(self, chartData ):
        self.chartData = chartData
        self.repaint()

    def paintEvent(self, event):
        if self.chartData :
            painter = QtGui.QPainter()
            painter.begin(self)
            # set color and width of line drawing pen
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))
            # drawLine(x1, y1, x2, y2) from point (x1,y1) to (x2,y2)
            # draw the baseline
            painter.drawLine(45, 160, 310, 160)
            # set up color and width of the bars
            width = 0.5
            painter.setPen(QtGui.QPen(QtCore.Qt.red, width))
            delta = width + 0.5
            x = 50
            for y in self.chartData:
                # correct for width
                y1 = 160 - width/2
                y2 = y1 - math.ceil(y/30) + width/2
                # draw each bar
                painter.drawLine(x, y1, x, y2)
                # add values to the top of each bar
                #s = str(y)
                #painter.drawText(x-8, y2-15, s)
                x += delta
            painter.end()
  

def main():
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
