# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_cinema_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddCinemaDialog(object):
    def setupUi(self, AddCinemaDialog):
        AddCinemaDialog.setObjectName("AddCinemaDialog")
        AddCinemaDialog.resize(400, 126)
        self.formLayout = QtWidgets.QFormLayout(AddCinemaDialog)
        self.formLayout.setObjectName("formLayout")
        self.groupBox = QtWidgets.QGroupBox(AddCinemaDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setObjectName("name_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.address_label = QtWidgets.QLabel(self.groupBox)
        self.address_label.setObjectName("address_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.address_label)
        self.name_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.name_line_edit.setObjectName("name_line_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_line_edit)
        self.address_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.address_line_edit.setObjectName("address_line_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.address_line_edit)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.button_box = QtWidgets.QDialogButtonBox(AddCinemaDialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.button_box)

        self.retranslateUi(AddCinemaDialog)
        QtCore.QMetaObject.connectSlotsByName(AddCinemaDialog)

    def retranslateUi(self, AddCinemaDialog):
        _translate = QtCore.QCoreApplication.translate
        AddCinemaDialog.setWindowTitle(_translate("AddCinemaDialog", "Form"))
        self.groupBox.setTitle(_translate("AddCinemaDialog", "Кинотеатр"))
        self.name_label.setText(_translate("AddCinemaDialog", "Название"))
        self.address_label.setText(_translate("AddCinemaDialog", "Адресс"))

