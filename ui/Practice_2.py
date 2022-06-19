# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Practice_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 450)
        Form.setMinimumSize(QSize(700, 450))
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_left_up = QPushButton(Form)
        self.pushButton_left_up.setObjectName(u"pushButton_left_up")

        self.horizontalLayout.addWidget(self.pushButton_left_up)

        self.pushButton_right_up = QPushButton(Form)
        self.pushButton_right_up.setObjectName(u"pushButton_right_up")

        self.horizontalLayout.addWidget(self.pushButton_right_up)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_center = QPushButton(Form)
        self.pushButton_center.setObjectName(u"pushButton_center")

        self.verticalLayout.addWidget(self.pushButton_center)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_left_down = QPushButton(Form)
        self.pushButton_left_down.setObjectName(u"pushButton_left_down")

        self.horizontalLayout_2.addWidget(self.pushButton_left_down)

        self.pushButton_right_down = QPushButton(Form)
        self.pushButton_right_down.setObjectName(u"pushButton_right_down")

        self.horizontalLayout_2.addWidget(self.pushButton_right_down)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.pushButton_get_wndw_data = QPushButton(Form)
        self.pushButton_get_wndw_data.setObjectName(u"pushButton_get_wndw_data")

        self.verticalLayout_2.addWidget(self.pushButton_get_wndw_data)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")

        self.horizontalLayout_3.addWidget(self.dial)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_4.addWidget(self.comboBox)

        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_4.addWidget(self.lcdNumber)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.horizontalSlider)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_4.addWidget(self.plainTextEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_left_up.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButton_right_up.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButton_center.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.pushButton_left_down.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButton_right_down.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.pushButton_get_wndw_data.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"HEX", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"DEC", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"OCT", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"BIN", None))

    # retranslateUi

