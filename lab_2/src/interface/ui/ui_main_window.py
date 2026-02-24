# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import src.interface.qrc.main_rc
import src.interface.qrc.main_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 758)
        MainWindow.setMinimumSize(QSize(1200, 758))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"border:none;\n"
"border-radius:0;\n"
"background-color:none;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 758))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"border:none;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(845, 758))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tab_widget_main = QTabWidget(self.frame)
        self.tab_widget_main.setObjectName(u"tab_widget_main")
        self.tab_start_page = QWidget()
        self.tab_start_page.setObjectName(u"tab_start_page")
        self.tab_start_page.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.tab_start_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.tab_start_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border:None;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_start = QLabel(self.frame_5)
        self.label_start.setObjectName(u"label_start")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(False)
        self.label_start.setFont(font1)
        self.label_start.setStyleSheet(u"border:None;")
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_start)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_start_with_logo = QPushButton(self.frame_3)
        self.button_start_with_logo.setObjectName(u"button_start_with_logo")
        self.button_start_with_logo.setStyleSheet(u"border:None;\n"
"border-radius:200px;\n"
"background-color:rgb(87, 99, 177);")
        icon = QIcon()
        icon.addFile(u":/images/images/doctor_without_background.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_start_with_logo.setIcon(icon)
        self.button_start_with_logo.setIconSize(QSize(300, 300))

        self.verticalLayout_4.addWidget(self.button_start_with_logo)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border:None;\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_exit = QPushButton(self.frame_4)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(150, 0))
        self.button_exit.setMaximumSize(QSize(250, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.button_exit.setFont(font2)
        self.button_exit.setStyleSheet(u"padding:20px;\n"
"background-color:rgb(87, 99, 177);\n"
"border-radius:25px;")

        self.horizontalLayout.addWidget(self.button_exit)

        self.button_start = QPushButton(self.frame_4)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setMinimumSize(QSize(150, 0))
        self.button_start.setMaximumSize(QSize(250, 16777215))
        self.button_start.setFont(font2)
        self.button_start.setStyleSheet(u"padding:20px;\n"
"background-color:rgb(67, 153, 143);\n"
"border-radius:25px;")

        self.horizontalLayout.addWidget(self.button_start)

        self.horizontalSpacer_2 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.tab_widget_main.addTab(self.tab_start_page, "")
        self.tab_main_page = QWidget()
        self.tab_main_page.setObjectName(u"tab_main_page")
        self.tab_main_page.setMinimumSize(QSize(824, 722))
        self.tab_main_page.setMaximumSize(QSize(16777215, 16777215))
        self.tab_main_page.setStyleSheet(u"border:none;")
        self.verticalLayout_6 = QVBoxLayout(self.tab_main_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.tab_main_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(825, 722))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"border:none;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 722))
        self.frame_7.setMaximumSize(QSize(300, 16777215))
        self.frame_7.setStyleSheet(u"border:none;")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border:none;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tab_widget_work_state = QTabWidget(self.frame_9)
        self.tab_widget_work_state.setObjectName(u"tab_widget_work_state")
        self.tab_widget_work_state.setStyleSheet(u"border:none;")
        self.tab_work_with_data = QWidget()
        self.tab_work_with_data.setObjectName(u"tab_work_with_data")
        self.tab_work_with_data.setStyleSheet(u"border:none;")
        self.verticalLayout_16 = QVBoxLayout(self.tab_work_with_data)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.tab_work_with_data)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:none;")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 0, 10, 0)
        self.frame_16 = QFrame(self.frame_10)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 110))
        self.frame_16.setStyleSheet(u"border:none;")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 0, 2, 1)
        self.button_icon = QPushButton(self.frame_16)
        self.button_icon.setObjectName(u"button_icon")
        self.button_icon.setIcon(icon)
        self.button_icon.setIconSize(QSize(100, 100))

        self.verticalLayout_17.addWidget(self.button_icon)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_20 = QFrame(self.frame_10)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border:none;")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_20)
        self.verticalLayout_23.setSpacing(15)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer)

        self.button_back = QPushButton(self.frame_20)
        self.button_back.setObjectName(u"button_back")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.button_back.setFont(font3)
        self.button_back.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button_back.setStyleSheet(u"QPushButton{\n"
"padding:3px;\n"
"background-color:rgb(26, 24, 26);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(39, 36, 39);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/back2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QSize(43, 43))

        self.verticalLayout_23.addWidget(self.button_back)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_23.addItem(self.verticalSpacer_5)

        self.label_work_with_data = QFrame(self.frame_20)
        self.label_work_with_data.setObjectName(u"label_work_with_data")
        self.label_work_with_data.setMaximumSize(QSize(16777215, 30))
        self.label_work_with_data.setStyleSheet(u"border:none;")
        self.label_work_with_data.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_work_with_data.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.label_work_with_data)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_work_with_data_2 = QLabel(self.label_work_with_data)
        self.label_work_with_data_2.setObjectName(u"label_work_with_data_2")
        self.label_work_with_data_2.setMaximumSize(QSize(16777215, 30))
        self.label_work_with_data_2.setFont(font3)
        self.label_work_with_data_2.setStyleSheet(u"border:none;")
        self.label_work_with_data_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_work_with_data_2)


        self.verticalLayout_23.addWidget(self.label_work_with_data)

        self.button_add_new_record = QPushButton(self.frame_20)
        self.button_add_new_record.setObjectName(u"button_add_new_record")
        self.button_add_new_record.setFont(font3)
        self.button_add_new_record.setStyleSheet(u"QPushButton {\n"
"    padding:13px;\n"
"	background-color:rgb(67, 153, 143);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 139, 130);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"")

        self.verticalLayout_23.addWidget(self.button_add_new_record)

        self.button_show_tree = QPushButton(self.frame_20)
        self.button_show_tree.setObjectName(u"button_show_tree")
        self.button_show_tree.setFont(font3)
        self.button_show_tree.setStyleSheet(u"QPushButton{\n"
"padding:13px;\n"
"background-color:rgb(26, 24, 26);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(39, 36, 39);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")

        self.verticalLayout_23.addWidget(self.button_show_tree)


        self.verticalLayout_14.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_10)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 70))
        self.frame_21.setStyleSheet(u"border:none;")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 0, 2, 0)
        self.button_delete = QPushButton(self.frame_21)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setFont(font3)
        self.button_delete.setStyleSheet(u"QPushButton{\n"
"	padding:13px;\n"
"    background-color:rgb(141, 69, 98);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	padding:13px;\n"
"    background-color:rgb(122, 60, 86);\n"
"    border-radius:10px;\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.button_delete)


        self.verticalLayout_14.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.frame_10)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 200))
        self.frame_23.setStyleSheet(u"border:none;")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.button_save_to_db = QPushButton(self.frame_23)
        self.button_save_to_db.setObjectName(u"button_save_to_db")
        self.button_save_to_db.setFont(font3)
        self.button_save_to_db.setStyleSheet(u"QPushButton{\n"
"	padding:13px;\n"
"    background-color:rgb(64, 43, 170);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	padding:13px;\n"
"    background-color:rgb(87, 99, 177);\n"
"    border-radius:10px;\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.button_save_to_db)

        self.button_exit_app = QPushButton(self.frame_23)
        self.button_exit_app.setObjectName(u"button_exit_app")
        self.button_exit_app.setFont(font3)
        self.button_exit_app.setStyleSheet(u"QPushButton{\n"
"	padding:13px;\n"
"    background-color:rgb(87, 99, 177);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	padding:13px;\n"
"    background-color:rgb(64, 43, 170);\n"
"    border-radius:10px;\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.button_exit_app)


        self.verticalLayout_14.addWidget(self.frame_23)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.tab_widget_work_state.addTab(self.tab_work_with_data, "")
        self.tab_load_data = QWidget()
        self.tab_load_data.setObjectName(u"tab_load_data")
        self.tab_load_data.setStyleSheet(u"border:none;")
        self.verticalLayout_18 = QVBoxLayout(self.tab_load_data)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.tab_load_data)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_24)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 400))
        self.frame_25.setMaximumSize(QSize(16777215, 500))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_25)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 0, 9, 0)
        self.button_icon_of_app = QPushButton(self.frame_25)
        self.button_icon_of_app.setObjectName(u"button_icon_of_app")
        self.button_icon_of_app.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.button_icon_of_app.setIcon(icon)
        self.button_icon_of_app.setIconSize(QSize(100, 100))

        self.verticalLayout_20.addWidget(self.button_icon_of_app)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.frame_25)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_2)

        self.button_load_from_file = QPushButton(self.frame_25)
        self.button_load_from_file.setObjectName(u"button_load_from_file")
        self.button_load_from_file.setMinimumSize(QSize(0, 30))
        self.button_load_from_file.setFont(font2)
        self.button_load_from_file.setStyleSheet(u"\n"
"QPushButton {\n"
"    padding:6px;\n"
"	background-color:rgb(67, 153, 143);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(61, 139, 130);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.button_load_from_file)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_4)

        self.button_load_from_db = QPushButton(self.frame_25)
        self.button_load_from_db.setObjectName(u"button_load_from_db")
        self.button_load_from_db.setMinimumSize(QSize(0, 30))
        self.button_load_from_db.setFont(font2)
        self.button_load_from_db.setStyleSheet(u"\n"
"QPushButton {\n"
"    padding:6px;\n"
"	background-color:rgb(87, 99, 177);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(75, 85, 152);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")

        self.verticalLayout_20.addWidget(self.button_load_from_db)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)


        self.verticalLayout_19.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_19.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_24)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_19.addWidget(self.frame_27)


        self.verticalLayout_18.addWidget(self.frame_24)

        self.tab_widget_work_state.addTab(self.tab_load_data, "")

        self.verticalLayout_13.addWidget(self.tab_widget_work_state)


        self.verticalLayout_7.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(824, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_12)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 90))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tab_widget_header = QTabWidget(self.frame_11)
        self.tab_widget_header.setObjectName(u"tab_widget_header")
        self.tab_widget_header.setStyleSheet(u"border:none;\n"
"background-color:none;")
        self.tab_header_search = QWidget()
        self.tab_header_search.setObjectName(u"tab_header_search")
        self.horizontalLayout_19 = QHBoxLayout(self.tab_header_search)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.tab_header_search)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setMaximumSize(QSize(16777215, 50))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.label_all_records = QLabel(self.frame_18)
        self.label_all_records.setObjectName(u"label_all_records")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_all_records.setFont(font5)
        self.label_all_records.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_all_records)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_count_records = QLabel(self.frame_18)
        self.label_count_records.setObjectName(u"label_count_records")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(False)
        self.label_count_records.setFont(font6)
        self.label_count_records.setStyleSheet(u"color:rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_count_records)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.button_search = QPushButton(self.frame_18)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setMinimumSize(QSize(100, 0))
        self.button_search.setMaximumSize(QSize(150, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setBold(True)
        font7.setItalic(False)
        self.button_search.setFont(font7)
        self.button_search.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button_search.setStyleSheet(u"QPushButton {\n"
"    background-color: #1a181a;\n"
"    border-radius: 14px;\n"
"    border: none;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(39, 36, 39);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/magnifying_glass.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_search.setIcon(icon2)
        self.button_search.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.button_search)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_10.addWidget(self.frame_18)


        self.horizontalLayout_19.addWidget(self.frame_17)

        self.tab_widget_header.addTab(self.tab_header_search, "")
        self.tab_header_other = QWidget()
        self.tab_header_other.setObjectName(u"tab_header_other")
        self.tab_widget_header.addTab(self.tab_header_other, "")

        self.horizontalLayout_4.addWidget(self.tab_widget_header)


        self.verticalLayout_10.addWidget(self.frame_11)

        self.tab_widget_records = QTabWidget(self.frame_12)
        self.tab_widget_records.setObjectName(u"tab_widget_records")
        self.tab_list_of_records = QWidget()
        self.tab_list_of_records.setObjectName(u"tab_list_of_records")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_list_of_records)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.tab_list_of_records)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 20, 0, -1)
        self.table_of_recording = QTableWidget(self.frame_15)
        if (self.table_of_recording.columnCount() < 6):
            self.table_of_recording.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_of_recording.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_of_recording.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_of_recording.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_of_recording.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_of_recording.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_of_recording.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.table_of_recording.rowCount() < 100):
            self.table_of_recording.setRowCount(100)
        self.table_of_recording.setObjectName(u"table_of_recording")
        self.table_of_recording.setMinimumSize(QSize(669, 0))
        self.table_of_recording.setStyleSheet(u"border:none;\n"
"background:none;")
        self.table_of_recording.setRowCount(100)
        self.table_of_recording.horizontalHeader().setVisible(True)
        self.table_of_recording.horizontalHeader().setCascadingSectionResizes(True)
        self.table_of_recording.horizontalHeader().setMinimumSectionSize(50)
        self.table_of_recording.horizontalHeader().setDefaultSectionSize(105)
        self.table_of_recording.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_of_recording.horizontalHeader().setStretchLastSection(True)
        self.table_of_recording.verticalHeader().setVisible(True)
        self.table_of_recording.verticalHeader().setCascadingSectionResizes(True)
        self.table_of_recording.verticalHeader().setHighlightSections(True)
        self.table_of_recording.verticalHeader().setProperty(u"showSortIndicator", True)
        self.table_of_recording.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.table_of_recording)


        self.horizontalLayout_7.addWidget(self.frame_15)

        self.tab_widget_records.addTab(self.tab_list_of_records, "")
        self.tab_tree_of_records = QWidget()
        self.tab_tree_of_records.setObjectName(u"tab_tree_of_records")
        self.verticalLayout_11 = QVBoxLayout(self.tab_tree_of_records)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.tab_tree_of_records)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 5, 100, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_8)

        self.label = QLabel(self.frame_22)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color:rgbrgb(240, 240, 240);\n"
"padding:10px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.button_back_to_table = QPushButton(self.frame_22)
        self.button_back_to_table.setObjectName(u"button_back_to_table")
        self.button_back_to_table.setMaximumSize(QSize(200, 16777215))
        self.button_back_to_table.setFont(font7)
        self.button_back_to_table.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.button_back_to_table.setStyleSheet(u"QPushButton {\n"
"    background-color: #1a181a;\n"
"    padding: 8px;\n"
"    border-radius: 18px;\n"
"    border: none;\n"
"    color: white;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(39, 36, 39);  /* \u0434\u0440\u0443\u0433\u043e\u0439 \u0446\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/table.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_back_to_table.setIcon(icon3)
        self.button_back_to_table.setIconSize(QSize(20, 20))

        self.horizontalLayout_20.addWidget(self.button_back_to_table)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addWidget(self.frame_22)

        self.treeWidget = QTreeWidget(self.tab_tree_of_records)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_11.addWidget(self.treeWidget)

        self.tab_widget_records.addTab(self.tab_tree_of_records, "")
        self.tab_no_records = QWidget()
        self.tab_no_records.setObjectName(u"tab_no_records")
        self.verticalLayout_22 = QVBoxLayout(self.tab_no_records)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.tab_no_records)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_31)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setPixmap(QPixmap(u":/images/images/no_records_horizontal.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_6)


        self.verticalLayout_22.addWidget(self.frame_31)

        self.tab_widget_records.addTab(self.tab_no_records, "")

        self.verticalLayout_10.addWidget(self.tab_widget_records)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 150))
        self.frame_13.setMaximumSize(QSize(16777215, 200))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tab_widget_footer = QTabWidget(self.frame_13)
        self.tab_widget_footer.setObjectName(u"tab_widget_footer")
        self.tab_pagination = QWidget()
        self.tab_pagination.setObjectName(u"tab_pagination")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_pagination)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.tab_pagination)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 10, 0)
        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(350, 16777215))
        self.frame_19.setStyleSheet(u"border:none;")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_all_records_2 = QLabel(self.frame_19)
        self.label_all_records_2.setObjectName(u"label_all_records_2")
        self.label_all_records_2.setMaximumSize(QSize(150, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        font8.setBold(False)
        self.label_all_records_2.setFont(font8)
        self.label_all_records_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_all_records_2)

        self.comboBox_pagination = QComboBox(self.frame_19)
        self.comboBox_pagination.addItem("")
        self.comboBox_pagination.addItem("")
        self.comboBox_pagination.addItem("")
        self.comboBox_pagination.addItem("")
        self.comboBox_pagination.addItem("")
        self.comboBox_pagination.setObjectName(u"comboBox_pagination")
        self.comboBox_pagination.setMinimumSize(QSize(80, 50))
        self.comboBox_pagination.setMaximumSize(QSize(80, 50))
        palette = QPalette()
        brush = QBrush(QColor(59, 134, 125, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        brush1 = QBrush(QColor(61, 139, 130, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush1)
        brush2 = QBrush(QColor(63, 145, 135, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush2)
        brush3 = QBrush(QColor(65, 148, 139, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush3)
        brush4 = QBrush(QColor(56, 128, 120, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush4)
        brush5 = QBrush(QColor(58, 132, 124, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush5)
        brush6 = QBrush(QColor(60, 136, 127, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush6)
        brush7 = QBrush(QColor(56, 126, 118, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush7)
        brush8 = QBrush(QColor(61, 138, 129, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush8)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush8)
        self.comboBox_pagination.setPalette(palette)
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(16)
        font9.setBold(True)
        self.comboBox_pagination.setFont(font9)
        self.comboBox_pagination.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBox_pagination.setStyleSheet(u"padding:10px;\n"
"text-align:center;\n"
"border: 1px solid rgb(64, 145, 136);\n"
"")

        self.horizontalLayout_12.addWidget(self.comboBox_pagination)


        self.horizontalLayout_6.addWidget(self.frame_19)

        self.result_pagination = QFrame(self.frame_14)
        self.result_pagination.setObjectName(u"result_pagination")
        self.result_pagination.setMaximumSize(QSize(700, 16777215))
        self.result_pagination.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.result_pagination.setStyleSheet(u"border:none;")
        self.result_pagination.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_pagination.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.result_pagination)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button_prev = QPushButton(self.result_pagination)
        self.button_prev.setObjectName(u"button_prev")
        self.button_prev.setMaximumSize(QSize(50, 50))
        self.button_prev.setFont(font4)
        self.button_prev.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(64, 145, 136);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_prev)

        self.button_first = QPushButton(self.result_pagination)
        self.button_first.setObjectName(u"button_first")
        self.button_first.setMaximumSize(QSize(50, 50))
        self.button_first.setFont(font4)
        self.button_first.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(67, 153, 143);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_first)

        self.button_current = QPushButton(self.result_pagination)
        self.button_current.setObjectName(u"button_current")
        self.button_current.setMaximumSize(QSize(50, 50))
        self.button_current.setFont(font4)
        self.button_current.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(138, 197, 62);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_current)

        self.button_last = QPushButton(self.result_pagination)
        self.button_last.setObjectName(u"button_last")
        self.button_last.setMaximumSize(QSize(50, 50))
        self.button_last.setFont(font4)
        self.button_last.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(67, 153, 143);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_last)

        self.button_next = QPushButton(self.result_pagination)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setMaximumSize(QSize(50, 50))
        self.button_next.setFont(font4)
        self.button_next.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(63, 144, 135);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_next)


        self.horizontalLayout_6.addWidget(self.result_pagination)


        self.horizontalLayout_14.addWidget(self.frame_14)

        self.tab_widget_footer.addTab(self.tab_pagination, "")
        self.tab_footer = QWidget()
        self.tab_footer.setObjectName(u"tab_footer")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_footer)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.tab_footer)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border:none;\n"
"")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, -1, -1)
        self.frame_32 = QFrame(self.frame_28)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_32)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.frame_29 = QFrame(self.frame_32)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 0, 0, 0)
        self.button_user_icon = QPushButton(self.frame_29)
        self.button_user_icon.setObjectName(u"button_user_icon")
        self.button_user_icon.setMinimumSize(QSize(26, 26))
        self.button_user_icon.setMaximumSize(QSize(60, 60))
        self.button_user_icon.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.button_user_icon.setIcon(icon)
        self.button_user_icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_16.addWidget(self.button_user_icon)

        self.label_medical_app = QLabel(self.frame_29)
        self.label_medical_app.setObjectName(u"label_medical_app")
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(10)
        self.label_medical_app.setFont(font10)
        self.label_medical_app.setStyleSheet(u"border:none;\n"
"")

        self.horizontalLayout_16.addWidget(self.label_medical_app)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_32)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(25, 0, 0, 0)
        self.label_last_medical_app = QLabel(self.frame_30)
        self.label_last_medical_app.setObjectName(u"label_last_medical_app")
        self.label_last_medical_app.setFont(font10)
        self.label_last_medical_app.setStyleSheet(u"border:none;\n"
"\n"
"")

        self.horizontalLayout_17.addWidget(self.label_last_medical_app)


        self.verticalLayout_9.addWidget(self.frame_30)


        self.horizontalLayout_21.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_28)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(310, 16777215))
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_33)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.button_address_clinic = QPushButton(self.frame_34)
        self.button_address_clinic.setObjectName(u"button_address_clinic")
        self.button_address_clinic.setMaximumSize(QSize(30, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/address.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_address_clinic.setIcon(icon4)
        self.button_address_clinic.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.button_address_clinic)

        self.label_address_clinic = QLabel(self.frame_34)
        self.label_address_clinic.setObjectName(u"label_address_clinic")
        self.label_address_clinic.setFont(font10)

        self.horizontalLayout_22.addWidget(self.label_address_clinic)


        self.verticalLayout_12.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.button_email_clinic = QPushButton(self.frame_35)
        self.button_email_clinic.setObjectName(u"button_email_clinic")
        self.button_email_clinic.setMaximumSize(QSize(30, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_email_clinic.setIcon(icon5)
        self.button_email_clinic.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.button_email_clinic)

        self.label_email_clinic = QLabel(self.frame_35)
        self.label_email_clinic.setObjectName(u"label_email_clinic")
        self.label_email_clinic.setFont(font10)

        self.horizontalLayout_23.addWidget(self.label_email_clinic)


        self.verticalLayout_12.addWidget(self.frame_35)


        self.horizontalLayout_21.addWidget(self.frame_33)


        self.horizontalLayout_15.addWidget(self.frame_28)

        self.tab_widget_footer.addTab(self.tab_footer, "")

        self.horizontalLayout_11.addWidget(self.tab_widget_footer)


        self.verticalLayout_8.addWidget(self.frame_13)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.tab_widget_main.addTab(self.tab_main_page, "")

        self.verticalLayout_2.addWidget(self.tab_widget_main)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tab_widget_main.setCurrentIndex(1)
        self.tab_widget_work_state.setCurrentIndex(1)
        self.tab_widget_header.setCurrentIndex(0)
        self.tab_widget_records.setCurrentIndex(2)
        self.tab_widget_footer.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_start.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438\u0439 \u0443\u0447\u0435\u0442 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.button_start_with_logo.setText("")
        self.button_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c", None))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_start_page), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
        self.button_icon.setText("")
        self.button_back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_work_with_data_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.button_add_new_record.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.button_show_tree.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.button_save_to_db.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \n"
" \u0432 \u0431\u0434", None))
        self.button_exit_app.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.tab_widget_work_state.setTabText(self.tab_widget_work_state.indexOf(self.tab_work_with_data), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.button_icon_of_app.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437", None))
        self.button_load_from_file.setText(QCoreApplication.translate("MainWindow", u"\u0444\u0430\u0439\u043b\u0430", None))
        self.button_load_from_db.setText(QCoreApplication.translate("MainWindow", u"\u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.tab_widget_work_state.setTabText(self.tab_widget_work_state.indexOf(self.tab_load_data), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_all_records.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435", None))
        self.label_count_records.setText("")
        self.button_search.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.tab_widget_header.setTabText(self.tab_widget_header.indexOf(self.tab_header_search), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.tab_widget_header.setTabText(self.tab_widget_header.indexOf(self.tab_header_other), QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0441\u0442\u043e\u0439 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        ___qtablewidgetitem = self.table_of_recording.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.table_of_recording.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438", None));
        ___qtablewidgetitem2 = self.table_of_recording.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.table_of_recording.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430", None));
        ___qtablewidgetitem4 = self.table_of_recording.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430", None));
        ___qtablewidgetitem5 = self.table_of_recording.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None));
        self.tab_widget_records.setTabText(self.tab_widget_records.indexOf(self.tab_list_of_records), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0435\u0432\u043e\u0432\u0438\u0434\u043d\u043e\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0435\u0439", None))
        self.button_back_to_table.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.tab_widget_records.setTabText(self.tab_widget_records.indexOf(self.tab_tree_of_records), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432 \u0432\u0438\u0434\u0435 \u0434\u0435\u0440\u0435\u0432\u0430", None))
        self.label_6.setText("")
        self.tab_widget_records.setTabText(self.tab_widget_records.indexOf(self.tab_no_records), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0435\u0442", None))
        self.label_all_records_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435", None))
        self.comboBox_pagination.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_pagination.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_pagination.setItemText(2, QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBox_pagination.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))
        self.comboBox_pagination.setItemText(4, QCoreApplication.translate("MainWindow", u"150", None))

        self.button_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.button_first.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_current.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_last.setText(QCoreApplication.translate("MainWindow", u"n", None))
        self.button_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.tab_widget_footer.setTabText(self.tab_widget_footer.indexOf(self.tab_pagination), QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0433\u0438\u043d\u0430\u0446\u0438\u044f", None))
        self.button_user_icon.setText("")
        self.label_medical_app.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0439 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.label_last_medical_app.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2026 \u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0439 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432 \n"
"\u0412\u0441\u0435 \u043f\u0440\u0430\u0432\u0430 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u044b.", None))
        self.button_address_clinic.setText("")
        self.label_address_clinic.setText(QCoreApplication.translate("MainWindow", u"\u0433. \u041c\u0438\u043d\u0441\u043a, \u0443\u043b. \u041b\u043e\u0431\u0430\u043d\u043a\u0430 24", None))
        self.button_email_clinic.setText("")
        self.label_email_clinic.setText(QCoreApplication.translate("MainWindow", u"minsk_clinic@gmail.com", None))
        self.tab_widget_footer.setTabText(self.tab_widget_footer.indexOf(self.tab_footer), QCoreApplication.translate("MainWindow", u"\u0424\u0443\u0442\u0435\u0440", None))
        self.tab_widget_main.setTabText(self.tab_widget_main.indexOf(self.tab_main_page), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430", None))
    # retranslateUi

        self.tab_widget_main.tabBar().hide()
        self.tab_widget_header.tabBar().hide()
        self.tab_widget_records.tabBar().hide()
        self.tab_widget_header.tabBar().hide()
        self.tab_widget_footer.tabBar().hide()
        self.tab_widget_work_state.tabBar().hide()