# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_session_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddSessionDialog(object):
    def setupUi(self, AddSessionDialog):
        AddSessionDialog.setObjectName("AddSessionDialog")
        AddSessionDialog.resize(654, 285)
        self.formLayout = QtWidgets.QFormLayout(AddSessionDialog)
        self.formLayout.setObjectName("formLayout")
        self.groupBox = QtWidgets.QGroupBox(AddSessionDialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.cinema_label = QtWidgets.QLabel(self.groupBox)
        self.cinema_label.setObjectName("cinema_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cinema_label)
        self.cinema_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.cinema_combo_box.setObjectName("cinema_combo_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cinema_combo_box)
        self.hall_label = QtWidgets.QLabel(self.groupBox)
        self.hall_label.setObjectName("hall_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.hall_label)
        self.hall_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.hall_combo_box.setObjectName("hall_combo_box")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hall_combo_box)
        self.film_label = QtWidgets.QLabel(self.groupBox)
        self.film_label.setObjectName("film_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.film_label)
        self.film_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.film_combo_box.setObjectName("film_combo_box")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.film_combo_box)
        self.date_label = QtWidgets.QLabel(self.groupBox)
        self.date_label.setObjectName("date_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.date_label)
        self.data_edit = QtWidgets.QDateEdit(self.groupBox)
        self.data_edit.setObjectName("data_edit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.data_edit)
        self.time_label = QtWidgets.QLabel(self.groupBox)
        self.time_label.setObjectName("time_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.time_label)
        self.time_edit = QtWidgets.QTimeEdit(self.groupBox)
        self.time_edit.setObjectName("time_edit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.time_edit)
        self.cinema_tool_btn = QtWidgets.QToolButton(self.groupBox)
        self.cinema_tool_btn.setObjectName("cinema_tool_btn")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cinema_tool_btn)
        self.hall_tool_btn = QtWidgets.QToolButton(self.groupBox)
        self.hall_tool_btn.setObjectName("hall_tool_btn")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.hall_tool_btn)
        self.film_tool_btn = QtWidgets.QToolButton(self.groupBox)
        self.film_tool_btn.setObjectName("film_tool_btn")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.film_tool_btn)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupBox)
        self.button_box = QtWidgets.QDialogButtonBox(AddSessionDialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.button_box)

        self.retranslateUi(AddSessionDialog)
        QtCore.QMetaObject.connectSlotsByName(AddSessionDialog)

    def retranslateUi(self, AddSessionDialog):
        _translate = QtCore.QCoreApplication.translate
        AddSessionDialog.setWindowTitle(_translate("AddSessionDialog", "Form"))
        self.groupBox.setTitle(_translate("AddSessionDialog", "Сеанс"))
        self.cinema_label.setText(_translate("AddSessionDialog", "Кинотеатр"))
        self.hall_label.setText(_translate("AddSessionDialog", "Зал"))
        self.film_label.setText(_translate("AddSessionDialog", "Фильм"))
        self.date_label.setText(_translate("AddSessionDialog", "Дата"))
        self.time_label.setText(_translate("AddSessionDialog", "Время"))
        self.cinema_tool_btn.setText(_translate("AddSessionDialog", "..."))
        self.hall_tool_btn.setText(_translate("AddSessionDialog", "..."))
        self.film_tool_btn.setText(_translate("AddSessionDialog", "..."))

