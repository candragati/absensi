# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportPeriode.ui'
#
# Created: Fri Feb 10 08:14:10 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(240, 112)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEditAkhir = QtGui.QDateEdit(Dialog)
        self.dateEditAkhir.setCalendarPopup(True)
        self.dateEditAkhir.setObjectName(_fromUtf8("dateEditAkhir"))
        self.gridLayout.addWidget(self.dateEditAkhir, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEditAwal = QtGui.QDateEdit(Dialog)
        self.dateEditAwal.setCalendarPopup(True)
        self.dateEditAwal.setObjectName(_fromUtf8("dateEditAwal"))
        self.gridLayout.addWidget(self.dateEditAwal, 0, 1, 1, 1)
        self.pushButtonExcel = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/file_extension_xls.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonExcel.setIcon(icon)
        self.pushButtonExcel.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonExcel.setAutoDefault(False)
        self.pushButtonExcel.setObjectName(_fromUtf8("pushButtonExcel"))
        self.gridLayout.addWidget(self.pushButtonExcel, 2, 0, 1, 1)
        self.pushButtonBatal = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBatal.setIcon(icon1)
        self.pushButtonBatal.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonBatal.setAutoDefault(False)
        self.pushButtonBatal.setObjectName(_fromUtf8("pushButtonBatal"))
        self.gridLayout.addWidget(self.pushButtonBatal, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Tanggal Awal", None))
        self.label_2.setText(_translate("Dialog", "Tanggal Akhir", None))
        self.pushButtonExcel.setText(_translate("Dialog", "Excel", None))
        self.pushButtonBatal.setText(_translate("Dialog", "Batal", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

