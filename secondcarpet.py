from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowsecondcarpet(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);")
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(-10, -20, 811, 71))
        self.lineEdit.setMaximumSize(QtCore.QSize(811, 71))
        self.lineEdit.setStyleSheet("background-color: rgb(26, 179, 179);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(-10, 30, 651, 41))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(651, 41))
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 170, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(34, 90, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 60, 141, 71))
        self.label.setMaximumSize(QtCore.QSize(141, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo22.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(550, 90, 81, 51))
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG_3006.JPEG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 90, 81, 51))
        self.pushButton_13.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMG_2972.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(249, 173, 1);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 211, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(249, 173, 1);\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 310, 221, 121))
        self.textEdit.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 460, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(54, 54, 54);\n"
"    color:rgb(30, 200, 200);\n"
"    border-radius: 1px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(249, 173, 1)\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 550, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 580, 211, 91))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 680, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(89, 173, 1);\n"
"background-color: rgb(170, 255, 127);")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 200, 441, 511))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("IMG_2912.JPG"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Iranian Carpet"))
        self.label_3.setText(_translate("MainWindow", "only"))
        self.label_2.setText(_translate("MainWindow", "T"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Order now"))
        self.label_5.setText(_translate("MainWindow", "Comment"))
        self.label_6.setText(_translate("MainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowsecondcarpet()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
