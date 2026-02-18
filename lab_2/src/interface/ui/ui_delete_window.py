# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import main_icons_rc

class Ui_DeleteWindow(object):
    def setupUi(self, DeleteWindow):
        if not DeleteWindow.objectName():
            DeleteWindow.setObjectName(u"DeleteWindow")
        DeleteWindow.resize(386, 500)
        DeleteWindow.setMinimumSize(QSize(386, 500))
        DeleteWindow.setMaximumSize(QSize(386, 500))
        self.verticalLayout = QVBoxLayout(DeleteWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DeleteWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame)
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
        self.verticalLayout_20 = QVBoxLayout(self.frame_30)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_fio_user = QLabel(self.frame_30)
        self.label_fio_user.setObjectName(u"label_fio_user")

        self.verticalLayout_20.addWidget(self.label_fio_user)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.line_edit_user = QLineEdit(self.frame_32)
        self.line_edit_user.setObjectName(u"line_edit_user")
        self.line_edit_user.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_16.addWidget(self.line_edit_user)

        self.button_user = QPushButton(self.frame_32)
        self.button_user.setObjectName(u"button_user")
        icon = QIcon()
        icon.addFile(u":/icons/icons/user2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_user.setIcon(icon)
        self.button_user.setIconSize(QSize(27, 27))

        self.horizontalLayout_16.addWidget(self.button_user)


        self.verticalLayout_20.addWidget(self.frame_32)


        self.verticalLayout_19.addWidget(self.frame_30)

        self.frame_33 = QFrame(self.frame_16)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border:None;")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_33)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label__address = QLabel(self.frame_33)
        self.label__address.setObjectName(u"label__address")

        self.verticalLayout_21.addWidget(self.label__address)

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


        self.verticalLayout_21.addWidget(self.frame_34)


        self.verticalLayout_19.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.frame_16)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border:None;")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_35)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label__date_of_birthday = QLabel(self.frame_35)
        self.label__date_of_birthday.setObjectName(u"label__date_of_birthday")

        self.verticalLayout_23.addWidget(self.label__date_of_birthday)

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

        self.button_of_birthday = QPushButton(self.frame_36)
        self.button_of_birthday.setObjectName(u"button_of_birthday")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/date.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_of_birthday.setIcon(icon2)
        self.button_of_birthday.setIconSize(QSize(27, 27))

        self.horizontalLayout_19.addWidget(self.button_of_birthday)


        self.verticalLayout_23.addWidget(self.frame_36)


        self.verticalLayout_19.addWidget(self.frame_35)

        self.frame_37 = QFrame(self.frame_16)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_37)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_date_of_admission = QLabel(self.frame_37)
        self.label_date_of_admission.setObjectName(u"label_date_of_admission")
        self.label_date_of_admission.setStyleSheet(u"border:None;")

        self.verticalLayout_24.addWidget(self.label_date_of_admission)

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

        self.button_of_date_of_addmission = QPushButton(self.frame_38)
        self.button_of_date_of_addmission.setObjectName(u"button_of_date_of_addmission")
        self.button_of_date_of_addmission.setIcon(icon2)
        self.button_of_date_of_addmission.setIconSize(QSize(27, 27))

        self.horizontalLayout_20.addWidget(self.button_of_date_of_addmission)


        self.verticalLayout_24.addWidget(self.frame_38)


        self.verticalLayout_19.addWidget(self.frame_37)

        self.frame_39 = QFrame(self.frame_16)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"border:None;")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_39)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_of_fio_doctor = QLabel(self.frame_39)
        self.label_of_fio_doctor.setObjectName(u"label_of_fio_doctor")

        self.verticalLayout_25.addWidget(self.label_of_fio_doctor)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_21.setSpacing(4)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, 0)
        self.line_edit_fio_doctor = QLineEdit(self.frame_40)
        self.line_edit_fio_doctor.setObjectName(u"line_edit_fio_doctor")
        self.line_edit_fio_doctor.setStyleSheet(u"border: 1px solid rgb(197, 197, 197);\n"
"border-radius:6px;\n"
"padding:4px;")

        self.horizontalLayout_21.addWidget(self.line_edit_fio_doctor)

        self.button_of_doctor = QPushButton(self.frame_40)
        self.button_of_doctor.setObjectName(u"button_of_doctor")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/doctor2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_of_doctor.setIcon(icon3)
        self.button_of_doctor.setIconSize(QSize(27, 27))

        self.horizontalLayout_21.addWidget(self.button_of_doctor)


        self.verticalLayout_25.addWidget(self.frame_40)


        self.verticalLayout_19.addWidget(self.frame_39)


        self.verticalLayout_18.addWidget(self.frame_16)


        self.verticalLayout_27.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border:None\n"
"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_cancel = QPushButton(self.frame_3)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setStyleSheet(u"background-color:rgb(87, 99, 177);\n"
"border:1px solid rgb(87, 99, 177);;\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_find = QPushButton(self.frame_3)
        self.button_find.setObjectName(u"button_find")
        self.button_find.setStyleSheet(u"background-color:rgb(67, 153, 143);\n"
"border:1px solid rgb(67, 153, 143);\n"
"border-radius:6px;\n"
"padding:2px 4px;")

        self.horizontalLayout.addWidget(self.button_find)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DeleteWindow)

        QMetaObject.connectSlotsByName(DeleteWindow)
    # setupUi

    def retranslateUi(self, DeleteWindow):
        DeleteWindow.setWindowTitle(QCoreApplication.translate("DeleteWindow", u"delete_window", None))
        self.label_fio_user.setText(QCoreApplication.translate("DeleteWindow", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430 (\u0410\u0440\u0445\u0438\u043f\u0435\u043d\u043a\u043e \u041c\u0438\u0445\u0430\u0438\u043b \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447)", None))
#if QT_CONFIG(accessibility)
        self.line_edit_user.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.line_edit_user.setPlaceholderText(QCoreApplication.translate("DeleteWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448\u0435 \u0424\u0418\u041e", None))
        self.button_user.setText("")
        self.label__address.setText(QCoreApplication.translate("DeleteWindow", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438 (\u0433. \u041c\u0438\u043d\u0441\u043a, \u0443\u043b. \u041b\u043e\u0431\u0430\u043d\u043a\u0430 23, \u043a\u0432. 55)", None))
        self.line_edit_address.setPlaceholderText(QCoreApplication.translate("DeleteWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u043f\u0438\u0441\u043a\u0438", None))
        self.button_address.setText("")
        self.label__date_of_birthday.setText(QCoreApplication.translate("DeleteWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f (20.02.2006)", None))
        self.line_edit_date_of_birthday.setPlaceholderText(QCoreApplication.translate("DeleteWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.button_of_birthday.setText("")
#if QT_CONFIG(accessibility)
        self.label_date_of_admission.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_date_of_admission.setText(QCoreApplication.translate("DeleteWindow", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430 (20.02.2006)", None))
        self.line_edit_date_of_admission.setPlaceholderText(QCoreApplication.translate("DeleteWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u0442\u0443 \u043f\u0440\u0438\u0435\u043c\u0430", None))
        self.button_of_date_of_addmission.setText("")
        self.label_of_fio_doctor.setText(QCoreApplication.translate("DeleteWindow", u"\u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430 (\u0410\u0440\u0445\u0438\u043f\u0435\u043d\u043a\u043e \u041c\u0438\u0445\u0430\u0438\u043b \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447)", None))
        self.line_edit_fio_doctor.setPlaceholderText(QCoreApplication.translate("DeleteWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0424\u0418\u041e \u0432\u0440\u0430\u0447\u0430", None))
        self.button_of_doctor.setText("")
        self.button_cancel.setText(QCoreApplication.translate("DeleteWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.button_find.setText(QCoreApplication.translate("DeleteWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
    # retranslateUi

