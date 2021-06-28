from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowkids(object):
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 60, 141, 60))
        self.label.setMaximumSize(QtCore.QSize(650, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo22.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(34, 90, 411, 51))
        self.label_10.setMaximumSize(QtCore.QSize(411, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 151, 151))
        self.label_2.setMaximumSize(QtCore.QSize(151, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("IMG_2927.JPG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 170, 151, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("IMG_2931.JPG"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 170, 151, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("IMG_2929.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 170, 151, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("IMG_2937.JPG"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 450, 151, 151))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("IMG_2941.JPG"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 450, 151, 151))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("IMG_2933.JPG"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 450, 151, 151))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("IMG_2939.JPG"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 450, 151, 151))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("IMG_2935.JPG"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(410, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(600, 640, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(410, 640, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 640, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 640, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(30, 200, 200);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(290, 700, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
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
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(460, 80, 171, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IMG_2972.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_12.setCheckable(False)
        self.pushButton_12.setObjectName("pushButton_12")
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
        self.label_10.setText(_translate("MainWindow", "Kids Room Carpet"))
        self.pushButton_3.setText(_translate("MainWindow", "Details"))
        self.pushButton_4.setText(_translate("MainWindow", "Details"))
        self.pushButton_5.setText(_translate("MainWindow", "Details"))
        self.pushButton_6.setText(_translate("MainWindow", "Details"))
        self.pushButton_7.setText(_translate("MainWindow", "Details"))
        self.pushButton_8.setText(_translate("MainWindow", "Details"))
        self.pushButton_9.setText(_translate("MainWindow", "Details"))
        self.pushButton_10.setText(_translate("MainWindow", "Details"))
        self.pushButton_11.setText(_translate("MainWindow", "back"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
