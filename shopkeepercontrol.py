from PyQt5 import QtCore, QtGui, QtWidgets
import shop
import addproducts
import welcome
from login_db import DataBase
class Ui_MainWindowshopkeepercontrol(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
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
        self.label_7.setGeometry(QtCore.QRect(570, 80, 221, 81))
        self.label_7.setMinimumSize(QtCore.QSize(141, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Downloads/logo22.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 600, 91, 41))
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
        self.pushButton_2.setGeometry(QtCore.QRect(600, 600, 91, 41))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 320, 91, 51))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 520, 91, 51))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 420, 91, 51))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 220, 91, 51))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 610, 91, 51))
        self.lineEdit_8.setStyleSheet("QLineEdit{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 520, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 610, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 420, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(255, 170, 0);\n"
"\n"
"    color:black;\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 660, 101, 51))
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
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(380, 260, 331, 321))
        self.listWidget.setStyleSheet("QListWidget{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color: rgb(143, 214, 214);\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"     border-radius: 15px;\n"
"\n"
"    background-color:rgb(26, 26,26);\n"
"\n"
"    color:white;\n"
"}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
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
        temp = DataBase().dict()
        score = str(temp["score"])
        income = str(temp["income"])
        location = temp["location"]
        profit = str(temp["profit"])
        wallet = str(temp["wallet"])
        product = str(temp["products"])
        products = product[1:-1]
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "shop"))
        self.pushButton.clicked.connect(self.gotowin12)
        self.pushButton_2.setText(_translate("MainWindow", "add"))
        self.pushButton_2.clicked.connect(self.gotowin13)
        self.label_2.setText(_translate("MainWindow", "income"))
        self.label_5.setText(_translate("MainWindow", "score"))
        self.label_8.setText(_translate("MainWindow", "wallet"))
        self.label_3.setText(_translate("MainWindow", "profit"))
        self.label_4.setText(_translate("MainWindow", "location"))
        self.lineEdit_6.setText(_translate("MainWindow", income))
        self.lineEdit_5.setText(_translate("MainWindow", location))
        self.lineEdit_8.setText(_translate("MainWindow", wallet))
        self.lineEdit_3.setText(_translate("MainWindow", profit))
        self.lineEdit_4.setText(_translate("MainWindow", score))
        self.pushButton_3.setText(_translate("MainWindow", "back"))
        self.pushButton_3.clicked.connect(self.gotowin17)
        self.label_9.setText(_translate("MainWindow", "items"))
        self.listWidget.addItem(products)

    def gotowin12(self):                        #vasl  b shop
        self.mw10 = QtWidgets.QMainWindow()
        self.win12 = shop.Ui_MainWindowshop()
        self.win12.setupUi(self.mw10)
        self.MainWindow.hide()
        self.mw10.show()    

    def gotowin13(self):                        #vasl  b addproducts
        self.mw11 = QtWidgets.QMainWindow()
        self.win13 = addproducts.Ui_MainWindowaddproducts()
        self.win13.setupUi(self.mw11)
        self.MainWindow.hide()
        self.mw11.show()    

   
    def gotowin17(self):                        #back b welcome
        self.mw15 = QtWidgets.QMainWindow()
        self.win17 = welcome.Ui_MainWindowwelcome()
        self.win17.setupUi(self.mw15)
        self.MainWindow.hide()
        self.mw15.show()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowshopkeepercontrol()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())