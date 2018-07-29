# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Thu Jan 26 05:04:30 2017
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
        Dialog.resize(276, 114)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEditPassword = QtGui.QLineEdit(Dialog)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.gridLayout.addWidget(self.lineEditPassword, 1, 2, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonBatal = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBatal.setIcon(icon)
        self.pushButtonBatal.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonBatal.setAutoDefault(False)
        self.pushButtonBatal.setObjectName(_fromUtf8("pushButtonBatal"))
        self.gridLayout_3.addWidget(self.pushButtonBatal, 0, 1, 1, 1)
        self.pushButtonLogin = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/administrator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogin.setIcon(icon1)
        self.pushButtonLogin.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonLogin.setAutoDefault(False)
        self.pushButtonLogin.setObjectName(_fromUtf8("pushButtonLogin"))
        self.gridLayout_3.addWidget(self.pushButtonLogin, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEditNIK = QtGui.QLineEdit(Dialog)
        self.lineEditNIK.setObjectName(_fromUtf8("lineEditNIK"))
        self.gridLayout.addWidget(self.lineEditNIK, 0, 2, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/lock.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonBatal.setText(_translate("Dialog", "Cancel", None))
        self.pushButtonLogin.setText(_translate("Dialog", "Login", None))
        self.label_2.setText(_translate("Dialog", "Password :", None))
        self.label.setText(_translate("Dialog", "NIK", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

