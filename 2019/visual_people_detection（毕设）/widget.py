# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wz/PycharmProjects/visual_people_detection/widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1019, 809)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(30, 700, 601, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 670, 171, 17))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 700, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 700, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(780, 700, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(30, 230, 941, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.map1 = QtWidgets.QLabel(self.frame)
        self.map1.setGeometry(QtCore.QRect(10, 10, 150, 200))
        self.map1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map1.setText("")
        self.map1.setTextFormat(QtCore.Qt.AutoText)
        self.map1.setObjectName("map1")
        self.map2 = QtWidgets.QLabel(self.frame)
        self.map2.setGeometry(QtCore.QRect(180, 10, 150, 200))
        self.map2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map2.setText("")
        self.map2.setObjectName("map2")
        self.map3 = QtWidgets.QLabel(self.frame)
        self.map3.setGeometry(QtCore.QRect(350, 10, 150, 200))
        self.map3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map3.setText("")
        self.map3.setObjectName("map3")
        self.map4 = QtWidgets.QLabel(self.frame)
        self.map4.setGeometry(QtCore.QRect(520, 10, 150, 200))
        self.map4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map4.setText("")
        self.map4.setObjectName("map4")
        self.map6 = QtWidgets.QLabel(self.frame)
        self.map6.setGeometry(QtCore.QRect(10, 220, 150, 200))
        self.map6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map6.setText("")
        self.map6.setObjectName("map6")
        self.map5 = QtWidgets.QLabel(self.frame)
        self.map5.setGeometry(QtCore.QRect(690, 10, 150, 200))
        self.map5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map5.setText("")
        self.map5.setObjectName("map5")
        self.map7 = QtWidgets.QLabel(self.frame)
        self.map7.setGeometry(QtCore.QRect(180, 220, 150, 200))
        self.map7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map7.setText("")
        self.map7.setObjectName("map7")
        self.map8 = QtWidgets.QLabel(self.frame)
        self.map8.setGeometry(QtCore.QRect(350, 220, 150, 200))
        self.map8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map8.setText("")
        self.map8.setObjectName("map8")
        self.map9 = QtWidgets.QLabel(self.frame)
        self.map9.setGeometry(QtCore.QRect(520, 220, 150, 200))
        self.map9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map9.setText("")
        self.map9.setObjectName("map9")
        self.map10 = QtWidgets.QLabel(self.frame)
        self.map10.setGeometry(QtCore.QRect(690, 220, 150, 200))
        self.map10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.map10.setText("")
        self.map10.setObjectName("map10")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(10, 40, 981, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setObjectName("widget_2")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(870, 10, 98, 74))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.listWidget = QtWidgets.QListWidget(self.widget_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 0, 841, 171))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 13, 384, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 740, 941, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 650, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 721, 471))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 721, 471))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.r1 = QtWidgets.QLabel(self.tab_3)
        self.r1.setGeometry(QtCore.QRect(10, 650, 91, 101))
        self.r1.setFrameShape(QtWidgets.QFrame.Box)
        self.r1.setText("")
        self.r1.setObjectName("r1")
        self.r2 = QtWidgets.QLabel(self.tab_3)
        self.r2.setGeometry(QtCore.QRect(100, 650, 91, 101))
        self.r2.setFrameShape(QtWidgets.QFrame.Box)
        self.r2.setText("")
        self.r2.setObjectName("r2")
        self.r3 = QtWidgets.QLabel(self.tab_3)
        self.r3.setGeometry(QtCore.QRect(190, 650, 91, 101))
        self.r3.setFrameShape(QtWidgets.QFrame.Box)
        self.r3.setText("")
        self.r3.setObjectName("r3")
        self.r4 = QtWidgets.QLabel(self.tab_3)
        self.r4.setGeometry(QtCore.QRect(280, 650, 91, 101))
        self.r4.setFrameShape(QtWidgets.QFrame.Box)
        self.r4.setText("")
        self.r4.setObjectName("r4")
        self.r5 = QtWidgets.QLabel(self.tab_3)
        self.r5.setGeometry(QtCore.QRect(370, 650, 91, 101))
        self.r5.setFrameShape(QtWidgets.QFrame.Box)
        self.r5.setText("")
        self.r5.setObjectName("r5")
        self.r6 = QtWidgets.QLabel(self.tab_3)
        self.r6.setGeometry(QtCore.QRect(460, 650, 91, 101))
        self.r6.setFrameShape(QtWidgets.QFrame.Box)
        self.r6.setText("")
        self.r6.setObjectName("r6")
        self.r7 = QtWidgets.QLabel(self.tab_3)
        self.r7.setGeometry(QtCore.QRect(550, 650, 91, 101))
        self.r7.setFrameShape(QtWidgets.QFrame.Box)
        self.r7.setText("")
        self.r7.setObjectName("r7")
        self.r8 = QtWidgets.QLabel(self.tab_3)
        self.r8.setGeometry(QtCore.QRect(640, 650, 91, 101))
        self.r8.setFrameShape(QtWidgets.QFrame.Box)
        self.r8.setText("")
        self.r8.setObjectName("r8")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(10, 630, 131, 17))
        self.label_13.setObjectName("label_13")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdNumber.setGeometry(QtCore.QRect(740, 10, 251, 101))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.d1 = QtWidgets.QLabel(self.tab_3)
        self.d1.setGeometry(QtCore.QRect(10, 510, 91, 111))
        self.d1.setFrameShape(QtWidgets.QFrame.Box)
        self.d1.setText("")
        self.d1.setObjectName("d1")
        self.d2 = QtWidgets.QLabel(self.tab_3)
        self.d2.setGeometry(QtCore.QRect(100, 510, 91, 111))
        self.d2.setFrameShape(QtWidgets.QFrame.Box)
        self.d2.setText("")
        self.d2.setObjectName("d2")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 490, 131, 17))
        self.label_16.setObjectName("label_16")
        self.d3 = QtWidgets.QLabel(self.tab_3)
        self.d3.setGeometry(QtCore.QRect(190, 510, 91, 111))
        self.d3.setFrameShape(QtWidgets.QFrame.Box)
        self.d3.setText("")
        self.d3.setObjectName("d3")
        self.d4 = QtWidgets.QLabel(self.tab_3)
        self.d4.setGeometry(QtCore.QRect(280, 510, 91, 111))
        self.d4.setFrameShape(QtWidgets.QFrame.Box)
        self.d4.setText("")
        self.d4.setObjectName("d4")
        self.d5 = QtWidgets.QLabel(self.tab_3)
        self.d5.setGeometry(QtCore.QRect(370, 510, 91, 111))
        self.d5.setFrameShape(QtWidgets.QFrame.Box)
        self.d5.setText("")
        self.d5.setObjectName("d5")
        self.d6 = QtWidgets.QLabel(self.tab_3)
        self.d6.setGeometry(QtCore.QRect(460, 510, 91, 111))
        self.d6.setFrameShape(QtWidgets.QFrame.Box)
        self.d6.setText("")
        self.d6.setObjectName("d6")
        self.d7 = QtWidgets.QLabel(self.tab_3)
        self.d7.setGeometry(QtCore.QRect(550, 510, 91, 111))
        self.d7.setFrameShape(QtWidgets.QFrame.Box)
        self.d7.setText("")
        self.d7.setObjectName("d7")
        self.d8 = QtWidgets.QLabel(self.tab_3)
        self.d8.setGeometry(QtCore.QRect(640, 510, 91, 111))
        self.d8.setFrameShape(QtWidgets.QFrame.Box)
        self.d8.setText("")
        self.d8.setObjectName("d8")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_3)
        self.lcdNumber_2.setGeometry(QtCore.QRect(840, 110, 151, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(740, 200, 251, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 249, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(740, 180, 201, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(740, 350, 201, 17))
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(740, 450, 251, 26))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox.setGeometry(QtCore.QRect(740, 370, 251, 26))
        self.spinBox.setObjectName("spinBox")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(740, 430, 201, 17))
        self.label_7.setObjectName("label_7")
        self.btn_pause = QtWidgets.QPushButton(self.tab_3)
        self.btn_pause.setGeometry(QtCore.QRect(890, 710, 101, 41))
        self.btn_pause.setObjectName("btn_pause")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(740, 500, 201, 17))
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(740, 520, 251, 25))
        self.comboBox.setObjectName("comboBox")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Widget)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label_4.setText(_translate("Widget", "Please select the tab:"))
        self.pushButton_3.setText(_translate("Widget", "submit"))
        self.pushButton_4.setText(_translate("Widget", "Reset"))
        self.pushButton_5.setText(_translate("Widget", "Train"))
        self.pushButton.setText(_translate("Widget", "Add..."))
        self.pushButton_2.setText(_translate("Widget", "Clear"))
        self.label.setText(_translate("Widget", "Add peoples\' photos you want to train for your classifier:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Widget", "Train classifier"))
        self.pushButton_6.setText(_translate("Widget", "Start"))
        self.label_13.setText(_translate("Widget", "[Rejected faces]"))
        self.label_16.setText(_translate("Widget", "[Detected faces]"))
        self.label_5.setText(_translate("Widget", "[Detected people] "))
        self.label_6.setText(_translate("Widget", "[Detected interval]"))
        self.label_7.setText(_translate("Widget", "[Convience]"))
        self.btn_pause.setText(_translate("Widget", "Pause"))
        self.label_8.setText(_translate("Widget", "[Save way ]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Widget", "Real-time system"))


