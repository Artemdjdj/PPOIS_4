# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_window.ui'
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
                               QLabel, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)
import src.interface.qrc.main_rc


class Ui_Dialog_save(object):
    def setupUi(self, Dialog_save):
        if not Dialog_save.objectName():
            Dialog_save.setObjectName(u"Dialog_save")
        Dialog_save.resize(430, 300)
        Dialog_save.setMinimumSize(QSize(430, 300))
        Dialog_save.setMaximumSize(QSize(430, 300))
        self.horizontalLayout_3 = QHBoxLayout(Dialog_save)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(Dialog_save)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:none;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border:none;\n"
                                   "")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_save = QLabel(self.frame_2)
        self.label_save.setObjectName(u"label_save")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_save.sizePolicy().hasHeightForWidth())
        self.label_save.setSizePolicy(sizePolicy)
        self.label_save.setPixmap(QPixmap(u":/images/images/save.png"))
        self.label_save.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_save)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_save_message = QLabel(self.frame_4)
        self.label_save_message.setObjectName(u"label_save_message")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.label_save_message.setFont(font)
        self.label_save_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_save_message)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"border:none;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"border:none;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_cancel = QPushButton(self.frame_5)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setStyleSheet(u"border:none;\n"
                                         "background-color:rgb(87, 99, 177);\n"
                                         "padding:6px;\n"
                                         "border-radius:6px;")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_ok = QPushButton(self.frame_5)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setStyleSheet(u"border:none;\n"
                                     "background-color:rgb(67, 153, 143);\n"
                                     "padding:6px;\n"
                                     "border-radius:6px;")

        self.horizontalLayout.addWidget(self.button_ok)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout_3.addWidget(self.frame)

        self.retranslateUi(Dialog_save)

        QMetaObject.connectSlotsByName(Dialog_save)

    # setupUi

    def retranslateUi(self, Dialog_save):
        Dialog_save.setWindowTitle(QCoreApplication.translate("Dialog_save", u"Dialog", None))
        self.label_save.setText("")
        self.label_save_message.setText(QCoreApplication.translate("Dialog_save",
                                                                   u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0444\u0430\u0439\u043b?",
                                                                   None))
        self.button_cancel.setText(QCoreApplication.translate("Dialog_save", u"\u041d\u0435\u0442", None))
        self.button_ok.setText(QCoreApplication.translate("Dialog_save", u"\u0414\u0430", None))
    # retranslateUi
