# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\details_session_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DetalisSessionDialog(object):
    def setupUi(self, DetalisSessionDialog):
        DetalisSessionDialog.setObjectName("DetalisSessionDialog")
        DetalisSessionDialog.resize(870, 490)
        self.gridLayout = QtWidgets.QGridLayout(DetalisSessionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.img_cont = QtWidgets.QLabel(DetalisSessionDialog)
        self.img_cont.setText("")
        self.img_cont.setAlignment(QtCore.Qt.AlignCenter)
        self.img_cont.setObjectName("img_cont")
        self.gridLayout.addWidget(self.img_cont, 0, 0, 1, 1)

        self.retranslateUi(DetalisSessionDialog)
        QtCore.QMetaObject.connectSlotsByName(DetalisSessionDialog)

    def retranslateUi(self, DetalisSessionDialog):
        _translate = QtCore.QCoreApplication.translate
        DetalisSessionDialog.setWindowTitle(_translate("DetalisSessionDialog", "Form"))

