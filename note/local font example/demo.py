# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(217, 90)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 131, 26))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 63, 14))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "那就是什么吧"))
        self.label.setText(_translate("MainWindow", "你说什么"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ###################################
    # 自定义本地font
    font_db = QtGui.QFontDatabase()
    font_id = font_db.addApplicationFont('GenWanMinTW-Medium.ttf')
    fm = font_db.applicationFontFamilies(font_id)
    print(fm)
    ttf_font = QtGui.QFont(fm[0])
    ####################################

    MainWindow = QtWidgets.QMainWindow()

    # 设置font
    MainWindow.setFont(ttf_font)

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
