from PyQt5 import QtCore, QtGui, QtWidgets
import adminvorod
from admin_db import acceptSH
import Qdialog


class Ui_MainWindowadminaddshopkeeper(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.label_7.setGeometry(QtCore.QRect(610, 80, 181, 81))
        self.label_7.setMinimumSize(QtCore.QSize(141, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("logo22.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 660, 111, 61))
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
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 280, 621, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "     border-radius: 15px;\n"
                                      "\n"
                                      "    background-color: rgb(143, 214, 214);\n"
                                      "\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 140, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
                                 "     border-radius: 15px;\n"
                                 "\n"
                                 "    background-color:rgb(255, 170, 0);\n"
                                 "\n"
                                 "    color:black;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 660, 111, 61))
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
        self.pushButton_3.setGeometry(QtCore.QRect(270, 660, 111, 61))
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
        self.pushButton_4.setGeometry(QtCore.QRect(120, 660, 111, 61))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ADD or Remove shopkeeper"))
        self.pushButton.setText(_translate("MainWindow", "YES"))
        self.label.setText(_translate("MainWindow", "add/remove shopkeeper"))
        self.pushButton_2.setText(_translate("MainWindow", "NO"))
        self.pushButton_3.setText(_translate("MainWindow", "ADD"))
        self.pushButton_4.setText(_translate("MainWindow", "back"))
        self.pushButton_4.clicked.connect(self.gotowin22)
        self.lineEdit_3.setText(_translate("MainWindow", self.box()))
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)

    def box(self):
        try:
            return (acceptSH().show2())
        except:
            return "There are no new requests!!!"

    def accept(self):  # accept new shopkeeper
        A = acceptSH().accept()
        self.mw1 = QtWidgets.QMainWindow()
        self.win3 = Qdialog.Ui_MainWindow()
        self.win3.setupUi(self.mw1)
        self.mw1.show()

    def reject(self):  # reject new shopkeeper
        A = acceptSH().reject()
        self.mw1 = QtWidgets.QMainWindow()
        self.win3 = Qdialog.Ui_MainWindow()
        self.win3.setupUi(self.mw1)
        self.mw1.show()

    def gotowin22(self):  # back b adminvorod
        self.mw20 = QtWidgets.QMainWindow()
        self.win22 = adminvorod.Ui_MainWindowadminvorod()
        self.win22.setupUi(self.mw20)
        self.MainWindow.hide()
        self.mw20.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowadminaddshopkeeper()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
