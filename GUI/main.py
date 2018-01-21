import os, sys, io
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Dialog import Ui_MainWindow

class MainW(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.openBtn.clicked.connect(self.OpenFile)
        self.outBtn.clicked.connect(self.OutDir)
        self.convertBtn.clicked.connect(self.Convert)

        # Fill default value of Code Store
        # self.row_codestore_spin.setText('0')
        # self.col_codestore_spin.setText('0')

        # Fill default value of PO Number
        # self.row_ponumber_Edit.setText('0')
        # self.col_ponumber_Edit.setText('0')
    def Convert(self) :
        # Code Store
        CSrow = self.row_spin_codestore.value()
        CScol = self.col_spin_codestore.value()

        # PO Number
        PNrow = self.row_spin_ponumber.value()
        PNcol = self.col_spin_ponumber.value()

        # Barcode
        BDrow = self.row_spin_barcode.value()
        BDcol = self.col_spin_barcode.value()

        # Quanity
        QTrow = self.row_spin_quantity.value()
        QTcol = self.col_spin_quantity.value()

        # Quanity
        MKrow = self.row_spin_mdlkarton.value()
        MKcol = self.col_spin_mdlkarton.value()

        print(CSrow)

    def OutDir(self) :
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        directory = QFileDialog.getExistingDirectory(self,
                "Select Directory",
                self.outputEdit.text(), options=options)

        if directory:
            self.outputEdit.setText(os.path.abspath(directory))

    def OpenFile(self) :
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                "Open File", self.openEdit.text(),
                "Excel (*.csv *.xls *.xlsx )", options=options)

        if fileName :
            dirName = os.path.dirname(os.path.abspath(fileName)) # get directory file
            self.openEdit.setText(os.path.abspath(fileName)) # set path to text edit

            if not self.outputEdit.text() : # check if output edit text empty
                self.outputEdit.setText(dirName+"\Output")

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = MainW()
    window.show()
    sys.exit(app.exec_())