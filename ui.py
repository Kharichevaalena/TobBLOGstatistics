import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import processing

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1024)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1440, 1024))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Main = QtWidgets.QWidget()
        self.tab_Main.setObjectName("tab_Main")
        self.font_Main = QtWidgets.QLabel(self.tab_Main)
        self.font_Main.setGeometry(QtCore.QRect(0, 0, 1440, 1024))
        self.font_Main.setText("")
        self.font_Main.setPixmap(QtGui.QPixmap("МЕДВЕДЬ-02-02 1.png"))
        self.font_Main.setObjectName("font_Main")
        self.label_TopBlog = QtWidgets.QLabel(self.tab_Main)
        self.label_TopBlog.setGeometry(QtCore.QRect(363, 0, 320, 180))
        self.label_TopBlog.setText("")
        self.label_TopBlog.setPixmap(QtGui.QPixmap("Artboard 7@4x 1.png"))
        self.label_TopBlog.setObjectName("label_TopBlog")
        self.label_X = QtWidgets.QLabel(self.tab_Main)
        self.label_X.setGeometry(QtCore.QRect(702, 72, 41, 41))
        self.label_X.setText("")
        self.label_X.setPixmap(QtGui.QPixmap("Vector.png"))
        self.label_X.setObjectName("label_X")
        self.label_GroupForest = QtWidgets.QLabel(self.tab_Main)
        self.label_GroupForest.setGeometry(QtCore.QRect(738, 14, 271, 152))
        self.label_GroupForest.setText("")
        self.label_GroupForest.setPixmap(QtGui.QPixmap("Artboard 6@4x 2.png"))
        self.label_GroupForest.setObjectName("label_GroupForest")
        self.label_Text = QtWidgets.QLabel(self.tab_Main)
        self.label_Text.setGeometry(QtCore.QRect(135, 224, 1168, 47))
        self.label_Text.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 40px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_Text.setObjectName("label_Text")
        self.label_YT = QtWidgets.QLabel(self.tab_Main)
        self.label_YT.setGeometry(QtCore.QRect(206, 468, 122, 30))
        self.label_YT.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_YT.setAlignment(QtCore.Qt.AlignCenter)
        self.label_YT.setObjectName("label_YT")
        self.label_TG = QtWidgets.QLabel(self.tab_Main)
        self.label_TG.setGeometry(QtCore.QRect(508, 468, 122, 30))
        self.label_TG.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_TG.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TG.setObjectName("label_TG")
        self.label_VK = QtWidgets.QLabel(self.tab_Main)
        self.label_VK.setGeometry(QtCore.QRect(810, 468, 122, 30))
        self.label_VK.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_VK.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VK.setObjectName("label_VK")
        self.label_DZ = QtWidgets.QLabel(self.tab_Main)
        self.label_DZ.setGeometry(QtCore.QRect(1112, 468, 122, 30))
        self.label_DZ.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 24px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_DZ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DZ.setObjectName("label_DZ")
        self.Button_YT = QtWidgets.QPushButton(self.tab_Main)
        self.Button_YT.setGeometry(QtCore.QRect(195, 315, 144, 144))
        self.Button_YT.setStyleSheet("backgroung-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"")
        self.Button_YT.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ЮТ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_YT.setIcon(icon)
        self.Button_YT.setIconSize(QtCore.QSize(144, 144))
        self.Button_YT.setObjectName("Button_YT")
        self.Button_YT.clicked.connect(lambda: self.Choice_SocialNet(1))
        self.Button_TG = QtWidgets.QPushButton(self.tab_Main)
        self.Button_TG.setGeometry(QtCore.QRect(497, 315, 144, 144))
        self.Button_TG.setStyleSheet("backgroung-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"")
        self.Button_TG.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ТГ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_TG.setIcon(icon1)
        self.Button_TG.setIconSize(QtCore.QSize(144, 144))
        self.Button_TG.setObjectName("Button_TG")
        self.Button_TG.clicked.connect(lambda: self.Choice_SocialNet(2))
        self.Button_VK = QtWidgets.QPushButton(self.tab_Main)
        self.Button_VK.setGeometry(QtCore.QRect(799, 315, 144, 144))
        self.Button_VK.setStyleSheet("backgroung-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.Button_VK.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ВК.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_VK.setIcon(icon2)
        self.Button_VK.setIconSize(QtCore.QSize(144, 144))
        self.Button_VK.setObjectName("Button_VK")
        self.Button_VK.clicked.connect(lambda: self.Choice_SocialNet(mode=3))
        self.Button_DZ = QtWidgets.QPushButton(self.tab_Main)
        self.Button_DZ.setGeometry(QtCore.QRect(1102, 315, 144, 144))
        self.Button_DZ.setStyleSheet("backgroung-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.Button_DZ.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ДЗЕН.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_DZ.setIcon(icon3)
        self.Button_DZ.setIconSize(QtCore.QSize(144, 144))
        self.Button_DZ.setObjectName("Button_DZ")
        self.Button_DZ.clicked.connect(lambda: self.Choice_SocialNet(4))
        self.tabWidget.addTab(self.tab_Main, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.font = QtWidgets.QLabel(self.widget)
        self.font.setGeometry(QtCore.QRect(0, 0, 1440, 1024))
        self.font.setText("")
        self.font.setPixmap(QtGui.QPixmap("мило-03 1.png"))
        self.font.setObjectName("font")
        self.label_GroupForest_2 = QtWidgets.QLabel(self.widget)
        self.label_GroupForest_2.setGeometry(QtCore.QRect(738, 14, 271, 152))
        self.label_GroupForest_2.setText("")
        self.label_GroupForest_2.setPixmap(QtGui.QPixmap("Artboard 6@4x 2.png"))
        self.label_GroupForest_2.setObjectName("label_GroupForest_2")
        self.label_TopBlog_2 = QtWidgets.QLabel(self.widget)
        self.label_TopBlog_2.setGeometry(QtCore.QRect(363, 0, 320, 180))
        self.label_TopBlog_2.setText("")
        self.label_TopBlog_2.setPixmap(QtGui.QPixmap("Artboard 7@4x 1.png"))
        self.label_TopBlog_2.setObjectName("label_TopBlog_2")
        self.label_X_2 = QtWidgets.QLabel(self.widget)
        self.label_X_2.setGeometry(QtCore.QRect(702, 72, 41, 41))
        self.label_X_2.setText("")
        self.label_X_2.setPixmap(QtGui.QPixmap("Vector.png"))
        self.label_X_2.setObjectName("label_X_2")
        self.Button_loadImage = QtWidgets.QPushButton(self.widget)
        self.Button_loadImage.setGeometry(QtCore.QRect(110, 374, 228, 228))
        font = QtGui.QFont()
        font.setFamily("Work Sans")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.Button_loadImage.setFont(font)
        self.Button_loadImage.setStyleSheet("display: flex;\n"
"width: 228px;\n"
"height: 228px;\n"
"padding: 92px 18px;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"gap: 12px;\n"
"flex-shrink: 0;\n"
"border-radius: 30px;\n"
"background: rgba(244, 235, 196, 0.30);\n"
"color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.Button_loadImage.setIconSize(QtCore.QSize(45, 45))
        self.Button_loadImage.setObjectName("Button_loadImage")
        self.Button_loadImage.clicked.connect(self.open_file)
        self.label_TextChoice = QtWidgets.QLabel(self.widget)
        self.label_TextChoice.setGeometry(QtCore.QRect(363, 235, 436, 75))
        self.label_TextChoice.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 64px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;\n"
"")
        self.label_TextChoice.setObjectName("label_TextChoice")
        self.Button_LoadFolder = QtWidgets.QPushButton(self.widget)
        self.Button_LoadFolder.setGeometry(QtCore.QRect(110, 632, 228, 228))
        self.Button_LoadFolder.setStyleSheet("display: flex;\n"
"width: 228px;\n"
"height: 228px;\n"
"padding: 92px 18px;\n"
"flex-direction: column;\n"
"align-items: center;\n"
"gap: 12px;\n"
"flex-shrink: 0;\n"
"border-radius: 30px;\n"
"background: rgba(244, 235, 196, 0.30);\n"
"\n"
"color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.Button_LoadFolder.setObjectName("Button_LoadFolder")
        self.Button_LoadFolder.clicked.connect(self.open_dir)
        self.label_ButtonImage = QtWidgets.QLabel(self.widget)
        self.label_ButtonImage.setGeometry(QtCore.QRect(120, 460, 210, 24))
        font = QtGui.QFont()
        font.setFamily("Work Sans")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_ButtonImage.setFont(font)
        self.label_ButtonImage.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_ButtonImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ButtonImage.setObjectName("label_ButtonImage")
        self.label_LoadImage2 = QtWidgets.QLabel(self.widget)
        self.label_LoadImage2.setGeometry(QtCore.QRect(201, 502, 45, 45))
        self.label_LoadImage2.setText("")
        self.label_LoadImage2.setPixmap(QtGui.QPixmap("Group 7.png"))
        self.label_LoadImage2.setObjectName("label_LoadImage2")
        self.label_LoaDFolder2 = QtWidgets.QLabel(self.widget)
        self.label_LoaDFolder2.setGeometry(QtCore.QRect(201, 760, 45, 45))
        self.label_LoaDFolder2.setText("")
        self.label_LoaDFolder2.setPixmap(QtGui.QPixmap("Group 7.png"))
        self.label_LoaDFolder2.setObjectName("label_LoaDFolder2")
        self.Button_Exit = QtWidgets.QPushButton(self.widget)
        self.Button_Exit.setGeometry(QtCore.QRect(58, 930, 93, 40))
        self.Button_Exit.setStyleSheet("backgroung-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"")
        self.Button_Exit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Arrow 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Exit.setIcon(icon4)
        self.Button_Exit.setIconSize(QtCore.QSize(40, 217))
        self.Button_Exit.setObjectName("Button_Exit")
        self.Button_Exit.clicked.connect(self.Exit)
        self.label_SocialNet2 = QtWidgets.QLabel(self.widget)
        self.label_SocialNet2.setGeometry(QtCore.QRect(877, 352, 122, 30))
        self.label_SocialNet2.setText("")
        self.label_SocialNet2.setStyleSheet("color: #F4EBC5;\n"
                                    "text-align: center;\n"
                                    "font-family: Work Sans;\n"
                                    "font-size: 24px;\n"
                                    "font-style: normal;\n"
                                    "font-weight: 700;\n"
                                    "line-height: normal;")
        self.label_SocialNet2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_SocialNet2.setObjectName("label_SocialNet2")
        self.label_SocialNet = QtWidgets.QLabel(self.widget)
        self.label_SocialNet.setGeometry(QtCore.QRect(866, 200, 144, 144))
        self.label_SocialNet.setText("")
        self.label_SocialNet.setObjectName("label_SocialNet")
        self.label_resultImg = QtWidgets.QLabel(self.widget)
        self.label_resultImg.setGeometry(QtCore.QRect(691, 488, 493, 265))
        self.label_resultImg.setStyleSheet("border-radius: 30px;\n"
"background: rgba(244, 235, 197, 0.30);")
        self.label_resultImg.setText("")
        self.label_resultImg.setObjectName("label_resultImg")
        self.label_resultImg.setVisible(False)
        self.label_followers = QtWidgets.QLabel(self.widget)
        self.label_followers.setGeometry(QtCore.QRect(707, 568, 388, 30))
        self.label_followers.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_followers.setObjectName("label_followers")
        self.label_followers.setVisible(False)
        self.label_followers2 = QtWidgets.QLabel(self.widget)
        self.label_followers2.setGeometry(QtCore.QRect(707, 605, 800, 30))
        self.label_followers2.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_followers2.setObjectName("label_followers2")
        self.label_followers2.setVisible(False)
        self.label_views = QtWidgets.QLabel(self.widget)
        self.label_views.setGeometry(QtCore.QRect(707, 630, 316, 30))
        self.label_views.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_views.setObjectName("label_views")
        self.label_views.setVisible(False)
        self.label_views2 = QtWidgets.QLabel(self.widget)
        self.label_views2.setGeometry(QtCore.QRect(707, 663, 800, 30))
        self.label_views2.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_views2.setObjectName("label_views2")
        self.label_views2.setVisible(False)
        self.Button_Download = QtWidgets.QPushButton(self.widget)
        self.Button_Download.setGeometry(QtCore.QRect(824, 488, 228, 228))
        self.Button_Download.setStyleSheet("backgroung-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.Button_Download.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ПАПКА-01 1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_Download.setIcon(icon5)
        self.Button_Download.setIconSize(QtCore.QSize(228, 228))
        self.Button_Download.setObjectName("Button_Download")
        self.Button_Download.setEnabled(False)
        self.Button_Download.setVisible(False)
        self.Button_Download.clicked.connect(self.CopyFileResult)
        self.label_Download = QtWidgets.QLabel(self.widget)
        self.label_Download.setGeometry(QtCore.QRect(874, 728, 128, 24))
        self.label_Download.setStyleSheet("color: #F4EBC5;\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 15px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_Download.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Download.setObjectName("label_Download")
        self.label_Download.setVisible(False)
        self.label_Info = QtWidgets.QLabel(self.widget)
        self.label_Info.setGeometry(QtCore.QRect(455, 488, 698, 24))
        self.label_Info.setStyleSheet("color: rgba(244, 235, 197, 0.60);\n"
"text-align: center;\n"
"font-family: Work Sans;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"line-height: normal;")
        self.label_Info.setObjectName("label_Info")
        self.label_paw = QtWidgets.QLabel(self.widget)
        self.label_paw.setGeometry(QtCore.QRect(810, 770, 251, 241))
        self.label_paw.setText("")
        self.label_paw.setPixmap(QtGui.QPixmap("лес-04 1.png"))
        self.label_paw.setObjectName("label_paw")
        self.label_paw2 = QtWidgets.QLabel(self.widget)
        self.label_paw2.setGeometry(QtCore.QRect(950, 660, 171, 141))
        self.label_paw2.setStyleSheet("\n"
"transform: rotate(7.584deg);")
        self.label_paw2.setText("")
        self.label_paw2.setPixmap(QtGui.QPixmap("лес-04 3.png"))
        self.label_paw2.setObjectName("label_paw2")
        self.label_paw3 = QtWidgets.QLabel(self.widget)
        self.label_paw3.setGeometry(QtCore.QRect(1010, 780, 141, 151))
        self.label_paw3.setText("")
        self.label_paw3.setPixmap(QtGui.QPixmap("лес-04 2.png"))
        self.label_paw3.setObjectName("label_paw3")
        self.label_paw4 = QtWidgets.QLabel(self.widget)
        self.label_paw4.setGeometry(QtCore.QRect(1140, 670, 141, 151))
        self.label_paw4.setText("")
        self.label_paw4.setPixmap(QtGui.QPixmap("лес-04 2.png"))
        self.label_paw4.setObjectName("label_paw4")
        self.label_paw5 = QtWidgets.QLabel(self.widget)
        self.label_paw5.setGeometry(QtCore.QRect(1090, 560, 171, 141))
        self.label_paw5.setStyleSheet("\n"
"transform: rotate(7.584deg);")
        self.label_paw5.setText("")
        self.label_paw5.setPixmap(QtGui.QPixmap("лес-04 3.png"))
        self.label_paw5.setObjectName("label_paw5")
        self.label_paw6 = QtWidgets.QLabel(self.widget)
        self.label_paw6.setGeometry(QtCore.QRect(1270, 550, 141, 151))
        self.label_paw6.setText("")
        self.label_paw6.setPixmap(QtGui.QPixmap("лес-04 2.png"))
        self.label_paw6.setObjectName("label_paw6")
        self.label_paw7 = QtWidgets.QLabel(self.widget)
        self.label_paw7.setGeometry(QtCore.QRect(1240, 450, 171, 141))
        self.label_paw7.setStyleSheet("\n"
"transform: rotate(7.584deg);")
        self.label_paw7.setText("")
        self.label_paw7.setPixmap(QtGui.QPixmap("лес-04 3.png"))
        self.label_paw7.setObjectName("label_paw7")
        self.tabWidget.addTab(self.widget, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Топ блог Х Группа лес"))
        self.label_Text.setText(_translate("MainWindow", "Выбери социальную сеть для распознавания KPI блога"))
        self.label_YT.setText(_translate("MainWindow", "YouTube"))
        self.label_TG.setText(_translate("MainWindow", "Telegram"))
        self.label_VK.setText(_translate("MainWindow", "VK"))
        self.label_DZ.setText(_translate("MainWindow", "Дзен"))
        self.label_TextChoice.setText(_translate("MainWindow", "Вы выбрали:"))
        self.Button_LoadFolder.setText(_translate("MainWindow", "ЗАГРУЗИТЬ ПАПКУ\n"""))
        self.label_ButtonImage.setText(_translate("MainWindow", "ЗАГРУЗИТЬ ИЗОБРАЖЕНИЕ"))
        self.label_followers.setText(_translate("MainWindow", "Количество подписчиков:"))
        self.label_views.setText(_translate("MainWindow", "Просмотры за месяц:"))
        self.label_Download.setText(_translate("MainWindow", "СКАЧАТЬ"))
        self.label_Info.setText(_translate("MainWindow", "Загрузите изображение в одном из форматов: jpeg, png, jpg, pdf, docx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", ""))

    def CopyFileResult(self):
        import shutil
        from tkinter import filedialog
        self.dirname = filedialog.askdirectory()
        mode = self.label_SocialNet2.text()
        if mode == "YouTube":
            file1 = 'yt1.xlsx'
            file2 = 'yt2.xlsx'
            shutil.copy(file1, self.dirname + '/')
            shutil.copy(file2, self.dirname + '/')

        elif mode == "Telegram":
            file = 'tg.xlsx'
            shutil.copy(file, self.dirname + '/')

        elif mode == "VK":
            file = 'vk.xlsx'
            shutil.copy(file, self.dirname + '/')

        elif mode == "Дзен":
            file = 'zn.xlsx'
            shutil.copy(file, self.dirname + '/')

    def Start_Settings(self):
        self.label_Info.setVisible(True)
        self.label_paw.setVisible(True)
        self.label_paw2.setVisible(True)
        self.label_paw3.setVisible(True)
        self.label_paw4.setVisible(True)
        self.label_paw5.setVisible(True)
        self.label_paw6.setVisible(True)
        self.label_paw7.setVisible(True)
        self.label_resultImg.setVisible(False)
        self.label_followers.setVisible(False)
        self.label_followers2.setVisible(False)
        self.label_views.setVisible(False)
        self.label_views2.setVisible(False)
        self.Button_Download.setVisible(False)
        self.Button_Download.setEnabled(False)
        self.label_Download.setVisible(False)
        self.label_TextChoice.setText("Вы выбрали:")

    def Choice_SocialNet(self, mode):
        if mode == 1:
            self.Start_Settings()
            self.label_SocialNet.setPixmap(QtGui.QPixmap("ЮТ.png"))
            self.label_SocialNet2.setText("YouTube")
            self.label_followers.setText("Количество подписчиков:")
            self.label_views.setText("Просмотры за месяц:")
        elif mode == 2:
            self.Start_Settings()
            self.label_SocialNet.setPixmap(QtGui.QPixmap("ТГ.png"))
            self.label_SocialNet2.setText("Telegram")
            self.label_followers.setText("ERR/VR:")
            self.label_views.setText(" ")
        elif mode == 3:
            self.Start_Settings()
            self.label_SocialNet.setPixmap(QtGui.QPixmap("ВК.png"))
            self.label_SocialNet2.setText("VK")
            self.label_followers.setText("Количество подписчиков:")
            self.label_views.setText(" ")
        elif mode == 4:
            self.Start_Settings()
            self.label_SocialNet.setPixmap(QtGui.QPixmap("ДЗЕН.png"))
            self.label_SocialNet2.setText("Дзен")
            self.label_followers.setText("Дочитывания:")
            self.label_views.setText(" ")

        self.tabWidget.setCurrentWidget(self.widget)


    def Exit(self):
        self.tabWidget.setCurrentWidget(self.tab_Main)

    def hidePaws(self):
        self.label_paw.setVisible(False)
        self.label_paw2.setVisible(False)
        self.label_paw3.setVisible(False)
        self.label_paw4.setVisible(False)
        self.label_paw5.setVisible(False)
        self.label_paw6.setVisible(False)
        self.label_paw7.setVisible(False)

    def open_file(self):
        content = "photo"
        self.label_Info.setVisible(False)
        self.Button_Download.setVisible(False)
        self.Button_Download.setEnabled(False)
        self.label_Download.setVisible(False)
        self.label_resultImg.setVisible(True)
        self.label_followers.setVisible(True)
        self.label_views.setVisible(True)
        self.label_views2.setVisible(True)
        self.hidePaws()
        from tkinter import filedialog
        self.filename = filedialog.askopenfilename(filetypes=(
            ('jpg file', '*.jpg'),
            ('png file', '*.png'),
            ('jpeg file', '*.jpeg')
        ))
        if self.filename == None or self.filename == "":
            pass
        else:
            if self.label_SocialNet2.text() == "YouTube":
                result1, result2 = processing.process_photo(self.label_SocialNet2.text(),content,self.filename)
                stringResult = ""
                for res in result1:
                    stringResult += res + " "
                self.label_followers2.setText(stringResult)
                stringResult = ""
                for res in result2:
                    stringResult += res + " "
                self.label_views2.setText(stringResult)
            else:
                result = processing.process_photo(self.label_SocialNet2.text(),content,self.filename)
                stringResult = ""
                for res in result:
                    stringResult += res + " "
                self.label_followers2.setText(stringResult)
        self.label_followers2.setVisible(True)
        self.label_views2.setVisible(True)
        self.label_TextChoice.setText("Готово!")


    def open_dir(self):
        content = "folder"
        self.hidePaws()
        self.label_Info.setVisible(False)
        self.Button_Download.setVisible(True)
        self.Button_Download.setEnabled(True)
        self.label_Download.setVisible(True)
        self.label_resultImg.setVisible(False)
        self.label_followers.setVisible(False)
        self.label_followers2.setVisible(False)
        self.label_views.setVisible(False)
        self.label_views2.setVisible(False)
        from tkinter import filedialog
        self.dirname = filedialog.askdirectory()
        if self.dirname == None or self.dirname == "":
            pass
        else:
            processing.process_photo(self.label_SocialNet2.text(), content, self.dirname)
        self.label_TextChoice.setText("Готово!")




if __name__ == "__main__":

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    MainWindow = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
