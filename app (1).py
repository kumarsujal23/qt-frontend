# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import utils
from groq import Groq 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 763)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("*{\n"
"border: none;\n"
"background-color: transperent;\n"
"background: transperent;\n"
"padding: 0;\n"
"margin:0;\n"
"color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color: #1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"background-color: #000000;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"background-color:#000000;\n"
"text-align:left;\n"
"padding: 5px 10px;\n"
"text-color: white;\n"
"border-top-left-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#CenterMenuSubContainer {\n"
"background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_4{\n"
"background-color: #000000;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMinimumSize(QtCore.QSize(40, 0))
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.vboxlayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("#HomeBtn:hover{background-color: #1f232a;}\n"
"#otherBtn:hover{background-color: #1f232a;}\n"
"#logsBtn:hover{background-color: #1f232a;}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menuBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBtn.sizePolicy().hasHeightForWidth())
        self.menuBtn.setSizePolicy(sizePolicy)
        self.menuBtn.setMinimumSize(QtCore.QSize(0, 2))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/feather(2)/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.verticalLayout_3.addWidget(self.menuBtn)
        self.HomeBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HomeBtn.sizePolicy().hasHeightForWidth())
        self.HomeBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.HomeBtn.setFont(font)
        self.HomeBtn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/feather(2)/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeBtn.setIcon(icon1)
        self.HomeBtn.setIconSize(QtCore.QSize(24, 24))
        self.HomeBtn.setObjectName("HomeBtn")
        self.verticalLayout_3.addWidget(self.HomeBtn, 0, QtCore.Qt.AlignTop)
        self.logsBtn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logsBtn.sizePolicy().hasHeightForWidth())
        self.logsBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logsBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/feather(2)/printer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logsBtn.setIcon(icon2)
        self.logsBtn.setIconSize(QtCore.QSize(24, 24))
        self.logsBtn.setObjectName("logsBtn")
        self.verticalLayout_3.addWidget(self.logsBtn)
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setStyleSheet("#settingsBtn:hover{background-color: #1f232a;}\n"
"#infoBtn:hover{background-color: #1f232a;}\n"
"#helpBtn:hover{background-color: #1f232a;}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsBtn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsBtn.sizePolicy().hasHeightForWidth())
        self.settingsBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.settingsBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/feather(2)/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon3)
        self.settingsBtn.setIconSize(QtCore.QSize(24, 24))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.infoBtn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoBtn.sizePolicy().hasHeightForWidth())
        self.infoBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infoBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/feather(2)/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoBtn.setIcon(icon4)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.vboxlayout.addWidget(self.leftMenuSubContainer)
        self.horizontalLayout.addWidget(self.leftMenuContainer)
        self.centerMenuContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy)
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centerMenuContainer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mainBodyContainer = QtWidgets.QWidget(self.centerMenuContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setMinimumSize(QtCore.QSize(0, 643))
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy)
        self.headerContainer.setMinimumSize(QtCore.QSize(100, 50))
        self.headerContainer.setMaximumSize(QtCore.QSize(16667, 50))
        self.headerContainer.setStyleSheet("background-color: #1f232a;")
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.XBRestore = QtWidgets.QFrame(self.headerContainer)
        self.XBRestore.setMinimumSize(QtCore.QSize(160, 0))
        self.XBRestore.setMaximumSize(QtCore.QSize(100, 100))
        self.XBRestore.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.XBRestore.setFrameShadow(QtWidgets.QFrame.Raised)
        self.XBRestore.setObjectName("XBRestore")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.XBRestore)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.appicon = QtWidgets.QLabel(self.XBRestore)
        self.appicon.setMaximumSize(QtCore.QSize(50, 50))
        self.appicon.setText("")
        self.appicon.setPixmap(QtGui.QPixmap(":/icons/feather(2)/131-1312148_linux-start-menu-icons-removebg-preview.png"))
        self.appicon.setScaledContents(True)
        self.appicon.setObjectName("appicon")
        self.horizontalLayout_5.addWidget(self.appicon)
        self.appname = QtWidgets.QLabel(self.XBRestore)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.appname.setFont(font)
        self.appname.setStyleSheet("background-color: #1f232a;")
        self.appname.setObjectName("appname")
        self.horizontalLayout_5.addWidget(self.appname)
        self.horizontalLayout_4.addWidget(self.XBRestore)
        self.Navigation = QtWidgets.QFrame(self.headerContainer)
        self.Navigation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navigation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navigation.setObjectName("Navigation")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Navigation)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.minimizeBtn = QtWidgets.QPushButton(self.Navigation)
        self.minimizeBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/feather(2)/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon5)
        self.minimizeBtn.setIconSize(QtCore.QSize(24, 16))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_7.addWidget(self.minimizeBtn)
        self.closeBtn = QtWidgets.QPushButton(self.Navigation)
        self.closeBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/feather(2)/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon6)
        self.closeBtn.setIconSize(QtCore.QSize(16, 16))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_7.addWidget(self.closeBtn)
        self.horizontalLayout_4.addWidget(self.Navigation, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.headerContainer)
        self.mainBodyContents = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContents.sizePolicy().hasHeightForWidth())
        self.mainBodyContents.setSizePolicy(sizePolicy)
        self.mainBodyContents.setMinimumSize(QtCore.QSize(0, 200))
        self.mainBodyContents.setMaximumSize(QtCore.QSize(166667, 1666667))
        self.mainBodyContents.setObjectName("mainBodyContents")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainBodyContents)
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mainContentsContainer = QtWidgets.QWidget(self.mainBodyContents)
        self.mainContentsContainer.setMinimumSize(QtCore.QSize(280, 0))
        self.mainContentsContainer.setObjectName("mainContentsContainer")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Window = QtWidgets.QStackedWidget(self.mainContentsContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Window.sizePolicy().hasHeightForWidth())
        self.Window.setSizePolicy(sizePolicy)
        self.Window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Window.setStyleSheet("#pushButton_2:clicked{\n"
"background-color: rgb(153, 193, 241)\n"
";}\n"
"\n"
"#pushButton_3:clicked{\n"
"background-color: rgb(153, 193, 241)\n"
";}\n"
"\n"
"QComboBox {background-color: rgb(55, 65, 81);  /* Light grey background */\n"
"                font-size: 14px;             /* Font size */\n"
"                border: 2px solid #0078d4;   /* Blue border */\n"
"                border-radius: 5px;          /* Rounded corners */\n"
"                padding: 5px;                /* Padding inside the combo box */\n"
"            }\n"
"\n"
"        \n"
"\n"
"            QComboBox::item:hover {\n"
"                background-color: #000000;   \n"
"                color: white;                 \n"
"            }\n"
"#textEdit_2{\n"
" font-size: 14px;             /* Font size */\n"
"                border: 2px solid #0078d4;   /* Blue border */\n"
"                border-radius: 5px;          /* Rounded corners */\n"
"                padding: 5px;                /* Padding inside the combo box */\n"
"}\n"
"\n"
"#textEdit_3{\n"
" font-size: 14px;             /* Font size */\n"
"                border: 2px solid #0078d4;   /* Blue border */\n"
"                border-radius: 5px;          /* Rounded corners */\n"
"                padding: 5px;                /* Padding inside the combo box */\n"
"}\n"
"#stackedWidget{\n"
" font-size: 14px;             /* Font size */\n"
"                border: 2px solid #0078d4;   /* Blue border */\n"
"                border-radius: 5px;          /* Rounded corners */\n"
"                padding: 5px;                /* Padding inside the combo box */\n"
"}\n"
"#StartBtn:pressed{\n"
"background-color: rgb(74, 122, 235);\n"
"}\n"
"\n"
"#summaryBtn:pressed{\n"
"background-color: rgb(74, 122, 235);\n"
"}")
        self.Window.setObjectName("Window")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget = QtWidgets.QStackedWidget(self.page)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 440, 531, 231))
        self.stackedWidget.setStyleSheet("background-color: #1f232a;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.InformationofSoftware = QtWidgets.QWidget()
        self.InformationofSoftware.setObjectName("InformationofSoftware")
        self.introheader = QtWidgets.QLabel(self.InformationofSoftware)
        self.introheader.setGeometry(QtCore.QRect(30, 20, 211, 31))
        self.introheader.setObjectName("introheader")
        self.infoelaborate = QtWidgets.QLabel(self.InformationofSoftware)
        self.infoelaborate.setGeometry(QtCore.QRect(30, 70, 431, 121))
        self.infoelaborate.setText("")
        self.infoelaborate.setObjectName("infoelaborate")
        self.stackedWidget.addWidget(self.InformationofSoftware)
        self.Analysing = QtWidgets.QWidget()
        self.Analysing.setObjectName("Analysing")
        self.Analysinglabel = QtWidgets.QLabel(self.Analysing)
        self.Analysinglabel.setGeometry(QtCore.QRect(30, 20, 81, 19))
        self.Analysinglabel.setObjectName("Analysinglabel")
        self.stackedWidget.addWidget(self.Analysing)
        self.Recovering = QtWidgets.QWidget()
        self.Recovering.setObjectName("Recovering")
        self.RecoveryLabel = QtWidgets.QLabel(self.Recovering)
        self.RecoveryLabel.setGeometry(QtCore.QRect(20, 20, 151, 19))
        self.RecoveryLabel.setObjectName("RecoveryLabel")
        self.stackedWidget.addWidget(self.Recovering)
        self.Summarise = QtWidgets.QWidget()
        self.Summarise.setObjectName("Summarise")
        self.SummaryLabel = QtWidgets.QLabel(self.Summarise)
        self.SummaryLabel.setGeometry(QtCore.QRect(20, 10, 191, 19))
        self.SummaryLabel.setObjectName("SummaryLabel")
        self.scrollArea = QtWidgets.QScrollArea(self.Summarise)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 491, 161))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 491, 161))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(470, 10, 16, 141))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.Summarise)
        self.DiskLocationLabel = QtWidgets.QLabel(self.page)
        self.DiskLocationLabel.setGeometry(QtCore.QRect(20, 60, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DiskLocationLabel.setFont(font)
        self.DiskLocationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DiskLocationLabel.setObjectName("DiskLocationLabel")
        self.diskLocationInput = QtWidgets.QTextEdit(self.page)
        self.diskLocationInput.setGeometry(QtCore.QRect(20, 90, 241, 41))
        self.diskLocationInput.setStyleSheet("background-color: rgb(55, 65, 81);\n"
"color: #ffffff;")
        self.diskLocationInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diskLocationInput.setTabChangesFocus(True)
        self.diskLocationInput.setObjectName("diskLocationInput")
        self.FilterLabel = QtWidgets.QLabel(self.page)
        self.FilterLabel.setGeometry(QtCore.QRect(40, 170, 451, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.FilterLabel.setFont(font)
        self.FilterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FilterLabel.setObjectName("FilterLabel")
        self.comboBox = QtWidgets.QComboBox(self.page)
        self.comboBox.setGeometry(QtCore.QRect(40, 190, 451, 41))
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(7, "")
        self.StartBtn = QtWidgets.QPushButton(self.page)
        self.StartBtn.setGeometry(QtCore.QRect(40, 280, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.StartBtn.setFont(font)
        self.StartBtn.setStyleSheet("background-color: rgb(37, 99, 235);\n"
"color: rgb(255, 255, 255);")
        self.StartBtn.setObjectName("StartBtn")
        self.StartBtn.pressed.connect(self.on_click_StartBtn)  

        self.summaryBtn = QtWidgets.QPushButton(self.page)
        self.summaryBtn.setGeometry(QtCore.QRect(280, 280, 221, 41))
        self.summaryBtn.pressed.connect(self.on_click_summaryBtn)  

        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        self.summaryBtn.setFont(font)
        self.summaryBtn.setStyleSheet("background-color: rgb(37, 99, 235);\n"
"color: rgb(255, 255, 255);")
        self.summaryBtn.setObjectName("summaryBtn")
        self.RecoveryPathLabel = QtWidgets.QLabel(self.page)
        self.RecoveryPathLabel.setGeometry(QtCore.QRect(280, 60, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.RecoveryPathLabel.setFont(font)
        self.RecoveryPathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RecoveryPathLabel.setObjectName("RecoveryPathLabel")
        self.recoveryBtnInput = QtWidgets.QTextEdit(self.page)
        self.recoveryBtnInput.setGeometry(QtCore.QRect(280, 90, 241, 41))
        self.recoveryBtnInput.setStyleSheet("background-color: rgb(55, 65, 81);\n"
"color: #ffffff;")
        self.recoveryBtnInput.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.recoveryBtnInput.setTabChangesFocus(True)
        self.recoveryBtnInput.setObjectName("recoveryBtnInput")
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(12)
        self.Window.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Window.addWidget(self.page_2)
        self.verticalLayout_11.addWidget(self.Window)
        self.horizontalLayout_8.addWidget(self.mainContentsContainer)
        self.rightMenuContainer = QtWidgets.QWidget(self.mainBodyContents)
        self.rightMenuContainer.setStyleSheet("background-color: #1f232a;")
        self.rightMenuContainer.setObjectName("rightMenuContainer")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.rightMenuSubContainer = QtWidgets.QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName("rightMenuSubContainer")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.AskHeader = QtWidgets.QFrame(self.rightMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AskHeader.sizePolicy().hasHeightForWidth())
        self.AskHeader.setSizePolicy(sizePolicy)
        self.AskHeader.setMinimumSize(QtCore.QSize(187, 0))
        self.AskHeader.setMaximumSize(QtCore.QSize(16777215, 30))
        self.AskHeader.setStyleSheet("")
        self.AskHeader.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AskHeader.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AskHeader.setObjectName("AskHeader")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.AskHeader)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.AskHeader)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_9.setStyleSheet("background-color: #1f232a;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/feather(2)/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon7)
        self.pushButton_9.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.verticalLayout_9.addWidget(self.AskHeader)
        self.AskAI = QtWidgets.QWidget(self.rightMenuSubContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AskAI.sizePolicy().hasHeightForWidth())
        self.AskAI.setSizePolicy(sizePolicy)
        self.AskAI.setMinimumSize(QtCore.QSize(300, 635))
        self.AskAI.setStyleSheet("background-color: #1f232a;")
        self.AskAI.setObjectName("AskAI")
        self.chatOutput = QtWidgets.QPlainTextEdit(self.AskAI)
        self.chatOutput.setGeometry(QtCore.QRect(23, 29, 251, 551))
        self.chatOutput.setMinimumSize(QtCore.QSize(0, 300))
        self.chatOutput.setObjectName("AItextout")
        self.chatInput = QtWidgets.QTextEdit(self.AskAI)
        self.chatInput.setGeometry(QtCore.QRect(20, 589, 271, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatInput.sizePolicy().hasHeightForWidth())
        self.chatInput.setSizePolicy(sizePolicy)
        self.chatInput.setStyleSheet("background-color: #ffffff;\n"
"color: black;\n"
"border-radius: 25px;")
        self.chatInput.setObjectName("AIinput")
        self.chatSend = QtWidgets.QPushButton(self.AskAI)
        self.chatSend.setGeometry(QtCore.QRect(250, 600, 31, 31))
        self.chatSend.setMaximumSize(QtCore.QSize(16777215, 16777213))
        self.chatSend.setStyleSheet("border-radius: 10px;\n"
"background-color: black;")
        self.chatSend.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/feather(2)/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chatSend.setIcon(icon8)
        self.chatSend.setIconSize(QtCore.QSize(24, 24))
        self.chatSend.setObjectName("chatSend")
        self.verticalLayout_9.addWidget(self.AskAI)
        self.verticalLayout_8.addWidget(self.rightMenuSubContainer)
        self.horizontalLayout_8.addWidget(self.rightMenuContainer)
        self.verticalLayout.addWidget(self.mainBodyContents)
        self.horizontalLayout_3.addWidget(self.mainBodyContainer)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click_StartBtn(self):
        # Change the background color of the button when it's clicked
        self.StartBtn.setStyleSheet("background-color: rgb(74, 122, 235);")
        self.stackedWidget.setCurrentIndex(2)
    
    def on_click_summaryBtn(self):
        # Change the background color of the button when it's clicked
        self.summaryBtn.setStyleSheet("background-color: rgb(74, 122, 235);")
        self.stackedWidget.setCurrentIndex(3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setText(_translate("MainWindow", "Menu"))
        self.HomeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.HomeBtn.setText(_translate("MainWindow", " Home"))
        self.logsBtn.setToolTip(_translate("MainWindow", "Reports/Logs"))
        self.logsBtn.setText(_translate("MainWindow", " Logs"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "Settings"))
        self.settingsBtn.setText(_translate("MainWindow", " Settings"))
        self.infoBtn.setToolTip(_translate("MainWindow", "Info"))
        self.infoBtn.setText(_translate("MainWindow", " Info"))
        self.appname.setText(_translate("MainWindow", "  XBRestore"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Minimize Window"))
        self.closeBtn.setToolTip(_translate("MainWindow", "CloseWindow"))
        self.introheader.setText(_translate("MainWindow", "This is a file-recovery software."))
        self.Analysinglabel.setText(_translate("MainWindow", "Analysing..."))
        self.SummaryLabel.setText(_translate("MainWindow", "Summary of recovered files"))
        self.DiskLocationLabel.setText(_translate("MainWindow", "Disk Location"))
        self.diskLocationInput.setPlaceholderText(_translate("MainWindow", "Provide Disk Location"))
        self.FilterLabel.setText(_translate("MainWindow", "Filter the type of files to recover"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", ".txt"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Text-based documents"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Archive files"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Image-based documents"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Executable binaries"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Script files"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Database"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Recover all"))
        self.StartBtn.setText(_translate("MainWindow", "Start Recovery process"))
        self.summaryBtn.setText(_translate("MainWindow", "Summary"))
        self.RecoveryPathLabel.setText(_translate("MainWindow", "Recovery Path"))
        self.recoveryBtnInput.setPlaceholderText(_translate("MainWindow", "Provide Recovery Path"))
        self.label_10.setText(_translate("MainWindow", "Logs"))
        self.pushButton_9.setToolTip(_translate("MainWindow", "close menu"))
        self.pushButton_9.setText(_translate("MainWindow", "Ask AI for Help"))

        self.chatSend.clicked.connect(self.handleChatSend)

    def handleChatSend(self):
        user_input = self.chatInput.toPlainText().strip()
        if not user_input:
            self.chatOutput.setPlainText("Please enter a message.")
            return
        
        client = Groq(
        api_key="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" # hehe
        )
        
        try:
            prefix="you are a file recovery tool for btrfs and xfs file system designed by team btrfs-bandits from IIT-KGP. Users wiil ask you for your help in revovey of files and how this recovery works or the file system works. help the users with it. the following is user's promt:-"
            chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prefix + user_input}
            ],
            model="llama3-8b-8192",
            stream=False,
            )
            
            response_content = chat_completion.choices[0].message.content
            self.chatOutput.setPlainText(response_content)
        
        except Exception as e:
            self.chatOutput.setText(f"An error occurred: {str(e)}")



        def paternFind(self):
            index = self.comboBox.currentIndex()

            if index == 0:
                self.pattern = ".txt"
            elif index == 1:
                self.pattern = ".tar"
            elif index == 2:
                self.pattern = ".jpg"
            elif index == 3:
                self.pattern = ".exe"
            elif index == 4:
                self.pattern = ".py"
            elif index == 5:
                self.pattern = ".db"
            elif index == 6:
                self.pattern = ".*"
            else:
                self.pattern = "" 
            return self.pattern

        self.StartBtn.clicked.connect(lambda: utils.run_btrfs_recover_script(
            self.diskLocationInput.toPlainText(), self.recoveryBtnInput.toPlainText(), paternFind(self), "recover"))
import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
