# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_film_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdFilmDialog(object):
    def setupUi(self, AdFilmDialog):
        AdFilmDialog.setObjectName("AdFilmDialog")
        AdFilmDialog.resize(621, 301)
        self.formLayout = QtWidgets.QFormLayout(AdFilmDialog)
        self.formLayout.setObjectName("formLayout")
        self.groupBox = QtWidgets.QGroupBox(AdFilmDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setObjectName("name_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.description_label = QtWidgets.QLabel(self.groupBox)
        self.description_label.setObjectName("description_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.description_label)
        self.name_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.name_line_edit.setObjectName("name_line_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_line_edit)
        self.description_edit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.description_edit.setObjectName("description_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.description_edit)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.button_box = QtWidgets.QDialogButtonBox(AdFilmDialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.button_box)

        self.retranslateUi(AdFilmDialog)
        QtCore.QMetaObject.connectSlotsByName(AdFilmDialog)

    def retranslateUi(self, AdFilmDialog):
        _translate = QtCore.QCoreApplication.translate
        AdFilmDialog.setWindowTitle(_translate("AdFilmDialog", "Form"))
        self.groupBox.setTitle(_translate("AdFilmDialog", "Фильм"))
        self.name_label.setText(_translate("AdFilmDialog", "Название"))
        self.description_label.setText(_translate("AdFilmDialog", "Описание"))

