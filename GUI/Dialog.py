# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ponumber = QtWidgets.QGroupBox(self.centralwidget)
        self.ponumber.setGeometry(QtCore.QRect(180, 80, 131, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.ponumber.setFont(font)
        self.ponumber.setObjectName("ponumber")
        self.lbl_row_ponumber = QtWidgets.QLabel(self.ponumber)
        self.lbl_row_ponumber.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lbl_row_ponumber.setObjectName("lbl_row_ponumber")
        self.lbl_col_ponumber = QtWidgets.QLabel(self.ponumber)
        self.lbl_col_ponumber.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.lbl_col_ponumber.setObjectName("lbl_col_ponumber")
        self.row_spin_ponumber = QtWidgets.QSpinBox(self.ponumber)
        self.row_spin_ponumber.setGeometry(QtCore.QRect(50, 20, 61, 22))
        self.row_spin_ponumber.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.row_spin_ponumber.setObjectName("row_spin_ponumber")
        self.col_spin_ponumber = QtWidgets.QSpinBox(self.ponumber)
        self.col_spin_ponumber.setGeometry(QtCore.QRect(50, 50, 61, 22))
        self.col_spin_ponumber.setObjectName("col_spin_ponumber")
        self.quantity = QtWidgets.QGroupBox(self.centralwidget)
        self.quantity.setGeometry(QtCore.QRect(180, 180, 131, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.quantity.setFont(font)
        self.quantity.setObjectName("quantity")
        self.lbl_row_quantity = QtWidgets.QLabel(self.quantity)
        self.lbl_row_quantity.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lbl_row_quantity.setObjectName("lbl_row_quantity")
        self.lbl_col_quantity = QtWidgets.QLabel(self.quantity)
        self.lbl_col_quantity.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.lbl_col_quantity.setObjectName("lbl_col_quantity")
        self.row_spin_quantity = QtWidgets.QSpinBox(self.quantity)
        self.row_spin_quantity.setGeometry(QtCore.QRect(50, 20, 61, 22))
        self.row_spin_quantity.setObjectName("row_spin_quantity")
        self.col_spin_quantity = QtWidgets.QSpinBox(self.quantity)
        self.col_spin_quantity.setGeometry(QtCore.QRect(50, 50, 61, 22))
        self.col_spin_quantity.setObjectName("col_spin_quantity")
        self.barcode = QtWidgets.QGroupBox(self.centralwidget)
        self.barcode.setGeometry(QtCore.QRect(10, 180, 131, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barcode.setFont(font)
        self.barcode.setObjectName("barcode")
        self.lbl_row_barcode = QtWidgets.QLabel(self.barcode)
        self.lbl_row_barcode.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lbl_row_barcode.setObjectName("lbl_row_barcode")
        self.lbl_col_barcode = QtWidgets.QLabel(self.barcode)
        self.lbl_col_barcode.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.lbl_col_barcode.setObjectName("lbl_col_barcode")
        self.row_spin_barcode = QtWidgets.QSpinBox(self.barcode)
        self.row_spin_barcode.setGeometry(QtCore.QRect(50, 20, 61, 22))
        self.row_spin_barcode.setObjectName("row_spin_barcode")
        self.col_spin_barcode = QtWidgets.QSpinBox(self.barcode)
        self.col_spin_barcode.setGeometry(QtCore.QRect(50, 50, 61, 22))
        self.col_spin_barcode.setObjectName("col_spin_barcode")
        self.mdlkarton = QtWidgets.QGroupBox(self.centralwidget)
        self.mdlkarton.setGeometry(QtCore.QRect(10, 280, 131, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.mdlkarton.setFont(font)
        self.mdlkarton.setObjectName("mdlkarton")
        self.lbl_row_mdlkarton = QtWidgets.QLabel(self.mdlkarton)
        self.lbl_row_mdlkarton.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lbl_row_mdlkarton.setObjectName("lbl_row_mdlkarton")
        self.lbl_col_mdlkarton = QtWidgets.QLabel(self.mdlkarton)
        self.lbl_col_mdlkarton.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.lbl_col_mdlkarton.setObjectName("lbl_col_mdlkarton")
        self.row_spin_mdlkarton = QtWidgets.QSpinBox(self.mdlkarton)
        self.row_spin_mdlkarton.setGeometry(QtCore.QRect(50, 20, 61, 22))
        self.row_spin_mdlkarton.setObjectName("row_spin_mdlkarton")
        self.col_spin_mdlkarton = QtWidgets.QSpinBox(self.mdlkarton)
        self.col_spin_mdlkarton.setGeometry(QtCore.QRect(50, 50, 61, 22))
        self.col_spin_mdlkarton.setObjectName("col_spin_mdlkarton")
        self.outBtn = QtWidgets.QPushButton(self.centralwidget)
        self.outBtn.setGeometry(QtCore.QRect(230, 40, 81, 23))
        self.outBtn.setObjectName("outBtn")
        self.convertBtn = QtWidgets.QPushButton(self.centralwidget)
        self.convertBtn.setGeometry(QtCore.QRect(190, 300, 111, 41))
        self.convertBtn.setMaximumSize(QtCore.QSize(111, 50))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.convertBtn.setFont(font)
        self.convertBtn.setObjectName("convertBtn")
        self.openEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.openEdit.setGeometry(QtCore.QRect(10, 10, 211, 23))
        self.openEdit.setObjectName("openEdit")
        self.codestore = QtWidgets.QGroupBox(self.centralwidget)
        self.codestore.setGeometry(QtCore.QRect(10, 80, 131, 81))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.codestore.setFont(font)
        self.codestore.setObjectName("codestore")
        self.lbl_row_codestore = QtWidgets.QLabel(self.codestore)
        self.lbl_row_codestore.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.lbl_row_codestore.setObjectName("lbl_row_codestore")
        self.lbl_col_codestore = QtWidgets.QLabel(self.codestore)
        self.lbl_col_codestore.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.lbl_col_codestore.setObjectName("lbl_col_codestore")
        self.row_spin_codestore = QtWidgets.QSpinBox(self.codestore)
        self.row_spin_codestore.setGeometry(QtCore.QRect(50, 20, 61, 22))
        self.row_spin_codestore.setObjectName("row_spin_codestore")
        self.col_spin_codestore = QtWidgets.QSpinBox(self.codestore)
        self.col_spin_codestore.setGeometry(QtCore.QRect(50, 50, 61, 22))
        self.col_spin_codestore.setObjectName("col_spin_codestore")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(230, 10, 81, 23))
        self.openBtn.setObjectName("openBtn")
        self.outputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputEdit.setGeometry(QtCore.QRect(10, 40, 211, 23))
        self.outputEdit.setObjectName("outputEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "e-PO CSV Converter"))
        self.ponumber.setTitle(_translate("MainWindow", "PO Number"))
        self.lbl_row_ponumber.setText(_translate("MainWindow", "Row"))
        self.lbl_col_ponumber.setText(_translate("MainWindow", "Column"))
        self.quantity.setTitle(_translate("MainWindow", "Quantity"))
        self.lbl_row_quantity.setText(_translate("MainWindow", "Row"))
        self.lbl_col_quantity.setText(_translate("MainWindow", "Column"))
        self.barcode.setTitle(_translate("MainWindow", "Barcode"))
        self.lbl_row_barcode.setText(_translate("MainWindow", "Row"))
        self.lbl_col_barcode.setText(_translate("MainWindow", "Column"))
        self.mdlkarton.setTitle(_translate("MainWindow", "Modal Karton"))
        self.lbl_row_mdlkarton.setText(_translate("MainWindow", "Row"))
        self.lbl_col_mdlkarton.setText(_translate("MainWindow", "Column"))
        self.outBtn.setText(_translate("MainWindow", "Output"))
        self.convertBtn.setText(_translate("MainWindow", "CONVERT"))
        self.codestore.setTitle(_translate("MainWindow", "Code Store"))
        self.lbl_row_codestore.setText(_translate("MainWindow", "Row"))
        self.lbl_col_codestore.setText(_translate("MainWindow", "Column"))
        self.openBtn.setText(_translate("MainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

