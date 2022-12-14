# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        MainWindow.setMinimumSize(QtCore.QSize(700, 550))
        MainWindow.setStyleSheet("background-color: rgb(21, 13, 36);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(21, 13, 36);")
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(211, 35, 156);")
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setIndent(-1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bit_1 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_1.setFont(font)
        self.bit_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_1.setObjectName("bit_1")
        self.horizontalLayout.addWidget(self.bit_1)
        self.bit_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_2.setFont(font)
        self.bit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_2.setObjectName("bit_2")
        self.horizontalLayout.addWidget(self.bit_2)
        self.bit_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_3.setFont(font)
        self.bit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_3.setObjectName("bit_3")
        self.horizontalLayout.addWidget(self.bit_3)
        self.bit_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_4.setFont(font)
        self.bit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_4.setObjectName("bit_4")
        self.horizontalLayout.addWidget(self.bit_4)
        self.bit_5 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_5.setFont(font)
        self.bit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_5.setObjectName("bit_5")
        self.horizontalLayout.addWidget(self.bit_5)
        self.bit_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_6.setFont(font)
        self.bit_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_6.setObjectName("bit_6")
        self.horizontalLayout.addWidget(self.bit_6)
        self.bit_7 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_7.setFont(font)
        self.bit_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_7.setObjectName("bit_7")
        self.horizontalLayout.addWidget(self.bit_7)
        self.bit_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_8.setFont(font)
        self.bit_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_8.setObjectName("bit_8")
        self.horizontalLayout.addWidget(self.bit_8)
        self.bit_9 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_9.setFont(font)
        self.bit_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bit_9.setLineWidth(0)
        self.bit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_9.setObjectName("bit_9")
        self.horizontalLayout.addWidget(self.bit_9)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.random_btn = QtWidgets.QPushButton(self.frame_4)
        self.random_btn.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(12)
        self.random_btn.setFont(font)
        self.random_btn.setStyleSheet("QPushButton{\n"
"color: White;\n"
"background-color: rgb(41, 27, 68);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(46, 32, 73);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(31, 17, 58);\n"
"}")
        self.random_btn.setIconSize(QtCore.QSize(20, 50))
        self.random_btn.setObjectName("random_btn")
        self.horizontalLayout_3.addWidget(self.random_btn)
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.bit_0 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(30)
        self.bit_0.setFont(font)
        self.bit_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_0.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_0.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_0.setObjectName("bit_0")
        self.horizontalLayout_3.addWidget(self.bit_0)
        spacerItem7 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.answer_btn = QtWidgets.QPushButton(self.frame_4)
        self.answer_btn.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(12)
        self.answer_btn.setFont(font)
        self.answer_btn.setStyleSheet("QPushButton{\n"
"color: White;\n"
"background-color: rgb(41, 27, 68);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(46, 32, 73);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(31, 17, 58);\n"
"}")
        self.answer_btn.setObjectName("answer_btn")
        self.horizontalLayout_3.addWidget(self.answer_btn)
        spacerItem8 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addWidget(self.frame_4)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_2.addItem(spacerItem10, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color: rgb(61, 27, 100);")
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem11, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem12, 1, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(211, 35, 156);")
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setIndent(-1)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        spacerItem14 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.frame_7.setFont(font)
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem15 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem15, 0, 0, 1, 1)
        self.bit_11 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_11.setFont(font)
        self.bit_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_11.setObjectName("bit_11")
        self.gridLayout_4.addWidget(self.bit_11, 0, 1, 1, 1)
        self.bit_12 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_12.setFont(font)
        self.bit_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_12.setObjectName("bit_12")
        self.gridLayout_4.addWidget(self.bit_12, 0, 2, 1, 1)
        self.bit_13 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_13.setFont(font)
        self.bit_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_13.setObjectName("bit_13")
        self.gridLayout_4.addWidget(self.bit_13, 0, 3, 1, 1)
        self.bit_14 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_14.setFont(font)
        self.bit_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_14.setObjectName("bit_14")
        self.gridLayout_4.addWidget(self.bit_14, 0, 4, 1, 1)
        self.bit_15 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_15.setFont(font)
        self.bit_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_15.setObjectName("bit_15")
        self.gridLayout_4.addWidget(self.bit_15, 0, 5, 1, 1)
        self.bit_16 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_16.setFont(font)
        self.bit_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_16.setObjectName("bit_16")
        self.gridLayout_4.addWidget(self.bit_16, 0, 6, 1, 1)
        self.bit_17 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_17.setFont(font)
        self.bit_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_17.setObjectName("bit_17")
        self.gridLayout_4.addWidget(self.bit_17, 0, 7, 1, 1)
        self.bit_18 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_18.setFont(font)
        self.bit_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_18.setObjectName("bit_18")
        self.gridLayout_4.addWidget(self.bit_18, 0, 8, 1, 1)
        self.bit_19 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(36)
        self.bit_19.setFont(font)
        self.bit_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bit_19.setLineWidth(0)
        self.bit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_19.setObjectName("bit_19")
        self.gridLayout_4.addWidget(self.bit_19, 0, 9, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem16, 0, 10, 1, 1)
        self.bit_21 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_21.setFont(font)
        self.bit_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_21.setStyleSheet("color: rgb(255, 234, 75);")
        self.bit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_21.setObjectName("bit_21")
        self.gridLayout_4.addWidget(self.bit_21, 1, 1, 1, 1)
        self.bit_22 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_22.setFont(font)
        self.bit_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_22.setStyleSheet("color: rgb(255, 234, 75);")
        self.bit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_22.setObjectName("bit_22")
        self.gridLayout_4.addWidget(self.bit_22, 1, 2, 1, 1)
        self.bit_23 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_23.setFont(font)
        self.bit_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_23.setStyleSheet("color: rgb(255, 234, 75);")
        self.bit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_23.setObjectName("bit_23")
        self.gridLayout_4.addWidget(self.bit_23, 1, 3, 1, 1)
        self.bit_24 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_24.setFont(font)
        self.bit_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_24.setStyleSheet("color: rgb(255, 234, 75);")
        self.bit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_24.setObjectName("bit_24")
        self.gridLayout_4.addWidget(self.bit_24, 1, 4, 1, 1)
        self.bit_25 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_25.setFont(font)
        self.bit_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_25.setStyleSheet("color: rgb(255, 234, 75);")
        self.bit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_25.setObjectName("bit_25")
        self.gridLayout_4.addWidget(self.bit_25, 1, 5, 1, 1)
        self.bit_26 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_26.setFont(font)
        self.bit_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_26.setStyleSheet("color: rgb(211, 35, 156);")
        self.bit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_26.setObjectName("bit_26")
        self.gridLayout_4.addWidget(self.bit_26, 1, 6, 1, 1)
        self.bit_27 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_27.setFont(font)
        self.bit_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_27.setStyleSheet("color: rgb(211, 35, 156);")
        self.bit_27.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_27.setObjectName("bit_27")
        self.gridLayout_4.addWidget(self.bit_27, 1, 7, 1, 1)
        self.bit_28 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_28.setFont(font)
        self.bit_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_28.setStyleSheet("color: rgb(211, 35, 156);")
        self.bit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_28.setObjectName("bit_28")
        self.gridLayout_4.addWidget(self.bit_28, 1, 8, 1, 1)
        self.bit_29 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(15)
        self.bit_29.setFont(font)
        self.bit_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_29.setStyleSheet("color: rgb(211, 35, 156);")
        self.bit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_29.setObjectName("bit_29")
        self.gridLayout_4.addWidget(self.bit_29, 1, 9, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem17 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(85, 170, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        spacerItem18 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem18)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem19 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.random_btn_2 = QtWidgets.QPushButton(self.frame_8)
        self.random_btn_2.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(12)
        self.random_btn_2.setFont(font)
        self.random_btn_2.setStyleSheet("QPushButton{\n"
"color: White;\n"
"background-color: rgb(41, 27, 68);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(46, 32, 73);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(31, 17, 58);\n"
"}")
        self.random_btn_2.setIconSize(QtCore.QSize(20, 50))
        self.random_btn_2.setObjectName("random_btn_2")
        self.horizontalLayout_6.addWidget(self.random_btn_2)
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.bit_10 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(30)
        self.bit_10.setFont(font)
        self.bit_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bit_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.bit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.bit_10.setObjectName("bit_10")
        self.horizontalLayout_6.addWidget(self.bit_10)
        spacerItem21 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem21)
        self.answer_btn_2 = QtWidgets.QPushButton(self.frame_8)
        self.answer_btn_2.setMinimumSize(QtCore.QSize(150, 100))
        font = QtGui.QFont()
        font.setFamily("ROG Fonts")
        font.setPointSize(12)
        self.answer_btn_2.setFont(font)
        self.answer_btn_2.setStyleSheet("QPushButton{\n"
"color: White;\n"
"background-color: rgb(41, 27, 68);\n"
"border-style: outset;\n"
"border-radius: 10px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(46, 32, 73);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgb(31, 17, 58);\n"
"}")
        self.answer_btn_2.setObjectName("answer_btn_2")
        self.horizontalLayout_6.addWidget(self.answer_btn_2)
        spacerItem22 = QtWidgets.QSpacerItem(76, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem22)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.gridLayout_3.addWidget(self.frame_5, 1, 1, 2, 1)
        spacerItem23 = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem23, 2, 2, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem24, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Parity bit puzzle!"))
        self.bit_1.setText(_translate("MainWindow", "1"))
        self.bit_2.setText(_translate("MainWindow", "1"))
        self.bit_3.setText(_translate("MainWindow", "1"))
        self.bit_4.setText(_translate("MainWindow", "1"))
        self.bit_5.setText(_translate("MainWindow", "1"))
        self.bit_6.setText(_translate("MainWindow", "1"))
        self.bit_7.setText(_translate("MainWindow", "1"))
        self.bit_8.setText(_translate("MainWindow", "1"))
        self.bit_9.setText(_translate("MainWindow", "1"))
        self.random_btn.setText(_translate("MainWindow", "Random"))
        self.bit_0.setText(_translate("MainWindow", "Odd"))
        self.answer_btn.setText(_translate("MainWindow", "ANSWER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Simple"))
        self.label_11.setText(_translate("MainWindow", "Hamming Parity bit!"))
        self.bit_11.setText(_translate("MainWindow", "1"))
        self.bit_12.setText(_translate("MainWindow", "1"))
        self.bit_13.setText(_translate("MainWindow", "1"))
        self.bit_14.setText(_translate("MainWindow", "1"))
        self.bit_15.setText(_translate("MainWindow", "1"))
        self.bit_16.setText(_translate("MainWindow", "1"))
        self.bit_17.setText(_translate("MainWindow", "1"))
        self.bit_18.setText(_translate("MainWindow", "1"))
        self.bit_19.setText(_translate("MainWindow", "1"))
        self.bit_21.setText(_translate("MainWindow", "1"))
        self.bit_22.setText(_translate("MainWindow", "2"))
        self.bit_23.setText(_translate("MainWindow", "3"))
        self.bit_24.setText(_translate("MainWindow", "4"))
        self.bit_25.setText(_translate("MainWindow", "5"))
        self.bit_26.setText(_translate("MainWindow", "6"))
        self.bit_27.setText(_translate("MainWindow", "7"))
        self.bit_28.setText(_translate("MainWindow", "8"))
        self.bit_29.setText(_translate("MainWindow", "9"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>1 + 3 + 5 + 6<br/>1 + 2 + 4 + 7<br/>2 + 3 + 8<br/>4 + 5 + 9</p></body></html>"))
        self.random_btn_2.setText(_translate("MainWindow", "Random"))
        self.bit_10.setText(_translate("MainWindow", "Odd"))
        self.answer_btn_2.setText(_translate("MainWindow", "ANSWER"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Hamming"))
