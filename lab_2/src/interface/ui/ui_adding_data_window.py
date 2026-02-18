# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adding_data_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import main_rc
import main_icons_rc

class Ui_AddingDataWindow(object):
    def setupUi(self, AddingDataWindow):
        if not AddingDataWindow.objectName():
            AddingDataWindow.setObjectName(u"AddingDataWindow")
        AddingDataWindow.resize(386, 840)
        AddingDataWindow.setMinimumSize(QSize(386, 840))
        AddingDataWindow.setMaximumSize(QSize(610, 840))
        self.verticalLayout = QVBoxLayout(AddingDataWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AddingDataWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:None")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:None;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border:None;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_fio_user = QLabel(self.frame_4)
        self.label_fio_user.setObjectName(u"label_fio_user")

        self.verticalLayout_4.addWidget(self.label_fio_user)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_edit_fio_user = QLineEdit(self.frame_10)
        self.line_edit_fio_user.setObjectName(u"line_edit_fio_user")
        self.line_edit_fio_user.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_2.addWidget(self.line_edit_fio_user)

        self.button_user = QPushButton(self.frame_10)
        self.button_user.setObjectName(u"button_user")
        icon = QIcon()
        icon.addFile(u":/icons/icons/user2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_user.setIcon(icon)
        self.button_user.setIconSize(QSize(27, 27))

        self.horizontalLayout_2.addWidget(self.button_user)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border:None;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_address = QLabel(self.frame_5)
        self.label_address.setObjectName(u"label_address")

        self.verticalLayout_5.addWidget(self.label_address)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_edit_address = QLineEdit(self.frame_11)
        self.line_edit_address.setObjectName(u"line_edit_address")
        self.line_edit_address.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_3.addWidget(self.line_edit_address)

        self.button_address = QPushButton(self.frame_11)
        self.button_address.setObjectName(u"button_address")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/address.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_address.setIcon(icon1)
        self.button_address.setIconSize(QSize(27, 27))

        self.horizontalLayout_3.addWidget(self.button_address)


        self.verticalLayout_5.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border:None;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_of_birthday = QLabel(self.frame_6)
        self.label_of_birthday.setObjectName(u"label_of_birthday")

        self.verticalLayout_6.addWidget(self.label_of_birthday)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.frame_12)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.calendarWidget)

        self.button_date_of_birthday = QPushButton(self.frame_12)
        self.button_date_of_birthday.setObjectName(u"button_date_of_birthday")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/date.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_date_of_birthday.setIcon(icon2)
        self.button_date_of_birthday.setIconSize(QSize(27, 27))

        self.horizontalLayout_4.addWidget(self.button_date_of_birthday)


        self.verticalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_of_admission = QLabel(self.frame_7)
        self.label_of_admission.setObjectName(u"label_of_admission")
        self.label_of_admission.setStyleSheet(u"border:None;")

        self.verticalLayout_7.addWidget(self.label_of_admission)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget_2 = QCalendarWidget(self.frame_13)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        self.calendarWidget_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.calendarWidget_2)

        self.button_date_of_admission = QPushButton(self.frame_13)
        self.button_date_of_admission.setObjectName(u"button_date_of_admission")
        self.button_date_of_admission.setIcon(icon2)
        self.button_date_of_admission.setIconSize(QSize(27, 27))

        self.horizontalLayout_5.addWidget(self.button_date_of_admission)


        self.verticalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border:None;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_fio_doctor = QLabel(self.frame_8)
        self.label_fio_doctor.setObjectName(u"label_fio_doctor")

        self.verticalLayout_8.addWidget(self.label_fio_doctor)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.line_edit_doctor = QLineEdit(self.frame_14)
        self.line_edit_doctor.setObjectName(u"line_edit_doctor")
        self.line_edit_doctor.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_6.addWidget(self.line_edit_doctor)

        self.button_doctor = QPushButton(self.frame_14)
        self.button_doctor.setObjectName(u"button_doctor")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/doctor2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_doctor.setIcon(icon3)
        self.button_doctor.setIconSize(QSize(27, 27))

        self.horizontalLayout_6.addWidget(self.button_doctor)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_doctor_promt = QLabel(self.frame_9)
        self.label_doctor_promt.setObjectName(u"label_doctor_promt")
        self.label_doctor_promt.setStyleSheet(u"border:None;")

        self.verticalLayout_9.addWidget(self.label_doctor_promt)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 9)
        self.text_edit_doctor_promt = QTextEdit(self.frame_15)
        self.text_edit_doctor_promt.setObjectName(u"text_edit_doctor_promt")
        self.text_edit_doctor_promt.setMinimumSize(QSize(315, 0))
        self.text_edit_doctor_promt.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_7.addWidget(self.text_edit_doctor_promt)

        self.pushButton = QPushButton(self.frame_15)
        self.pushButton.setObjectName(u"pushButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/admission.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton.setAutoRepeatInterval(97)

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.frame_15)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border:None\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_cancel = QPushButton(self.frame_3)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setStyleSheet(u"background-color:rgb(193, 35, 90);\n"
"border : 1px solid  rgb(193, 35, 90);\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_clear = QPushButton(self.frame_3)
        self.button_clear.setObjectName(u"button_clear")
        self.button_clear.setStyleSheet(u"background-color:rgb(87, 99, 177);\n"
"border:1px solid rgb(87, 99, 177);;\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout.addWidget(self.button_clear)

        self.button_save = QPushButton(self.frame_3)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setStyleSheet(u"background-color:rgb(67, 153, 143);\n"
"border:1px solid rgb(67, 153, 143);\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout.addWidget(self.button_save)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AddingDataWindow)

        QMetaObject.connectSlotsByName(AddingDataWindow)
    # setupUi

    def retranslateUi(self, AddingDataWindow):
        AddingDataWindow.setWindowTitle(QCoreApplication.translate("AddingDataWindow", u"\u0424\u043e\u0440\u043c\u0430 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.label_fio_user.setText(QCoreApplication.translate("AddingDataWindow", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 (\u0410\u0440\u0445\u0438\u043f\u0435\u043d\u043a\u043e \u041c\u0438\u0445\u0430\u0438\u043b \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447)", None))
#if QT_CONFIG(accessibility)
        self.line_edit_fio_user.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_edit_fio_user.setPlaceholderText(QCoreApplication.translate("AddingDataWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0424\u0418\u041e", None))
        self.button_user.setText("")
        self.label_address.setText(QCoreApplication.translate("AddingDataWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438 (\u0433. \u041c\u0438\u043d\u0441\u043a, \u0443\u043b. \u0421\u0443\u0445\u0430\u0440\u0435\u0432\u0441\u043a\u0430\u044f 23, \u043a\u0432. 55)", None))
        self.line_edit_address.setPlaceholderText(QCoreApplication.translate("AddingDataWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438", None))
        self.button_address.setText("")
        self.label_of_birthday.setText(QCoreApplication.translate("AddingDataWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f (20.02.2006)", None))
        self.button_date_of_birthday.setText("")
#if QT_CONFIG(accessibility)
        self.label_of_admission.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_of_admission.setText(QCoreApplication.translate("AddingDataWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430 (20.02.2006)", None))
        self.button_date_of_admission.setText("")
        self.label_fio_doctor.setText(QCoreApplication.translate("AddingDataWindow", u"\u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430 (\u0410\u0440\u0445\u0438\u043f\u0435\u043d\u043a\u043e \u041c\u0438\u0445\u0430\u0438\u043b \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447)", None))
        self.line_edit_doctor.setPlaceholderText(QCoreApplication.translate("AddingDataWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430", None))
        self.button_doctor.setText("")
        self.label_doctor_promt.setText(QCoreApplication.translate("AddingDataWindow", u"\u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.text_edit_doctor_promt.setPlaceholderText(QCoreApplication.translate("AddingDataWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0432\u0440\u0430\u0447\u0430", None))
        self.pushButton.setText("")
        self.button_cancel.setText(QCoreApplication.translate("AddingDataWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.button_clear.setText(QCoreApplication.translate("AddingDataWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.button_save.setText(QCoreApplication.translate("AddingDataWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

