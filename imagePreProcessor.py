# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="tahhan"
__date__ ="$Jun 28, 2012 1:01:29 AM$"

from PyQt4 import QtGui, QtCore
import os, Image, random, math

HISTOGRAM_THRESHOLD = 50

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


if __name__ == "__main__":
    print "nothing to do here for now"
