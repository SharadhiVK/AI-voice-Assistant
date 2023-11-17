# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JarvisUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Bg = QtWidgets.QLabel(self.centralwidget)
        self.Bg.setGeometry(QtCore.QRect(-30, -20, 1131, 601))
        self.Bg.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Bg.setText("")
        self.Bg.setScaledContents(False)
        self.Bg.setObjectName("Bg")
        self.bg_border = QtWidgets.QLabel(self.centralwidget)
        self.bg_border.setGeometry(QtCore.QRect(0, 0, 1051, 561))
        self.bg_border.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border : 2px Solid White;\n"
"")
        self.bg_border.setText("")
        self.bg_border.setObjectName("bg_border")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 510, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border : 1px solid white;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 510, 131, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border : 1px solid white;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.Gif = QtWidgets.QLabel(self.centralwidget)
        self.Gif.setGeometry(QtCore.QRect(10, 10, 601, 381))
        self.Gif.setStyleSheet("border : 1px solid white;\n"
"\n"
"")
        self.Gif.setText("")
        self.Gif.setPixmap(QtGui.QPixmap("../../../../2 - Python/3 -  Materials/G.U.I Material/B.G/1.gif"))
        self.Gif.setScaledContents(True)
        self.Gif.setObjectName("Gif")
        self.Gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_2.setGeometry(QtCore.QRect(620, 10, 421, 201))
        self.Gif_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border : 1px solid white;\n"
"")
        self.Gif_2.setText("")
        self.Gif_2.setPixmap(QtGui.QPixmap("../../../../2 - Python/3 -  Materials/G.U.I Material/VoiceReg/gui (4).gif"))
        self.Gif_2.setScaledContents(True)
        self.Gif_2.setObjectName("Gif_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(780, 450, 256, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border : 2px solid white;\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.Terminal = QtWidgets.QLabel(self.centralwidget)
        self.Terminal.setGeometry(QtCore.QRect(10, 400, 761, 151))
        self.Terminal.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border : 1px solid white;\n"
"")
        self.Terminal.setText("")
        self.Terminal.setObjectName("Terminal")
        self.Gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.Gif_3.setGeometry(QtCore.QRect(620, 220, 421, 171))
        self.Gif_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(255, 255, 255);\n"
"border : 1px solid white;\n"
"")
        self.Gif_3.setText("")
        self.Gif_3.setPixmap(QtGui.QPixmap("../../../../2 - Python/3 -  Materials/G.U.I Material/ExtraGui/initial.gif"))
        self.Gif_3.setScaledContents(True)
        self.Gif_3.setObjectName("Gif_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "CLOSE"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
