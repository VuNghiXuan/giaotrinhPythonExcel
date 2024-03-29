# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doimau.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(500, 420, 75, 23))
        # self.pushButton_2.setObjectName("pushButton_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(580, 420, 75, 23))
        # self.pushButton_3.setObjectName("pushButton_3")
        self.label_maylanh = QtWidgets.QLabel(self.centralwidget)
        self.label_maylanh.setGeometry(QtCore.QRect(100, 10, 0, 0))
        self.label_maylanh.setText("")
        self.label_maylanh.setPixmap(QtGui.QPixmap("./B1/dieuhoa.gif"))
        self.label_maylanh.resize(600, 400)
        # self.label.setPixmap(QtGui.QPixmap("./B1/vang.png"))

        self.label_maylanh.setObjectName("label_maylanh")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(450, 280, 141, 71))
        # self.label_2.setText("")
        # self.label_2.setPixmap(QtGui.QPixmap("./B1/vang.png"))
        # self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # doi mau            
        self.pushButton.setCheckable(True) #Nhận biết các trạng thái được nhấn và thả của nút nếu được đặt thành true   
        self.pushButton.toggle() #toggle: Chuyển đổi tín hiệu từ nhấn-->thả, ngược lại
        self.pushButton.clicked.connect(self.toggle_bnt) #Liên kết nút bấm
        
        # self.pushButton_2.setCheckable(True) #Nhận biết các trạng thái được nhấn và thả của nút nếu được đặt thành true   
        # self.pushButton_2.toggle() #toggle: Chuyển đổi tín hiệu từ nhấn-->thả, ngược lại
        # self.pushButton_2.clicked.connect(self.toggle_bnt_2)

        # self.pushButton_3.setCheckable(True) #Nhận biết các trạng thái được nhấn và thả của nút nếu được đặt thành true   
        # self.pushButton_3.toggle() #toggle: Chuyển đổi tín hiệu từ nhấn-->thả, ngược lại
        # self.pushButton_3.clicked.connect(self.toggle_bnt_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ON/OFF"))
        # self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        # self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
    
    # def toggle_bnt(self):
    #     if self.pushButton.isChecked():
    #         self.label.setPixmap(QtGui.QPixmap("./B1/den.jpg"))
    #     else:
    #         self.label.setPixmap(QtGui.QPixmap("./B1/vang.png"))
    
    # Chuyển thành máy điều hòa
    def toggle_bnt(self):
        if self.pushButton.isChecked():
            self.label_maylanh.setPixmap(QtGui.QPixmap("./B1/dieuhoa.gif"))
        else:
            self.movie = QMovie('./B1/dieuhoa.gif')
            self.label_maylanh.setMovie(self.movie)
            self.movie.start()
            
    def toggle_bnt_2(self):
        if self.pushButton_2.isChecked():
            self.label_2.setPixmap(QtGui.QPixmap("./B1/den.jpg"))
        # else:
        #     self.label.setPixmap(QtGui.QPixmap("./B1/vang.png"))
    def toggle_bnt_3(self):
        if self.pushButton_3.isChecked():
            self.label_2.setPixmap(QtGui.QPixmap("./B1/vang.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
