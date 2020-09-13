# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QCoreApplication, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QTimer, QUrl, Qt
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import QAction, QDialog, QFileDialog, QLabel, QListWidget, QListWidgetItem, QMainWindow, QMenu, QMenuBar, QPushButton, QSlider, QStatusBar, QWidget
import cv2
import qimage2ndarray
from Effects import *
from imageCrop import Ui_Dialog
from imageResize import Ui_Dialog_Resize

class Ui_MainWindow(object):

    image_stack=[None]
    current_effect=""
    def resize(self):
        self.timer.stop()
        temp=QDialog()
        temp.ui=Ui_Dialog_Resize(self.image_stack[-1])
        temp.ui.setupUi(temp)
        temp.show()
        temp.exec_()
        self.image_stack.append(temp.ui.image)
        self.timer.start(1)
        pass

    def cropping(self):
        if type(self.image_stack[-1])==type(None):
            print("lol")
            return
        self.timer.stop()
        temp=QDialog()
        temp.ui=Ui_Dialog(self.image_stack[-1])
        temp.ui.setupUi(temp)
        temp.show()
        temp.exec_()
        self.image_stack.append(temp.ui.image)
        self.timer.start(1)
        pass

    def effectFuctions(self,effect,image,amount):
        if effect=="Brightness":
            return brightness(image, amount=amount)
        elif effect=="Saturation":
            return saturation(image, amount)
        elif effect=="Sharpen":
            return sharpness(image, amount)
        elif effect=="Sepia Effect":
            return sepia(image, amount)
        elif effect=="Warm":
            return warm(image, amount)
        elif effect == "Cold":
            return cold(image, amount)
        elif effect == "Equalize":
            return equalise(image, amount)
        elif effect== "Cartoon":
            return cartoon(image, amount)
        elif effect== "Blurring":
            return blurring(image, amount) 
        elif effect== "Pencil Sketch":
            return pencil_sketch(image, amount)
        elif effect== "Noise Reduction":
            return noise_reduction(image, amount)
        elif effect== "Negetive" :
            return negative(image, amount)
        elif effect== "Vignette":  
            return vignette(image, amount)
        elif effect== "Emboss":
            return emboss(image, amount)
        elif effect== "Redden": # lal panni
            return redden(image, amount)
        elif effect== "Greenify": # hari panni 
            return greenify(image, amount)
        elif effect== "Bloom Blue": # nili panni 
            return nili_panni(image, amount)
        elif effect== "HDR":  
            return hdr(image, amount)
        elif effect== "Yellow":  
            return yellow_panni(image, amount)


    def showFrame(self,frame):
        if type(frame)==type(None):
            self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body style=\"background-color:powderblue;\"><p align=\"center\">Your Image Here</p></body></html>", None))
            return
        if self.listWidget.selectedItems()!=[]:
            effect=self.listWidget.selectedItems()[0].text()
            if effect!=self.current_effect:
                print("LOL")
                self.current_effect=effect
                clearTemp()
            temp=self.effectFuctions(effect,frame.copy(),self.horizontalSlider.value())
            frame= temp if type(temp)!=type(None) else frame
        
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image=qimage2ndarray.array2qimage(frame)
        self.label.setPixmap(QPixmap.fromImage(image))
        pass

    def addImage(self):
        #
        self.image_stack=[None]
        filePath,_=QFileDialog.getOpenFileName(QMainWindow(), 'Open file')
        self.image_stack.append(cv2.imread(filePath))
        pass

    def saveImage(self):
        #print("lol")
        filePath,_=QFileDialog.getSaveFileName(QMainWindow(),"Choose the save location")
        self.label.pixmap().save(filePath,"jpg",100)
        
        #self.cv2.imwrite(filePath,self.image_stack[-1])
        #pass
    
    def commit(self):
        frame=self.image_stack[-1]
        if self.listWidget.selectedItems()==[]:
            return
        effect=self.listWidget.selectedItems()[0].text()
        temp=self.effectFuctions(effect,frame,self.horizontalSlider.value())
        #frame= temp if type(temp)!=type(None) else None
        if type(frame)!=type(None):
            self.image_stack.append(temp)
        self.horizontalSlider.setValue(0)
        self.listWidget.setCurrentItem(None)

    def cancle(self):
       self.horizontalSlider.setValue(0)
       self.listWidget.setCurrentItem(None)

    def undo(self):
        if type(self.image_stack)!=type(None):
            self.image_stack.pop()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1131, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 781, 431))
        self.label.setStyleSheet(u"background-color: rgb(85, 255, 255)")
        self.label.setScaledContents(True)
        
        self.listWidget = QListWidget(self.centralwidget)
        no_of_widgets=19
        for i in range(no_of_widgets):
            QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(850, 160, 256, 201))

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(870, 70, 211, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        #print(self.horizontalSlider.value())
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(930, 10, 101, 51))
        self.label_2.setMinimumSize(QSize(0, 31))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(10)
        
        # ✅ commit button
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(892, 110, 61, 28))
        self.pushButton.clicked.connect(lambda : self.commit())

        # ❌ cancle button
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(990, 110, 61, 28))
        self.pushButton_2.clicked.connect(lambda : self.cancle())

        # ↩️ Undo button
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(370, 20, 61, 28))
        self.pushButton_3.clicked.connect(lambda : self.undo())

        #crop
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(910, 380, 61, 28))
        self.pushButton_4.clicked.connect(self.cropping)
        
        # Resize
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(980, 380, 61, 28))
        self.pushButton_5.clicked.connect(self.resize)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")

        self.menubar.setGeometry(QRect(0, 0, 1131, 26))
        self.menuNew_File = QMenu(self.menubar)
        self.menuNew_File.setObjectName(u"menuNew_File")

        #New File
        self.actionNew_File = QAction("NewFile")
        self.actionNew_File.triggered.connect(self.addImage)
        self.menuNew_File.addAction(self.actionNew_File)

        #Save File
        self.actionSave_File = QAction("SaveFile")
        self.actionSave_File.triggered.connect(self.saveImage)
        self.menuNew_File.addAction(self.actionSave_File)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        self.timer=QTimer()
        self.timer.timeout.connect(lambda : self.showFrame(self.image_stack[-1]) ) 
        self.timer.start(1)

        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuNew_File.menuAction())
        #self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body style=\"background-color:powderblue;\"><p align=\"center\">Your Image Here</p></body></html>", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Brightness", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Saturation", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sharpen", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sepia Effect", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Warm", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Cold", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Equalize", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Cartoon", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Blurring", None)); 
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Pencil Sketch", None)); 
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Noise Reduction", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Negetive", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Vignette", None));  #"Redden" "Greenify" "Bloom Blue" "HDR" "Bass"
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Emboss", None)); 
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Redden", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Greenify", None));
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Bloom Blue", None));
        ___qlistwidgetitem17 = self.listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"HDR", None));
        ___qlistwidgetitem18 = self.listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Yellow", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Amount%</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2705 ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u274c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u21a9\ufe0f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Crop", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Resize", None))
        self.menuNew_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        #self.menuSave.setTitle(QCoreApplication.translate("MainWindow", u"Save ", None))
    # retranslateUi

