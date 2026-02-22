# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmation_to_db_window.ui'
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

class Ui_DialogSaveToDb(object):
    def setupUi(self, DialogSaveToDb):
        if not DialogSaveToDb.objectName():
            DialogSaveToDb.setObjectName(u"DialogSaveToDb")
        DialogSaveToDb.resize(430, 300)
        DialogSaveToDb.setMinimumSize(QSize(430, 300))
        DialogSaveToDb.setMaximumSize(QSize(430, 300))
        self.verticalLayout = QVBoxLayout(DialogSaveToDb)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogSaveToDb)
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
        self.label_to_save = QLabel(self.frame_2)
        self.label_to_save.setObjectName(u"label_to_save")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_to_save.sizePolicy().hasHeightForWidth())
        self.label_to_save.setSizePolicy(sizePolicy)
        self.label_to_save.setPixmap(QPixmap(u":/images/images/db.png"))
        self.label_to_save.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_to_save)

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
        font.setPointSize(9)
        font.setBold(False)
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
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_cancel = QPushButton(self.frame_3)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setStyleSheet(u"border:none;\n"
"background-color:rgb(87, 99, 177);\n"
"padding:6px;\n"
"border-radius:6px;")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_ok = QPushButton(self.frame_3)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setStyleSheet(u"border:none;\n"
"background-color:rgb(67, 153, 143);\n"
"padding:6px;\n"
"border-radius:6px;")

        self.horizontalLayout.addWidget(self.button_ok)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DialogSaveToDb)

        QMetaObject.connectSlotsByName(DialogSaveToDb)
    # setupUi

    def retranslateUi(self, DialogSaveToDb):
        DialogSaveToDb.setWindowTitle(QCoreApplication.translate("DialogSaveToDb", u"Dialog", None))
        self.label_to_save.setText("")
        self.label_save_message.setText(QCoreApplication.translate("DialogSaveToDb", u" \u0412\u044b \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445?", None))
        self.button_cancel.setText(QCoreApplication.translate("DialogSaveToDb", u"\u041d\u0435\u0442", None))
        self.button_ok.setText(QCoreApplication.translate("DialogSaveToDb", u"\u0414\u0430", None))
    # retranslateUi

