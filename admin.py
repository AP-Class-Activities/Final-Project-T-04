from PyQt5 import QtCore, QtGui, QtWidgets
import  welcome

class Ui_MainWindowadmin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        font = QtGui.QFont()
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(26, 26, 26)")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 280, 420, 81))
        self.lineEdit.setMaximumSize(QtCore.QSize(420, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 420, 420, 81))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(420, 81))
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
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 560, 420, 81))
        self.pushButton.setMaximumSize(QtCore.QSize(420, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
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
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 300, 91))
        self.label.setMaximumSize(QtCore.QSize(300, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 680, 211, 41))
        self.pushButton_2.setMaximumSize(QtCore.QSize(420, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(113, 169, 169);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Back Icons – Free Vector Download, PNG, SVG, GIF_files/circled-left(4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "username"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "shopkeeper"))
        self.pushButton_2.setText(_translate("MainWindow", "back"))
        self.pushButton_2.clicked.connect(self.gotowin8)
    def gotowin8(self):                             #back b welcome
        self.mw6 = QtWidgets.QMainWindow()
        self.win8 = welcome.Ui_MainWindowwelcome()
        self.win8.setupUi(self.mw6)
        self.MainWindow.hide()
        self.mw6.show()    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
