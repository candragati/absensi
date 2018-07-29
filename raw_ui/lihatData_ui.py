# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lihatData.ui'
#
# Created: Sun Jul 29 11:36:45 2018
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
        Dialog.resize(412, 216)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEditNama = QtGui.QLineEdit(Dialog)
        self.lineEditNama.setEnabled(False)
        self.lineEditNama.setObjectName(_fromUtf8("lineEditNama"))
        self.gridLayout.addWidget(self.lineEditNama, 2, 1, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        self.pushButtonKeluar = QtGui.QPushButton(Dialog)
        self.pushButtonKeluar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/door_in.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonKeluar.setIcon(icon)
        self.pushButtonKeluar.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonKeluar.setAutoDefault(False)
        self.pushButtonKeluar.setObjectName(_fromUtf8("pushButtonKeluar"))
        self.gridLayout_4.addWidget(self.pushButtonKeluar, 0, 1, 1, 1)
        self.pushButtonSimpan = QtGui.QPushButton(Dialog)
        self.pushButtonSimpan.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSimpan.setIcon(icon1)
        self.pushButtonSimpan.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonSimpan.setAutoDefault(False)
        self.pushButtonSimpan.setObjectName(_fromUtf8("pushButtonSimpan"))
        self.gridLayout_4.addWidget(self.pushButtonSimpan, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEditID = QtGui.QLineEdit(Dialog)
        self.lineEditID.setEnabled(False)
        self.lineEditID.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditID.setObjectName(_fromUtf8("lineEditID"))
        self.gridLayout.addWidget(self.lineEditID, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEditNIK = QtGui.QLineEdit(Dialog)
        self.lineEditNIK.setEnabled(False)
        self.lineEditNIK.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditNIK.setObjectName(_fromUtf8("lineEditNIK"))
        self.gridLayout.addWidget(self.lineEditNIK, 1, 1, 1, 1)
        self.lineEditJobTitle = QtGui.QLineEdit(Dialog)
        self.lineEditJobTitle.setEnabled(False)
        self.lineEditJobTitle.setObjectName(_fromUtf8("lineEditJobTitle"))
        self.gridLayout.addWidget(self.lineEditJobTitle, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 5, 1, 1, 1)
        self.labelKeterangan = QtGui.QLabel(Dialog)
        self.labelKeterangan.setObjectName(_fromUtf8("labelKeterangan"))
        self.gridLayout.addWidget(self.labelKeterangan, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_4.setText(_translate("Dialog", "Job Title :", None))
        self.label.setText(_translate("Dialog", "NIK :", None))
        self.label_2.setText(_translate("Dialog", "Nama :", None))
        self.label_3.setText(_translate("Dialog", "ID Absen :", None))
        self.label_5.setText(_translate("Dialog", "Kode SHift :", None))
        self.labelKeterangan.setText(_translate("Dialog", "Keterangan", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

