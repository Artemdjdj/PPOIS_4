# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import src.interface.qrc.main_rc
import src.interface.qrc.main_icons_rc

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        if not SearchWindow.objectName():
            SearchWindow.setObjectName(u"SearchWindow")
        SearchWindow.resize(1400, 722)
        SearchWindow.setMinimumSize(QSize(1400, 722))
        SearchWindow.setMaximumSize(QSize(1400, 942))
        SearchWindow.setStyleSheet(u"background-color:none;")
        self.verticalLayout = QVBoxLayout(SearchWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(SearchWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(386, 0))
        self.frame_2.setMaximumSize(QSize(386, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border:none;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border:None")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border:None;")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_16)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"border:None;")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_30)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_user = QLabel(self.frame_30)
        self.label_user.setObjectName(u"label_user")

        self.verticalLayout_5.addWidget(self.label_user)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.line_edit_fio_user = QLineEdit(self.frame_32)
        self.line_edit_fio_user.setObjectName(u"line_edit_fio_user")
        self.line_edit_fio_user.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_16.addWidget(self.line_edit_fio_user)

        self.button_user = QPushButton(self.frame_32)
        self.button_user.setObjectName(u"button_user")
        icon = QIcon()
        icon.addFile(u":/icons/icons/user2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_user.setIcon(icon)
        self.button_user.setIconSize(QSize(27, 27))

        self.horizontalLayout_16.addWidget(self.button_user)


        self.verticalLayout_5.addWidget(self.frame_32)


        self.verticalLayout_19.addWidget(self.frame_30)

        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border:None;")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_33)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_address = QLabel(self.frame_33)
        self.label_address.setObjectName(u"label_address")

        self.verticalLayout_6.addWidget(self.label_address)

        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.line_edit_address = QLineEdit(self.frame_34)
        self.line_edit_address.setObjectName(u"line_edit_address")
        self.line_edit_address.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_17.addWidget(self.line_edit_address)

        self.button_address = QPushButton(self.frame_34)
        self.button_address.setObjectName(u"button_address")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/address.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_address.setIcon(icon1)
        self.button_address.setIconSize(QSize(27, 27))

        self.horizontalLayout_17.addWidget(self.button_address)


        self.verticalLayout_6.addWidget(self.frame_34)


        self.verticalLayout_19.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.frame_16)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border:None;")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_35)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_date_of_birthday = QLabel(self.frame_35)
        self.label_date_of_birthday.setObjectName(u"label_date_of_birthday")

        self.verticalLayout_11.addWidget(self.label_date_of_birthday)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_19.setSpacing(4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.line_edit_date_of_birthday = QLineEdit(self.frame_36)
        self.line_edit_date_of_birthday.setObjectName(u"line_edit_date_of_birthday")
        self.line_edit_date_of_birthday.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_19.addWidget(self.line_edit_date_of_birthday)

        self.button_date_of_birthday = QPushButton(self.frame_36)
        self.button_date_of_birthday.setObjectName(u"button_date_of_birthday")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/date.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_date_of_birthday.setIcon(icon2)
        self.button_date_of_birthday.setIconSize(QSize(27, 27))

        self.horizontalLayout_19.addWidget(self.button_date_of_birthday)


        self.verticalLayout_11.addWidget(self.frame_36)


        self.verticalLayout_19.addWidget(self.frame_35)

        self.frame_37 = QFrame(self.frame_16)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_37)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_date_of_admission = QLabel(self.frame_37)
        self.label_date_of_admission.setObjectName(u"label_date_of_admission")
        self.label_date_of_admission.setStyleSheet(u"border:None;")

        self.verticalLayout_13.addWidget(self.label_date_of_admission)

        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.line_edit_date_of_admission = QLineEdit(self.frame_38)
        self.line_edit_date_of_admission.setObjectName(u"line_edit_date_of_admission")
        self.line_edit_date_of_admission.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_20.addWidget(self.line_edit_date_of_admission)

        self.button_of_admission = QPushButton(self.frame_38)
        self.button_of_admission.setObjectName(u"button_of_admission")
        self.button_of_admission.setIcon(icon2)
        self.button_of_admission.setIconSize(QSize(27, 27))

        self.horizontalLayout_20.addWidget(self.button_of_admission)


        self.verticalLayout_13.addWidget(self.frame_38)


        self.verticalLayout_19.addWidget(self.frame_37)

        self.frame_39 = QFrame(self.frame_16)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"border:None;")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_39)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_doctor_fio = QLabel(self.frame_39)
        self.label_doctor_fio.setObjectName(u"label_doctor_fio")

        self.verticalLayout_7.addWidget(self.label_doctor_fio)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, 0)
        self.line_edit_doctor = QLineEdit(self.frame_40)
        self.line_edit_doctor.setObjectName(u"line_edit_doctor")
        self.line_edit_doctor.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_21.addWidget(self.line_edit_doctor)

        self.button_doctor_icon = QPushButton(self.frame_40)
        self.button_doctor_icon.setObjectName(u"button_doctor_icon")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/doctor2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_doctor_icon.setIcon(icon3)
        self.button_doctor_icon.setIconSize(QSize(27, 27))

        self.horizontalLayout_21.addWidget(self.button_doctor_icon)


        self.verticalLayout_7.addWidget(self.frame_40)


        self.verticalLayout_19.addWidget(self.frame_39)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_27.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setStyleSheet(u"border:None\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_cancel = QPushButton(self.frame_5)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMaximumSize(QSize(160, 16777215))
        self.button_cancel.setStyleSheet(u"background-color:rgb(87, 99, 177);\n"
"border:1px solid rgb(87, 99, 177);;\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout_2.addWidget(self.button_cancel)

        self.button_search = QPushButton(self.frame_5)
        self.button_search.setObjectName(u"button_search")
        self.button_search.setMaximumSize(QSize(160, 16777215))
        self.button_search.setStyleSheet(u"background-color:rgb(67, 153, 143);\n"
"border:1px solid rgb(67, 153, 143);\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout_2.addWidget(self.button_search)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(669, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 40))
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setSpacing(80)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(70, 0, 60, 0)
        self.main_label = QLabel(self.frame_11)
        self.main_label.setObjectName(u"main_label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.main_label.setFont(font)
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.main_label)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_12)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.tab_widget_records = QTabWidget(self.frame_12)
        self.tab_widget_records.setObjectName(u"tab_widget_records")
        self.tab_list_of_records = QWidget()
        self.tab_list_of_records.setObjectName(u"tab_list_of_records")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_list_of_records)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.tab_list_of_records)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 20, 0, -1)
        self.table_of_recording = QTableWidget(self.frame_17)
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
        if (self.table_of_recording.rowCount() < 5):
            self.table_of_recording.setRowCount(5)
        self.table_of_recording.setObjectName(u"table_of_recording")
        self.table_of_recording.setMinimumSize(QSize(669, 0))
        self.table_of_recording.setStyleSheet(u"border:none;\n"
"background:none;")
        self.table_of_recording.horizontalHeader().setVisible(True)
        self.table_of_recording.horizontalHeader().setCascadingSectionResizes(True)
        self.table_of_recording.horizontalHeader().setDefaultSectionSize(105)
        self.table_of_recording.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.table_of_recording.horizontalHeader().setStretchLastSection(True)
        self.table_of_recording.verticalHeader().setVisible(True)
        self.table_of_recording.verticalHeader().setCascadingSectionResizes(True)
        self.table_of_recording.verticalHeader().setHighlightSections(True)
        self.table_of_recording.verticalHeader().setProperty(u"showSortIndicator", True)
        self.table_of_recording.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_5.addWidget(self.table_of_recording)


        self.horizontalLayout_7.addWidget(self.frame_17)

        self.tab_widget_records.addTab(self.tab_list_of_records, "")
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
        self.label_without_recording = QLabel(self.frame_31)
        self.label_without_recording.setObjectName(u"label_without_recording")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_without_recording.sizePolicy().hasHeightForWidth())
        self.label_without_recording.setSizePolicy(sizePolicy)
        self.label_without_recording.setPixmap(QPixmap(u":/images/images/start_in_search_window.png"))
        self.label_without_recording.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_without_recording)


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
        self.horizontalLayout_3 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, -1)
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
        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(250, 16777215))
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
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.label_all_records_2.setFont(font1)
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
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.comboBox_pagination.setFont(font2)
        self.comboBox_pagination.setStyleSheet(u"padding:10px;\n"
"text-align:center;\n"
"")

        self.horizontalLayout_12.addWidget(self.comboBox_pagination)


        self.horizontalLayout_6.addWidget(self.frame_19)

        self.result_pagination = QFrame(self.frame_14)
        self.result_pagination.setObjectName(u"result_pagination")
        self.result_pagination.setMaximumSize(QSize(800, 16777215))
        self.result_pagination.setStyleSheet(u"border:none;")
        self.result_pagination.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_pagination.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.result_pagination)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button_prev = QPushButton(self.result_pagination)
        self.button_prev.setObjectName(u"button_prev")
        self.button_prev.setMaximumSize(QSize(50, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.button_prev.setFont(font3)
        self.button_prev.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(64, 145, 136);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_prev)

        self.button_first = QPushButton(self.result_pagination)
        self.button_first.setObjectName(u"button_first")
        self.button_first.setMaximumSize(QSize(50, 50))
        self.button_first.setFont(font3)
        self.button_first.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(67, 153, 143);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_first)

        self.button_current = QPushButton(self.result_pagination)
        self.button_current.setObjectName(u"button_current")
        self.button_current.setMaximumSize(QSize(50, 50))
        self.button_current.setFont(font3)
        self.button_current.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(138, 197, 62);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_current)

        self.button_last = QPushButton(self.result_pagination)
        self.button_last.setObjectName(u"button_last")
        self.button_last.setMaximumSize(QSize(50, 50))
        self.button_last.setFont(font3)
        self.button_last.setStyleSheet(u"padding:15px;\n"
"background-color:rgb(67, 153, 143);\n"
"border-radius:25px;")

        self.horizontalLayout_9.addWidget(self.button_last)

        self.button_next = QPushButton(self.result_pagination)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setMaximumSize(QSize(50, 50))
        self.button_next.setFont(font3)
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
        self.horizontalLayout_22 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, -1, -1, -1)
        self.frame_41 = QFrame(self.frame_28)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_41)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.frame_29 = QFrame(self.frame_41)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 0, 0, 0)
        self.button_user_icon = QPushButton(self.frame_29)
        self.button_user_icon.setObjectName(u"button_user_icon")
        self.button_user_icon.setMinimumSize(QSize(26, 26))
        self.button_user_icon.setMaximumSize(QSize(60, 60))
        self.button_user_icon.setStyleSheet(u"background-color:none;\n"
"border:none;")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/doctor_without_background.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_user_icon.setIcon(icon4)
        self.button_user_icon.setIconSize(QSize(25, 25))

        self.horizontalLayout_23.addWidget(self.button_user_icon)

        self.label_medical_app = QLabel(self.frame_29)
        self.label_medical_app.setObjectName(u"label_medical_app")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.label_medical_app.setFont(font4)
        self.label_medical_app.setStyleSheet(u"border:none;\n"
"")

        self.horizontalLayout_23.addWidget(self.label_medical_app)


        self.verticalLayout_9.addWidget(self.frame_29)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(25, 0, 0, 0)
        self.label_last_medical_app = QLabel(self.frame_42)
        self.label_last_medical_app.setObjectName(u"label_last_medical_app")
        self.label_last_medical_app.setFont(font4)
        self.label_last_medical_app.setStyleSheet(u"border:none;\n"
"\n"
"")

        self.horizontalLayout_24.addWidget(self.label_last_medical_app)


        self.verticalLayout_9.addWidget(self.frame_42)


        self.horizontalLayout_22.addWidget(self.frame_41)

        self.frame_43 = QFrame(self.frame_28)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(310, 16777215))
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_43)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.button_address_clinic = QPushButton(self.frame_44)
        self.button_address_clinic.setObjectName(u"button_address_clinic")
        self.button_address_clinic.setMaximumSize(QSize(30, 16777215))
        self.button_address_clinic.setIcon(icon1)
        self.button_address_clinic.setIconSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.button_address_clinic)

        self.label_address_clinic = QLabel(self.frame_44)
        self.label_address_clinic.setObjectName(u"label_address_clinic")
        self.label_address_clinic.setFont(font4)

        self.horizontalLayout_25.addWidget(self.label_address_clinic)


        self.verticalLayout_12.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_43)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.button_email_clinic = QPushButton(self.frame_45)
        self.button_email_clinic.setObjectName(u"button_email_clinic")
        self.button_email_clinic.setMaximumSize(QSize(30, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_email_clinic.setIcon(icon5)
        self.button_email_clinic.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.button_email_clinic)

        self.label_email_clinic = QLabel(self.frame_45)
        self.label_email_clinic.setObjectName(u"label_email_clinic")
        self.label_email_clinic.setFont(font4)

        self.horizontalLayout_26.addWidget(self.label_email_clinic)


        self.verticalLayout_12.addWidget(self.frame_45)


        self.horizontalLayout_22.addWidget(self.frame_43)


        self.horizontalLayout_15.addWidget(self.frame_28)

        self.tab_widget_footer.addTab(self.tab_footer, "")

        self.horizontalLayout_3.addWidget(self.tab_widget_footer)


        self.verticalLayout_8.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(SearchWindow)

        self.tab_widget_records.setCurrentIndex(1)
        self.tab_widget_footer.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SearchWindow)
    # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Dialog", None))
        self.label_user.setText(QCoreApplication.translate("SearchWindow", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 (\u0410\u0440\u0445\u0438\u043f\u0435\u043d\u043a\u043e \u041c\u0438\u0445\u0430\u0438\u043b \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447)", None))
#if QT_CONFIG(accessibility)
        self.line_edit_fio_user.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_edit_fio_user.setPlaceholderText(QCoreApplication.translate("SearchWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0424\u0418\u041e", None))
        self.button_user.setText("")
        self.label_address.setText(QCoreApplication.translate("SearchWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438 (\u0433. \u041c\u0438\u043d\u0441\u043a, \u0443\u043b. \u041b\u043e\u0431\u0430\u043d\u043a\u0430 23, \u043a\u0432. 55)", None))
        self.line_edit_address.setPlaceholderText(QCoreApplication.translate("SearchWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438", None))
        self.button_address.setText("")
        self.label_date_of_birthday.setText(QCoreApplication.translate("SearchWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f (2006-02-12)", None))
        self.line_edit_date_of_birthday.setPlaceholderText(QCoreApplication.translate("SearchWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.button_date_of_birthday.setText("")
#if QT_CONFIG(accessibility)
        self.label_date_of_admission.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_date_of_admission.setText(QCoreApplication.translate("SearchWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430 (2006-02-12)", None))
        self.line_edit_date_of_admission.setText("")
        self.line_edit_date_of_admission.setPlaceholderText(QCoreApplication.translate("SearchWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u043f\u0440\u0438\u0435\u043c\u0430", None))
        self.button_of_admission.setText("")
        self.label_doctor_fio.setText(QCoreApplication.translate("SearchWindow", u"\u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430 (\u0410\u0440\u0445\u0438\u043f\u0435\u043d\u043a\u043e \u041c\u0438\u0445\u0430\u0438\u043b \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447)", None))
        self.line_edit_doctor.setPlaceholderText(QCoreApplication.translate("SearchWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430", None))
        self.button_doctor_icon.setText("")
        self.button_cancel.setText(QCoreApplication.translate("SearchWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.button_search.setText(QCoreApplication.translate("SearchWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.main_label.setText(QCoreApplication.translate("SearchWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043e\u0438\u0441\u043a\u0430", None))
        ___qtablewidgetitem = self.table_of_recording.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SearchWindow", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem1 = self.table_of_recording.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SearchWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438", None));
        ___qtablewidgetitem2 = self.table_of_recording.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SearchWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem3 = self.table_of_recording.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SearchWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430", None));
        ___qtablewidgetitem4 = self.table_of_recording.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SearchWindow", u"\u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430", None));
        ___qtablewidgetitem5 = self.table_of_recording.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SearchWindow", u"\u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None));
        self.tab_widget_records.setTabText(self.tab_widget_records.indexOf(self.tab_list_of_records), QCoreApplication.translate("SearchWindow", u"\u0417\u0430\u043f\u0438\u0441\u0438", None))
        self.label_without_recording.setText("")
        self.tab_widget_records.setTabText(self.tab_widget_records.indexOf(self.tab_no_records), QCoreApplication.translate("SearchWindow", u"\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0435\u0442", None))
        self.label_all_records_2.setText(QCoreApplication.translate("SearchWindow", u"\u0417\u0430\u043f\u0438\u0441\u0435\u0439 \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435", None))
        self.comboBox_pagination.setItemText(0, QCoreApplication.translate("SearchWindow", u"5", None))
        self.comboBox_pagination.setItemText(1, QCoreApplication.translate("SearchWindow", u"10", None))
        self.comboBox_pagination.setItemText(2, QCoreApplication.translate("SearchWindow", u"50", None))
        self.comboBox_pagination.setItemText(3, QCoreApplication.translate("SearchWindow", u"100", None))
        self.comboBox_pagination.setItemText(4, QCoreApplication.translate("SearchWindow", u"150", None))

        self.button_prev.setText(QCoreApplication.translate("SearchWindow", u"<", None))
        self.button_first.setText(QCoreApplication.translate("SearchWindow", u"1", None))
        self.button_current.setText(QCoreApplication.translate("SearchWindow", u"3", None))
        self.button_last.setText(QCoreApplication.translate("SearchWindow", u"n", None))
        self.button_next.setText(QCoreApplication.translate("SearchWindow", u">", None))
        self.tab_widget_footer.setTabText(self.tab_widget_footer.indexOf(self.tab_pagination), QCoreApplication.translate("SearchWindow", u"\u041f\u0430\u0433\u0438\u043d\u0430\u0446\u0438\u044f", None))
        self.button_user_icon.setText("")
        self.label_medical_app.setText(QCoreApplication.translate("SearchWindow", u"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0439 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.label_last_medical_app.setText(QCoreApplication.translate("SearchWindow", u"\u00a9 2026 \u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0443\u0447\u0435\u0442\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0439 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432 \n"
"\u0412\u0441\u0435 \u043f\u0440\u0430\u0432\u0430 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u044b.", None))
        self.button_address_clinic.setText("")
        self.label_address_clinic.setText(QCoreApplication.translate("SearchWindow", u"\u0433. \u041c\u0438\u043d\u0441\u043a, \u0443\u043b. \u041b\u043e\u0431\u0430\u043d\u043a\u0430 24", None))
        self.button_email_clinic.setText("")
        self.label_email_clinic.setText(QCoreApplication.translate("SearchWindow", u"minsk_clinic@gmail.com", None))
        self.tab_widget_footer.setTabText(self.tab_widget_footer.indexOf(self.tab_footer), QCoreApplication.translate("SearchWindow", u"\u0424\u0443\u0442\u0435\u0440", None))
    # retranslateUi

        self.tab_widget_records.tabBar().hide()
        self.tab_widget_footer.tabBar().hide()