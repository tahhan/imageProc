# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="tahhan"
__date__ ="$Jun 28, 2012 12:55:48 AM$"

from PyQt4 import QtGui, QtCore
import math

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

if __name__ == "__main__":
    print "nothing to do here for now"
