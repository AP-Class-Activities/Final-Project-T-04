from PyQt5 import QtCore, QtGui, QtWidgets
from customer_db import DataBase


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(26, 26, 26)")
        self.MainWindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 210, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
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
        self.pushButton_10.setGeometry(QtCore.QRect(370, 160, 141, 41))
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
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 180, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(225, 225, 225)")
        self.label_11.setObjectName("label_11")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(70, 250, 241, 71))
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
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(70, 90, 241, 71))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
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
        self.pushButton_9.setText(_translate("MainWindow", "Back"))
        self.pushButton_9.clicked.connect(self.gotowin2)
        self.pushButton_10.setText(_translate("MainWindow", "Ok"))
        self.label_10.setText(_translate("MainWindow", "Deposit Amount"))
        self.label_11.setText(_translate("MainWindow", "User"))
        self.pushButton_10.clicked.connect(self.deposit)
    def deposit(self):
        user = self.plainTextEdit_3.toPlainText()
        money = int(self.plainTextEdit_2.toPlainText())
        dict = DataBase().search(user)
        wallet = dict["wallet"]
        new_wallet = wallet + money
        dict["wallet"] = new_wallet
        print(dict)
        print(money)
        DataBase().delete(user)
        DataBase().add(dict)

    def gotowin2(self):                             #vasl b rug
        self.MainWindow.close()
                      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
