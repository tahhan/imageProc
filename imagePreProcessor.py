#!/usr/bin/python
""" this class deal with image procssing """
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
        width, height = self.img.size

        #pixeling : the only purpose of this it to reduce the over head of im.getpixel()
        self.pixels = self.img.load()

        #initialize histogram with zeros
        self.histo = [0 for x in range(256)]

        #now fill it
        for i in range(width):
            for j in range(height):
                self.histo[self.pixels[i,j]] = self.histo[self.pixels[i,j]]+1

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
                self.img.putpixel((i, j), ( (maxR - minR)/float(max - min) )* (self.pixels[i,j] - min) )

        self.loadImageFromPIX(self.img)

    def slidesLeftHisto(self, amount):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel( (i, j), self.pixels[i,j] - amount )

        self.loadImageFromPIX(self.img)

    def slidesRightHisto(self, amount):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel( (i, j), self.pixels[i,j] + amount )

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
                self.img.putpixel((i, j), self.histo[ self.pixels[i,j] ]  )

        self.loadImageFromPIX(self.img)

    def negative(self):
        width, height = self.img.size
        for i in range(width):
            for j in range(height):
                self.img.putpixel((i, j), 255 - self.pixels[i,j]  )

        self.loadImageFromPIX(self.img)

    def meanFilter(self):
        width, height = self.img.size
        for i in range(1, width-1):
            for j in range(1, height-1):
                result = (
                self.pixels[ (i - 1), j-1] +
                self.pixels[ (i - 1), j ] +
                self.pixels[ (i - 1), j+1 ] +
                self.pixels[ i, j-1 ] +
                self.pixels[ i, j ] +
                self.pixels[ i, j+1 ] +
                self.pixels[ (i+1), j-1 ] +
                self.pixels[ (i+1), j ] +
                self.pixels[ (i+1), j+1 ] ) / 9

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
                   window.append( self.pixels[j , i] )
             # Order elements (only half of them)
             for x in range(0, 5):
                # Find position of minimum element
                min = x
                for l in range(x + 1, 9):
                    if window[l] < window[min]:
                       min = l
                #Put found minimum element in its place
                temp = window[x];
                window[x] = window[min]
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
                pixel_up = self.pixels[i,j-1]
                pixel_down = self.pixels[i,j+1]
                pixel_left = self.pixels[i-1,j]
                pixel_right = self.pixels[i+1,j]
                pixel_up_left = self.pixels[i-1,j-1]
                pixel_up_right = self.pixels[i+1,j-1]
                pixel_down_left = self.pixels[i-1,j+1]
                pixel_down_right = self.pixels[i+1,j+1]

                # appliying convolution mask
                conv_x = (pixel_up_right+(pixel_right*2)+pixel_down_right)-(pixel_up_left+(pixel_left*2)+pixel_down_left)
                conv_y = (pixel_up_left+(pixel_up*2)+pixel_up_right)-(pixel_down_left+(pixel_down*2)+pixel_down_right)

                # calculating the distance
                #gray = math.sqrt( (conv_x*conv_x+conv_y+conv_y) )
                gray = math.fabs(conv_x)+math.fabs(conv_y);
                newImg.putpixel((i,j), gray)

        self.loadImageFromPIX(newImg)
