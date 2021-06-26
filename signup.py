from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowsignup(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(26, 26, 26)\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 300, 91))
        self.label.setMaximumSize(QtCore.QSize(300, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(225, 225, 225)")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 350, 361, 51))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 450, 361, 51))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(180, 650, 200, 51))
        self.commandLinkButton_2.setMaximumSize(QtCore.QSize(200, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setStyleSheet("QCommandLinkButton{\n"
"    border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCommandLinkButton:hover{\n"
"\n"
"    background-color: rgb(113, 169, 169);\n"
"}")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 550, 361, 51))
        self.pushButton.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
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
"    background-color: rgb(26, 179, 179)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 250, 361, 51))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(361, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(400, 650, 181, 51))
        self.comboBox.setMinimumSize(QtCore.QSize(181, 51))
        self.comboBox.setMaximumSize(QtCore.QSize(181, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n"
"    border-radius: 25px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"\n"
"    background-color: rgb(113, 169, 169);\n"
"}")
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "password"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Email"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "back"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "username"))
        self.comboBox.setItemText(0, _translate("MainWindow", "customer"))
        self.comboBox.setItemText(1, _translate("MainWindow", "shopkeeper"))
        self.comboBox.setItemText(2, _translate("MainWindow", "admin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
