from PyQt5 import QtCore, QtGui, QtWidgets
import signup
import customer
import shopkeeper
import admin
class Ui_MainWindowwelcome(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color:rgb(26, 26, 26)")
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 110, 300, 91))
        self.label.setMaximumSize(QtCore.QSize(300, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(225, 225, 225)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 400, 350, 81))
        self.pushButton.setMaximumSize(QtCore.QSize(350, 81))
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
"    background-color: rgb(255, 170, 0)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 270, 350, 81))
        self.pushButton_2.setMaximumSize(QtCore.QSize(350, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 400, 350, 81))
        self.pushButton_3.setMaximumSize(QtCore.QSize(350, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 530, 350, 81))
        self.pushButton_4.setMaximumSize(QtCore.QSize(350, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
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
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.pushButton.clicked.connect(self.gotowin2)
        self.pushButton_2.setText(_translate("MainWindow", "Admin"))
        self.pushButton_2.clicked.connect(self.gotowin9)
        self.pushButton_3.setText(_translate("MainWindow", "Customer"))
        self.pushButton_3.clicked.connect(self.gotowin4)
        self.pushButton_4.setText(_translate("MainWindow", "shopkeeper"))
        self.pushButton_4.clicked.connect(self.gotowin6)
    def gotowin2(self):                        #vasl kardane welcome b signup
        self.mw = QtWidgets.QMainWindow()
        self.win2 = signup.Ui_MainWindowsignup()
        self.win2.setupUi(self.mw)
        self.MainWindow.hide()
        self.mw.show()    

    def gotowin4(self):                        #vasl kardane welcome b customer
        self.mw2 = QtWidgets.QMainWindow()
        self.win4 = customer.Ui_MainWindowcustomer()
        self.win4.setupUi(self.mw2)
        self.MainWindow.hide()
        self.mw2.show()    
    
    def gotowin6(self):                        #vasl kardane welcome b shopkeeper
        self.mw4 = QtWidgets.QMainWindow()
        self.win6 = shopkeeper.Ui_MainWindowshopkeeper()
        self.win6.setupUi(self.mw4)
        self.MainWindow.hide()
        self.mw4.show()    

    def gotowin9(self):                        #vasl kardane welcome b admin
        self.mw7 = QtWidgets.QMainWindow()
        self.win9 = admin.Ui_MainWindowadmin()
        self.win9.setupUi(self.mw7)
        self.MainWindow.hide()
        self.mw7.show()    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowwelcome()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
