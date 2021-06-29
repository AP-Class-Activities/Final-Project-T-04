from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0)")
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 90, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_7.setObjectName("label_7")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(290, 210, 71, 51))
        self.plainTextEdit_2.setStyleSheet("QPlainTextEdit{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 90, 161, 51))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(420, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(255, 170, 0);\n"
"\n"
"    color: rgb(255, 225, 225);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"\n"
"    background-color: rgb(26, 179, 179)\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(630, 420, 111, 51))
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(350, 630, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(630, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_11.setObjectName("label_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(630, 350, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
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
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(630, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.pushButton_12.setGeometry(QtCore.QRect(630, 210, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton{\n"
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
        self.pushButton_12.setObjectName("pushButton_12")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(290, 280, 71, 51))
        self.plainTextEdit_3.setStyleSheet("QPlainTextEdit{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(290, 350, 71, 51))
        self.plainTextEdit_4.setStyleSheet("QPlainTextEdit{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(290, 420, 71, 51))
        self.plainTextEdit_5.setStyleSheet("QPlainTextEdit{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(120, 550, 221, 101))
        self.plainTextEdit_7.setStyleSheet("QPlainTextEdit{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QPlainTextEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QPlainTextEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(450, 550, 221, 101))
        self.lineEdit_16.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
"    color: #FFF;\n"
"\n"
"    background-color: rgb(36, 36, 36);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62)\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(35, 218, 233)\n"
"\n"
"    background-color: rgb(47, 47, 47)\n"
"}")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 670, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border-radius: 2px;\n"
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 191, 51))
        self.label_2.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 280, 191, 51))
        self.label_3.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 350, 191, 51))
        self.label_4.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 420, 191, 51))
        self.label_12.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(440, 210, 131, 51))
        self.label_13.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(440, 280, 131, 51))
        self.label_14.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(440, 350, 131, 51))
        self.label_15.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(440, 420, 131, 51))
        self.label_16.setStyleSheet("QLabel{\n"
"    border: 2px solid rgb(38, 38, 48);\n"
"    border-radius: 15px;\n"
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
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(340, 670, 111, 71))
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
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(30, 670, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    border-radius: 1px;\n"
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
        self.pushButton_13.setObjectName("pushButton_13")
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
        self.pushButton.setText(_translate("MainWindow", "Charging Wallet"))
        self.label_5.setText(_translate("MainWindow", "Address"))
        self.label_6.setText(_translate("MainWindow", "Price"))
        self.label_7.setText(_translate("MainWindow", "Discount Code"))
        self.lineEdit_3.setText(_translate("MainWindow", "Wallet"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "username"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete"))
        self.label_8.setText(_translate("MainWindow", "Products"))
        self.label_9.setText(_translate("MainWindow", "Total Price"))
        self.label_10.setText(_translate("MainWindow", "Number"))
        self.label_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_10.setText(_translate("MainWindow", "Delete"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_12.setText(_translate("MainWindow", "Delete"))
        self.pushButton_3.setText(_translate("MainWindow", "Pay"))
        self.pushButton_13.setText(_translate("MainWindow", "Back"))
        self.pushButton_13.clicked.connect(self.gotowin70)


    def gotowin70(self):                             #baste shodan
        self.MainWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
