# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_hall_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddHallDialog(object):
    def setupUi(self, AddHallDialog):
        AddHallDialog.setObjectName("AddHallDialog")
        AddHallDialog.resize(499, 178)
        self.formLayout = QtWidgets.QFormLayout(AddHallDialog)
        self.formLayout.setObjectName("formLayout")
        self.groupBox = QtWidgets.QGroupBox(AddHallDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.cinema_label = QtWidgets.QLabel(self.groupBox)
        self.cinema_label.setObjectName("cinema_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cinema_label)
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setObjectName("name_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.count_row_label = QtWidgets.QLabel(self.groupBox)
        self.count_row_label.setObjectName("count_row_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.count_row_label)
        self.count_col_label = QtWidgets.QLabel(self.groupBox)
        self.count_col_label.setObjectName("count_col_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.count_col_label)
        self.cinema_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.cinema_combo_box.setObjectName("cinema_combo_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cinema_combo_box)
        self.name_line_edit = QtWidgets.QLineEdit(self.groupBox)
        self.name_line_edit.setObjectName("name_line_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_line_edit)
        self.count_row_edit = QtWidgets.QSpinBox(self.groupBox)
        self.count_row_edit.setObjectName("count_row_edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.count_row_edit)
        self.count_col_elit = QtWidgets.QSpinBox(self.groupBox)
        self.count_col_elit.setObjectName("count_col_elit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.count_col_elit)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.button_box = QtWidgets.QDialogButtonBox(AddHallDialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.button_box)

        self.retranslateUi(AddHallDialog)
        QtCore.QMetaObject.connectSlotsByName(AddHallDialog)

    def retranslateUi(self, AddHallDialog):
        _translate = QtCore.QCoreApplication.translate
        AddHallDialog.setWindowTitle(_translate("AddHallDialog", "Form"))
        self.groupBox.setTitle(_translate("AddHallDialog", "Зал"))
        self.cinema_label.setText(_translate("AddHallDialog", "Кинотеатр"))
        self.name_label.setText(_translate("AddHallDialog", "Название"))
        self.count_row_label.setText(_translate("AddHallDialog", "Количество рядов"))
        self.count_col_label.setText(_translate("AddHallDialog", "Количество колонок"))

