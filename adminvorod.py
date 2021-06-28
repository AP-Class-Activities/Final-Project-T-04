from PyQt5 import QtCore, QtGui, QtWidgets
import adminadd
import adminaddproducts
import adminaddshopkeeper
import welcome
class Ui_MainWindowadminvorod(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(-10, -20, 811, 71))
        self.lineEdit.setStyleSheet("background-color: rgb(26, 179, 179);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(-10, 30, 651, 41))
        self.lineEdit_2.setStyleSheet("background-color:rgb(255, 170, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(610, 80, 181, 81))
        self.label_7.setMinimumSize(QtCore.QSize(141, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("logo22.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 370, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 280, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(143, 214, 214);\n"
"\n"
"    color:black;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 190, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 470, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(143, 214, 214);\n"
"\n"
"    color:black;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
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
        self.pushButton.setText(_translate("MainWindow", "shopkeeper"))
        self.pushButton.clicked.connect(self.gotowin18)
        self.pushButton_2.setText(_translate("MainWindow", "products"))
        self.pushButton_2.clicked.connect(self.gotowin19)
        self.pushButton_3.setText(_translate("MainWindow", "customers"))
        self.pushButton_3.clicked.connect(self.gotowin20)
        self.pushButton_4.setText(_translate("MainWindow", "back"))
        self.pushButton_4.clicked.connect(self.gotowin21)
    def gotowin18(self):                             #shopkeeper b adminaddshopkeeper
        self.mw16 = QtWidgets.QMainWindow()
        self.win18 = adminaddshopkeeper.Ui_MainWindowadminaddshopkeeper()
        self.win18.setupUi(self.mw16)
        self.MainWindow.hide()
        self.mw16.show()    

    def gotowin19(self):                             #products b adminaddproducts
        self.mw17 = QtWidgets.QMainWindow()
        self.win19 = adminaddproducts.Ui_MainWindowadminaddproducts()
        self.win19.setupUi(self.mw17)
        self.MainWindow.hide()
        self.mw17.show()    
        
    def gotowin20(self):                             #custoer b adminadd
        self.mw18 = QtWidgets.QMainWindow()
        self.win20 = adminadd.Ui_MainWindowadminadd()
        self.win20.setupUi(self.mw18)
        self.MainWindow.hide()
        self.mw18.show()         

    def gotowin21(self):                             #back b welcome
        self.mw19 = QtWidgets.QMainWindow()
        self.win21 = welcome.Ui_MainWindowwelcome()
        self.win21.setupUi(self.mw19)
        self.MainWindow.hide()
        self.mw19.show()         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowadminvorod()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
