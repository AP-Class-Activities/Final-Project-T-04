from PyQt5 import QtCore, QtGui, QtWidgets
import kids
import boxmessage
import favoritemessage
import box
import show

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 60, 141, 71))
        self.label.setMaximumSize(QtCore.QSize(141, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo22.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(34, 90, 411, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_10.setObjectName("label_10")
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 71, 41))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 460, 221, 71))
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 200, 441, 511))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("IMG_2941.JPG"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 580, 221, 91))
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255)")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 550, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_5.setObjectName("label_5")
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
        self.pushButton_12.clicked.connect(self.gotowin80)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(460, 90, 81, 51))
        self.pushButton_13.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("IMG_2972.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.gotowin71)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(70, 310, 221, 121))
        self.label_17.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 1px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QLable:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 720, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"    color: rgb(255, 225, 225);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(26, 179, 179)\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 680, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(89, 173, 1);\n"
"background-color: rgb(170, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 680, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(89, 173, 1);\n"
"background-color: rgb(170, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
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
        self.label_2.setText(_translate("MainWindow", "T"))
        self.label_3.setText(_translate("MainWindow", "only"))
        self.pushButton.setText(_translate("MainWindow", "Order now"))
        self.pushButton.clicked.connect(self.gotowin81)
        self.label_5.setText(_translate("MainWindow", "Comment"))
        self.pushButton_9.setText(_translate("MainWindow", "back"))
        self.pushButton_2.setText(_translate("MainWindow", "Send"))
        self.pushButton_3.setText(_translate("MainWindow", "Show"))
        self.pushButton_3.clicked.connect(self.gotowin83)

    def gotowin80(self):                             #vasl b favoritmessage dialog
        self.mw78 = QtWidgets.QMainWindow()
        self.win80 = favoritemessage.Ui_MainWindow()
        self.win80.setupUi(self.mw78)
        self.mw78.show()        

    def gotowin81(self):                             #vasl b favoritmessage dialog
        self.mw79 = QtWidgets.QMainWindow()
        self.win81 = box.Ui_MainWindow()
        self.win81.setupUi(self.mw79)
        self.mw79.show()       

    def gotowin71(self):                             #vasl b sabadkharid dialog
        self.mw69 = QtWidgets.QMainWindow()
        self.win71 = boxmessage.Ui_MainWindow()
        self.win71.setupUi(self.mw69)
        self.mw69.show()                    

    def gotowin62(self):                             #vasl b kids
        self.mw60 = QtWidgets.QMainWindow()
        self.win62 = kids.Ui_MainWindowkids()
        self.win62.setupUi(self.mw60)
        self.MainWindow.hide()
        self.mw60.show()                

    def gotowin83(self):                             #vasl b show
        self.mw81 = QtWidgets.QMainWindow()
        self.win83 = show.Ui_MainWindow()
        self.win83.setupUi(self.mw81)
        self.mw81.show()                        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
