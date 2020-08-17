# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/AdemBerkAksoy/Desktop/ageof/main_design.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 838)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(998, 838))
        MainWindow.setMaximumSize(QtCore.QSize(998, 838))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("QPushButton{\n"
" border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setContentsMargins(50, 0, 50, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_choose = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_choose.sizePolicy().hasHeightForWidth())
        self.pushButton_choose.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.pushButton_choose.setFont(font)
        self.pushButton_choose.setObjectName("pushButton_choose")
        self.gridLayout_2.addWidget(self.pushButton_choose, 2, 2, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.page)
        self.pushButton_start.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 3, 1, 1, 1)
        self.pushButton_download = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_download.sizePolicy().hasHeightForWidth())
        self.pushButton_download.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.pushButton_download.setFont(font)
        self.pushButton_download.setObjectName("pushButton_download")
        self.gridLayout_2.addWidget(self.pushButton_download, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.gridLayout_2.setRowStretch(0, 3)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("QPushButton{\n"
" border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QCheckBox{\n"
"    padding-left:18px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width:25px;\n"
"    height:25px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/check/icons/unchecked.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/check/icons/checked.png);\n"
"    width:30px;\n"
"    height:30px;\n"
"}\n"
"#label_3,\n"
"#label_4,\n"
"#label_5,\n"
"#label_6,\n"
"#label_7,\n"
"#label_8,\n"
"#label_9,\n"
"#label_10,\n"
"#label_11 {\n"
"background-color: rgb(58,64,85);\n"
"border-radius: 7px;\n"
"color:rgb(21, 180, 6);\n"
"padding:5px\n"
"}\n"
"")
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setContentsMargins(0, 5, 0, 5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 1, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 1, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 1, 7, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5.addLayout(self.verticalLayout_2, 2, 0, 1, 8)
        self.gridLayout_5.setRowStretch(1, 2)
        self.gridLayout_5.setRowStretch(2, 9)
        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_12 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 2, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_x = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_x.sizePolicy().hasHeightForWidth())
        self.pushButton_x.setSizePolicy(sizePolicy)
        self.pushButton_x.setObjectName("pushButton_x")
        self.gridLayout_8.addWidget(self.pushButton_x, 0, 2, 1, 1)
        self.pushButton_4x = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4x.sizePolicy().hasHeightForWidth())
        self.pushButton_4x.setSizePolicy(sizePolicy)
        self.pushButton_4x.setObjectName("pushButton_4x")
        self.gridLayout_8.addWidget(self.pushButton_4x, 2, 2, 1, 1)
        self.pushButton_2x = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2x.sizePolicy().hasHeightForWidth())
        self.pushButton_2x.setSizePolicy(sizePolicy)
        self.pushButton_2x.setObjectName("pushButton_2x")
        self.gridLayout_8.addWidget(self.pushButton_2x, 1, 2, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 7, 2)
        self.pushButton_16x = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16x.sizePolicy().hasHeightForWidth())
        self.pushButton_16x.setSizePolicy(sizePolicy)
        self.pushButton_16x.setObjectName("pushButton_16x")
        self.gridLayout_8.addWidget(self.pushButton_16x, 3, 2, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.page_2)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_8.addWidget(self.pushButton_stop, 4, 2, 1, 1)
        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_8.setColumnStretch(2, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.gridLayout_7.setColumnStretch(1, 2)
        self.gridLayout_7.setColumnStretch(2, 1)
        self.gridLayout_7.setRowStretch(0, 1)
        self.gridLayout_7.setRowStretch(1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_7, 4, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 7)
        self.gridLayout_4.setRowStretch(3, 9)
        self.gridLayout_4.setRowStretch(4, 3)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Age of Empires Replay"))
        self.label.setText(_translate("MainWindow", "WELCOME"))
        self.pushButton_choose.setText(_translate("MainWindow", "Choose File"))
        self.pushButton_start.setText(_translate("MainWindow", "GO TO RESULTS"))
        self.pushButton_download.setText(_translate("MainWindow", "Download File"))
        self.label_2.setText(_translate("MainWindow", "Choose or Download Game Data "))
        self.label_3.setText(_translate("MainWindow", "RESULTS"))
        self.label_7.setText(_translate("MainWindow", "GOLD"))
        self.label_10.setText(_translate("MainWindow", "MILITARY UNITS"))
        self.label_5.setText(_translate("MainWindow", "FOOD"))
        self.label_6.setText(_translate("MainWindow", "WOOD"))
        self.label_8.setText(_translate("MainWindow", "STONE"))
        self.label_9.setText(_translate("MainWindow", "VILLAGERS"))
        self.label_4.setText(_translate("MainWindow", "PLAYER"))
        self.label_11.setText(_translate("MainWindow", "TOTAL SCORE"))
        self.label_12.setText(_translate("MainWindow", "REPLAY"))
        self.pushButton_x.setText(_translate("MainWindow", "X"))
        self.pushButton_4x.setText(_translate("MainWindow", "4X"))
        self.pushButton_2x.setText(_translate("MainWindow", "2X"))
        self.pushButton_16x.setText(_translate("MainWindow", "16X"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))

import icon_rc
