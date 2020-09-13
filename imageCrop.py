# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageCrop.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import QLabel,QListWidget, QListWidgetItem, QPushButton
import PySide2.QtWidgets
from PySide2.QtCore import QTimer
import cv2
import qimage2ndarray
class ImageLable(QLabel):
    
    start=(0,0)
    current=(0,0)
    #end=(0,0)
    drawFlag=False
    selectedMode=None
    def mouseMoveEvent(self, ev):
        if self.drawFlag!=False and self.selectedMode!=None:
            #print(self.selectedMode)
            x=int(ev.x()*self.widthFactor)
            y=int(ev.y()*self.heightFactor)
            #Free Square 3:2 4:3 5:4 7:5 16:9
            if self.selectedMode=="Free":
                pass
            elif self.selectedMode=="Square":
                width=abs(x-self.start[0])
                height=width
                y=int(self.start[1]+height)
            elif self.selectedMode== "3:2":
                width=abs(x-self.start[0]) 
                height=(2/3)*width
                y=int(self.start[1]+height)
            elif self.selectedMode== "4:3":
                width=abs(x-self.start[0]) 
                height=(3/4)*width
                y=int(self.start[1]+height)
            elif self.selectedMode== "5:4":
                width=abs(x-self.start[0]) 
                height=(4/5)*width
                y=int(self.start[1]+height)
            elif self.selectedMode== "7:5":
                width=abs(x-self.start[0]) 
                height=(5/7)*width
                y=int(self.start[1]+height)
            elif self.selectedMode== "16:9":
                width=abs(x-self.start[0]) 
                height=(9/16)*width
                y=int(self.start[1]+height)
            self.current=( x,y )
            self.tempImage=self.drawImage.copy()
            cv2.rectangle(self.tempImage,self.start,self.current,(255,255,0),2)
  
    def mousePressEvent(self, ev):
        self.drawFlag=True
        x=int(ev.x()*self.widthFactor)
        y=int(ev.y()*self.heightFactor)        
        self.start=( x,y )

    def mouseReleaseEvent(self, ev):
        self.drawFlag=False

    def __init__(self,parent,image):
        super().__init__(parent)
        self.drawImage=image
        self.tempImage=image.copy()
        self.setObjectName(u"label")
        self.setGeometry(QRect(20, 20, 781, 431))
        self.setStyleSheet(u"background-color: rgb(85, 255, 255)")
        self.setScaledContents(True)
        self.setMouseTracking(True)
        self.setText(QCoreApplication.translate("ImageCrop", u"<html><head/><body style=\"background-color:powderblue;\"><p align=\"center\">Your Image Here</p></body></html>", None))
        self.widthFactor=image.shape[1]/self.size().width()
        self.heightFactor=image.shape[0]/self.size().height()

class Ui_Dialog(object):

    final_image=None

    def __init__(self,image):
        super().__init__()
        self.image=image


    def showFrame(self):
        if len(self.listWidget.selectedItems())>0:
            self.imageWidget.selectedMode=self.listWidget.selectedItems()[0].text()
        else:
            self.imageWidget.selectedMode=None
        image=cv2.cvtColor(self.imageWidget.tempImage,cv2.COLOR_BGR2RGB)
        image=qimage2ndarray.array2qimage(image)
        self.imageWidget.setPixmap(QPixmap.fromImage(image))
        pass

    

    def commitCrop(self,Dialog):
        start=self.imageWidget.start
        end=self.imageWidget.current
        if start!=end:
            print(start,end)
            #self.image=self.image[start[0]:end[0],start[1]:end[1]]
            self.image=self.image[start[1]:end[1],start[0]:end[0]]
            print(self.image.shape)
        Dialog.close()

    def cancle(self):
        #print("Lol")
        self.listWidget.setCurrentItem(None)
        self.imageWidget.tempImage=self.image

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1104, 481)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(970, 90, 61, 28))
        self.pushButton_2.clicked.connect(self.cancle)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(880, 90, 61, 28))
        self.pushButton.clicked.connect(lambda : self.commitCrop(Dialog))
        
        self.listWidget = QListWidget(Dialog)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(830, 150, 256, 192))

        """ self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 781, 431))
        self.label.setStyleSheet(u"background-color: rgb(85, 255, 255)")
        self.label.setScaledContents(True) """
        self.imageWidget=ImageLable(Dialog,self.image)

        self.timer=QTimer()
        self.timer.timeout.connect(self.showFrame) 
        self.timer.start(1) 

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Image Crop", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u274c", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u2705 ", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"Free", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"Square", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"3:2", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"4:3", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"5:4", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"7:5", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"16:9", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        #self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body style=\"background-color:powderblue;\"><p align=\"center\">Your Image Here</p></body></html>", None))
    # retranslateUi

