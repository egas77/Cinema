# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.remove_session_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_session_btn.setObjectName("remove_session_btn")
        self.gridLayout.addWidget(self.remove_session_btn, 2, 1, 1, 1)
        self.open_session_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_session_btn.setObjectName("open_session_btn")
        self.gridLayout.addWidget(self.open_session_btn, 2, 0, 1, 1)
        self.session_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.session_label.setFont(font)
        self.session_label.setObjectName("session_label")
        self.gridLayout.addWidget(self.session_label, 0, 0, 1, 1)
        self.add_sesion_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_sesion_btn.setObjectName("add_sesion_btn")
        self.gridLayout.addWidget(self.add_sesion_btn, 3, 0, 1, 2)
        self.sessions_table = QtWidgets.QTableWidget(self.centralwidget)
        self.sessions_table.setObjectName("sessions_table")
        self.sessions_table.setColumnCount(0)
        self.sessions_table.setRowCount(0)
        self.gridLayout.addWidget(self.sessions_table, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        self.menuExport = QtWidgets.QMenu(self.menuFIle)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_docx = QtWidgets.QAction(MainWindow)
        self.action_docx.setObjectName("action_docx")
        self.action_xlsx = QtWidgets.QAction(MainWindow)
        self.action_xlsx.setObjectName("action_xlsx")
        self.action_pptx = QtWidgets.QAction(MainWindow)
        self.action_pptx.setObjectName("action_pptx")
        self.menuExport.addAction(self.action_docx)
        self.menuExport.addAction(self.action_xlsx)
        self.menuExport.addAction(self.action_pptx)
        self.menuFIle.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.remove_session_btn.setText(_translate("MainWindow", "Удалить"))
        self.open_session_btn.setText(_translate("MainWindow", "Открыть"))
        self.session_label.setText(_translate("MainWindow", "Сеансы"))
        self.add_sesion_btn.setText(_translate("MainWindow", "Добавить"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.action_docx.setText(_translate("MainWindow", "docx"))
        self.action_xlsx.setText(_translate("MainWindow", "xlsx"))
        self.action_pptx.setText(_translate("MainWindow", "pptx"))

