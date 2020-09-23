# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 330)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.dNILabel = QLabel(self.centralwidget)
        self.dNILabel.setObjectName(u"dNILabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dNILabel)

        self.le_dni = QLineEdit(self.centralwidget)
        self.le_dni.setObjectName(u"le_dni")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_dni)

        self.nombreLabel = QLabel(self.centralwidget)
        self.nombreLabel.setObjectName(u"nombreLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.nombreLabel)

        self.le_nombre = QLineEdit(self.centralwidget)
        self.le_nombre.setObjectName(u"le_nombre")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_nombre)

        self.apellidoLabel = QLabel(self.centralwidget)
        self.apellidoLabel.setObjectName(u"apellidoLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.apellidoLabel)

        self.le_apellido = QLineEdit(self.centralwidget)
        self.le_apellido.setObjectName(u"le_apellido")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_apellido)

        self.edadLabel = QLabel(self.centralwidget)
        self.edadLabel.setObjectName(u"edadLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.edadLabel)

        self.le_edad = QLineEdit(self.centralwidget)
        self.le_edad.setObjectName(u"le_edad")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.le_edad)

        self.sexoLabel = QLabel(self.centralwidget)
        self.sexoLabel.setObjectName(u"sexoLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sexoLabel)

        self.cb_sexo = QComboBox(self.centralwidget)
        self.cb_sexo.addItem("")
        self.cb_sexo.addItem("")
        self.cb_sexo.addItem("")
        self.cb_sexo.setObjectName(u"cb_sexo")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cb_sexo)

        self.provinciaLabel = QLabel(self.centralwidget)
        self.provinciaLabel.setObjectName(u"provinciaLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.provinciaLabel)

        self.cb_provincia = QComboBox(self.centralwidget)
        self.cb_provincia.setObjectName(u"cb_provincia")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.cb_provincia)

        self.fechaRegistroLabel = QLabel(self.centralwidget)
        self.fechaRegistroLabel.setObjectName(u"fechaRegistroLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.fechaRegistroLabel)

        self.le_fecha_registro = QDateEdit(self.centralwidget)
        self.le_fecha_registro.setObjectName(u"le_fecha_registro")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.le_fecha_registro)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_clear = QPushButton(self.centralwidget)
        self.pb_clear.setObjectName(u"pb_clear")

        self.horizontalLayout.addWidget(self.pb_clear)

        self.pb_register = QPushButton(self.centralwidget)
        self.pb_register.setObjectName(u"pb_register")

        self.horizontalLayout.addWidget(self.pb_register)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pb_clear.clicked.connect(MainWindow.clear_all)
        self.pb_register.clicked.connect(MainWindow.register)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Casos de COVID 19", None))
        self.dNILabel.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.le_dni.setInputMask(QCoreApplication.translate("MainWindow", u"99.999.999", None))
        self.nombreLabel.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.apellidoLabel.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.edadLabel.setText(QCoreApplication.translate("MainWindow", u"Edad", None))
        self.le_edad.setInputMask(QCoreApplication.translate("MainWindow", u"009", None))
        self.sexoLabel.setText(QCoreApplication.translate("MainWindow", u"Sexo", None))
        self.cb_sexo.setItemText(0, QCoreApplication.translate("MainWindow", u"Hombre", None))
        self.cb_sexo.setItemText(1, QCoreApplication.translate("MainWindow", u"Mujer", None))
        self.cb_sexo.setItemText(2, QCoreApplication.translate("MainWindow", u"Otros", None))

        self.provinciaLabel.setText(QCoreApplication.translate("MainWindow", u"Provincia", None))
        self.fechaRegistroLabel.setText(QCoreApplication.translate("MainWindow", u"Fecha Registro", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Persona", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pb_register.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
    # retranslateUi

