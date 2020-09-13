from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import cv2
from PySide2 import QtGui

class Ui_Dialog_Resize(object):

    def __init__(self,image):
        super().__init__()
        self.image=image

    def customORautomatic(self):
        if self.checkBox.isChecked():
            self.textEdit.setDisabled(False)
            self.textEdit_2.setDisabled(False)           
        else:
            self.textEdit.setDisabled(True)
            self.textEdit_2.setDisabled(True)

    def changeResolution(self,Dialog):
        if self.checkBox.isChecked():
            x=int(self.textEdit.toPlainText())
            y=int(self.textEdit_2.toPlainText())
            self.image=cv2.resize(self.image,(x,y))
            #open CV ka kaam 
        else:
            temp=self.listWidget.selectedItems()[0].text()
            temp=temp.split(":")[-1]
            temp=[int(i.strip()) for i in temp.split("x")]
            self.image=cv2.resize(self.image,(temp[0],temp[1]))
        
        QMessageBox.information(Dialog, 'Operation Complete',"Your Image has been resized",QMessageBox.Ok)
        Dialog.close()                           

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(284, 635)
        self.listWidget = QListWidget(Dialog)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)

        #resolution List
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 30, 241, 431))
        #Custom Resolution Checkbox
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(70, 480, 151, 20))
        self.checkBox.toggled.connect(self.customORautomatic)
        #Custom Resolution Text Edit X
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(60, 510, 191, 31))
        self.textEdit.setDisabled(True)
        #Custom Resolution Text Edit Y
        self.textEdit_2 = QTextEdit(Dialog)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(60, 560, 191, 31))
        self.textEdit_2.setDisabled(True)
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 510, 21, 21))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 560, 21, 21))
        
        # Resize it !!! button
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 600, 93, 28))
        self.pushButton.clicked.connect(lambda : self.changeResolution(Dialog))
        
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Resizer", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Dialog", u"4320p: 7680x4320", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Dialog", u"2160p: 3840x2160", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Dialog", u"1440p: 2560x1440", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Dialog", u"2048x1536", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Dialog", u"1920x1440", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Dialog", u"1080p: 1920x1080", None));
        ___qlistwidgetitem6 = self.listWidget.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Dialog", u"1600x1200", None));
        ___qlistwidgetitem7 = self.listWidget.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Dialog", u"1600x1200", None));
        ___qlistwidgetitem8 = self.listWidget.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Dialog", u"1440x1080", None));
        ___qlistwidgetitem9 = self.listWidget.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Dialog", u"1400x1050", None));
        ___qlistwidgetitem10 = self.listWidget.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Dialog", u"1280x960", None));
        ___qlistwidgetitem11 = self.listWidget.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Dialog", u"720p: 1280x720", None));
        ___qlistwidgetitem12 = self.listWidget.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Dialog", u"1024x768", None));
        ___qlistwidgetitem13 = self.listWidget.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Dialog", u"960x720", None));
        ___qlistwidgetitem14 = self.listWidget.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Dialog", u"480p: 854x480", None));
        ___qlistwidgetitem15 = self.listWidget.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Dialog", u"800x600", None));
        ___qlistwidgetitem16 = self.listWidget.item(16)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Dialog", u"640x480", None));
        ___qlistwidgetitem17 = self.listWidget.item(17)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Dialog", u"360p: 640x360", None));
        ___qlistwidgetitem18 = self.listWidget.item(18)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Dialog", u"240p: 426x240", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Custom Resolution", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Resize IT!!!", None))
    # retranslateUi

