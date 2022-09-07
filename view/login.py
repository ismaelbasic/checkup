# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(384, 364)
        font = QFont()
        font.setFamily(u"Bebas Neue")
        font.setPointSize(28)
        Login.setFont(font)
        icon = QIcon()
        icon.addFile(u"config/img/icone.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Bebas Neue")
        font1.setPointSize(48)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Bebas Neue")
        font2.setPointSize(24)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(85, 85, 85);")

        self.verticalLayout.addWidget(self.label)

        self.campoUsuario = QLineEdit(Login)
        self.campoUsuario.setObjectName(u"campoUsuario")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(20)
        self.campoUsuario.setFont(font3)

        self.verticalLayout.addWidget(self.campoUsuario)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(85, 85, 85);")

        self.verticalLayout_2.addWidget(self.label_3)

        self.campoSenha = QLineEdit(Login)
        self.campoSenha.setObjectName(u"campoSenha")
        self.campoSenha.setFont(font3)

        self.verticalLayout_2.addWidget(self.campoSenha)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.btEntrar = QPushButton(Login)
        self.btEntrar.setObjectName(u"btEntrar")
        self.btEntrar.setFont(font2)
        self.btEntrar.setStyleSheet(u"background-color: rgb(79, 255, 79);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.btEntrar)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 44, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Checkup: Login", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.label.setText(QCoreApplication.translate("Login", u"Usu\u00e1rio:", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Senha:", None))
        self.btEntrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
    # retranslateUi

