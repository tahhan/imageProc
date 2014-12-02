
from PyQt4 import QtCore, QtGui
import PIL.ImageQt as ImageQt

from Chart import Chart
from imagePreProcessor import imagePreProcessor

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.imgPreProc = imagePreProcessor()

    def setupUi(self, MainWindow):
        MainWindow.showMaximized()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        #MainWindow.resize(1014, 682)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))

        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        self.gridLayout_3 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        self.scrollArea_2 = QtGui.QScrollArea(self.frame_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))

        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 459, 448))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))

        self.gridLayout_6 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))

        self.modifided_image = ImageWidget(self.scrollAreaWidgetContents_2)
        self.modifided_image.setObjectName(_fromUtf8("modifided_image"))

        self.gridLayout_6.addWidget(self.modifided_image, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))

        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 448))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))

        self.original_image = ImageWidget(self.scrollAreaWidgetContents)
        self.original_image.setObjectName(_fromUtf8("original_image"))

        self.gridLayout_5.addWidget(self.original_image, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidget.setFloating(True)
        self.dockWidget.setGeometry(QtCore.QRect(0, 0, 620, 220))

        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))

        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.frame_4 = QtGui.QFrame(self.dockWidgetContents)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))

        self.gridLayout_8 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))

        self.original_histogram = Chart(self.frame_4)
        self.original_histogram.setObjectName(_fromUtf8("original_histogram"))

        self.gridLayout_8.addWidget(self.original_histogram, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_3 = QtGui.QFrame(self.dockWidgetContents)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))

        self.gridLayout_7 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))

        self.modifided_histogram = Chart(self.frame_3)
        self.modifided_histogram.setObjectName(_fromUtf8("modifided_histogram"))

        self.gridLayout_7.addWidget(self.modifided_histogram, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.frame_3)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))

        self.menuOperations = QtGui.QMenu(self.menubar)
        self.menuOperations.setObjectName(_fromUtf8("menuOperations"))
        self.menuOperations.setEnabled(False)

        self.menuHistogram_Modification = QtGui.QMenu(self.menuOperations)
        self.menuHistogram_Modification.setObjectName(_fromUtf8("menuHistogram_Modification"))

        self.menuSlide_Histogram = QtGui.QMenu(self.menuHistogram_Modification)
        self.menuSlide_Histogram.setObjectName(_fromUtf8("menuSlide_Histogram"))

        self.menuMapping_Equations = QtGui.QMenu(self.menuOperations)
        self.menuMapping_Equations.setObjectName(_fromUtf8("menuMapping_Equations"))

        self.menuLocal_Mask_Operations = QtGui.QMenu(self.menuOperations)
        self.menuLocal_Mask_Operations.setObjectName(_fromUtf8("menuLocal_Mask_Operations"))

        self.menuSegmentation = QtGui.QMenu(self.menuOperations)
        self.menuSegmentation.setObjectName(_fromUtf8("menuSegmentation"))

        MainWindow.setMenuBar(self.menubar)

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("action_Open"))
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.triggered.connect(self.showOpen)

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(QtGui.qApp.quit)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)

        self.actionStretch_Histogram = QtGui.QAction(MainWindow)
        self.actionStretch_Histogram.setObjectName(_fromUtf8("actionStretch_Histogram"))
        self.actionStretch_Histogram.triggered.connect(self.stretchHisto)

        self.actionShrink_Histogram = QtGui.QAction(MainWindow)
        self.actionShrink_Histogram.setObjectName(_fromUtf8("actionShrink_Histogram"))
        self.actionShrink_Histogram.triggered.connect(self.shrinkHisto)

        self.actionLeft = QtGui.QAction(MainWindow)
        self.actionLeft.setObjectName(_fromUtf8("actionLeft"))
        self.actionLeft.triggered.connect(self.slidesLeftHisto)

        self.actionRight = QtGui.QAction(MainWindow)
        self.actionRight.setObjectName(_fromUtf8("actionRight"))
        self.actionRight.triggered.connect(self.slidesRightHisto)

        self.actionHistogram_Equalization = QtGui.QAction(MainWindow)
        self.actionHistogram_Equalization.setObjectName(_fromUtf8("actionHistogram_Equalization"))
        self.actionHistogram_Equalization.triggered.connect(self.histogramEqualization)

        self.actionNegative = QtGui.QAction(MainWindow)
        self.actionNegative.setObjectName(_fromUtf8("actionNegative"))
        self.actionNegative.triggered.connect(self.negative)

        self.actionMean_Local_Filtering = QtGui.QAction(MainWindow)
        self.actionMean_Local_Filtering.setObjectName(_fromUtf8("actionMean_Local_Filtering"))
        self.actionMean_Local_Filtering.triggered.connect(self.meanFilter)

        self.actionMedian_Local_Filtering = QtGui.QAction(MainWindow)
        self.actionMedian_Local_Filtering.setObjectName(_fromUtf8("actionMedian_Local_Filtering"))
        self.actionMedian_Local_Filtering.triggered.connect(self.medianFilter)

        self.actionSobel_Edge_Detector = QtGui.QAction(MainWindow)
        self.actionSobel_Edge_Detector.setObjectName(_fromUtf8("actionSobel_Edge_Detector"))
        self.actionSobel_Edge_Detector.triggered.connect(self.edgeDetection)

        self.menuSlide_Histogram.addAction(self.actionLeft)
        self.menuSlide_Histogram.addAction(self.actionRight)

        self.menuHistogram_Modification.addAction(self.actionStretch_Histogram)
        self.menuHistogram_Modification.addAction(self.actionShrink_Histogram)
        self.menuHistogram_Modification.addAction(self.menuSlide_Histogram.menuAction())
        self.menuHistogram_Modification.addAction(self.actionHistogram_Equalization)

        self.menuMapping_Equations.addAction(self.actionNegative)

        self.menuLocal_Mask_Operations.addAction(self.actionMean_Local_Filtering)
        self.menuLocal_Mask_Operations.addAction(self.actionMedian_Local_Filtering)

        self.menuSegmentation.addAction(self.actionSobel_Edge_Detector)

        self.menuOperations.addAction(self.menuHistogram_Modification.menuAction())
        self.menuOperations.addAction(self.menuMapping_Equations.menuAction())
        self.menuOperations.addAction(self.menuLocal_Mask_Operations.menuAction())
        self.menuOperations.addAction(self.menuSegmentation.menuAction())

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOperations.menuAction())

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOperations.setTitle(_translate("MainWindow", "Operations", None))
        self.menuHistogram_Modification.setTitle(_translate("MainWindow", "Histogram Modification", None))
        self.menuSlide_Histogram.setTitle(_translate("MainWindow", "Slide Histogram", None))
        self.menuMapping_Equations.setTitle(_translate("MainWindow", "Mapping Equations", None))
        self.menuLocal_Mask_Operations.setTitle(_translate("MainWindow", "Local (Mask) Operations", None))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation", None))

        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionStretch_Histogram.setText(_translate("MainWindow", "Stretch Histogram", None))
        self.actionShrink_Histogram.setText(_translate("MainWindow", "Shrink Histogram", None))
        self.actionLeft.setText(_translate("MainWindow", "Left", None))
        self.actionRight.setText(_translate("MainWindow", "Right", None))
        self.actionHistogram_Equalization.setText(_translate("MainWindow", "Histogram Equalization", None))
        self.actionNegative.setText(_translate("MainWindow", "Negative", None))
        self.actionMean_Local_Filtering.setText(_translate("MainWindow", "Mean Local Filtering", None))
        self.actionMedian_Local_Filtering.setText(_translate("MainWindow", "Median Local Filtering", None))
        self.actionSobel_Edge_Detector.setText(_translate("MainWindow", "Sobel Edge Detector", None))

    def showOpen(self):
        """Shows the file opening dialog."""
        filepath = QtGui.QFileDialog.getOpenFileName(
        self, 'Open File', '', 'All Files (*.*);;jpeg (*.jpeg);;jpg (*.jpg);;png (*.png)')

        if filepath:
            self.open(filepath)

    def showIntDialog(self, title, text):
        amount, ok = QtGui.QInputDialog.getInt(self, title, text)

        if ok:
            return amount
        else:
            return 0

    def open(self, filepath):
        self.imgPreProc.loadImage(str(filepath))
        self.original_image.Qimg = ImageQt.ImageQt(self.imgPreProc.img.convert("RGB") if self.imgPreProc.img.mode == "L" else self.imgPreProc.img)
        self.original_image.repaint()
        self.original_histogram.setData(self.imgPreProc.histo)
        self.refreshAll()
        self.menuOperations.setEnabled(True)

    def repaintImage(self):
        self.modifided_image.Qimg = ImageQt.ImageQt(self.imgPreProc.img.convert("RGB") if self.imgPreProc.img.mode == "L" else self.imgPreProc.img) 
        self.modifided_image.repaint()

    def rebuildHisto(self):
        self.modifided_histogram.setData(self.imgPreProc.histo)

    def refreshAll(self):
        self.rebuildHisto()
        self.repaintImage()

    def stretchHisto(self):
        self.imgPreProc.stretchHisto()
        self.refreshAll()

    def shrinkHisto(self):
        minR = self.showIntDialog('Histogram Min Shrink', 'Shrink Min:')
        if minR:
            maxR = self.showIntDialog('Histogram Max Shrink', 'Shrink Max:')
            if maxR:
                self.imgPreProc.shrinkHisto(minR, maxR)
                self.refreshAll()
            else :
                QtGui.QMessageBox.critical(self, "Error", "Provide the the Max")
        else :
            QtGui.QMessageBox.critical(self, "Error", "Provide the the Min")
            

    def slidesLeftHisto(self):
        amount = self.showIntDialog('Slide Histogram, Left', 'Sliding Amount:')
        if amount:
            self.imgPreProc.slidesLeftHisto(amount)
            self.refreshAll()
        else :
            QtGui.QMessageBox.critical(self, "Error", "Provide the amount of sliding")            

    def slidesRightHisto(self):
        amount = self.showIntDialog('Slide Histogram, Right', 'Sliding Amount:')
        if amount:
            self.imgPreProc.slidesRightHisto(amount)
            self.refreshAll()
        else :
            QtGui.QMessageBox.critical(self, "Error", "You have to fill the By")

    def histogramEqualization(self):
        self.imgPreProc.histogramEqualization()
        self.refreshAll()

    def negative(self):
        self.imgPreProc.negative()
        self.refreshAll()

    def meanFilter(self):
        self.imgPreProc.meanFilter()
        self.refreshAll()

    def medianFilter(self):
        self.imgPreProc.medianFilter()
        self.refreshAll()

    def edgeDetection(self):
        self.imgPreProc.edgeDetection()
        self.refreshAll()

class ImageWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(ImageWidget, self).__init__(parent)
        self.Qimg = None

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        if self.Qimg :
            painter.drawImage(event.rect(), self.Qimg, event.rect())
        painter.end()
