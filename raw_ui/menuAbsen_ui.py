# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuAbsen.ui'
#
# Created: Thu Feb 09 04:12:47 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(714, 464)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.labelAbsenTerakhir = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelAbsenTerakhir.setFont(font)
        self.labelAbsenTerakhir.setText(_fromUtf8(""))
        self.labelAbsenTerakhir.setObjectName(_fromUtf8("labelAbsenTerakhir"))
        self.gridLayout.addWidget(self.labelAbsenTerakhir, 2, 1, 1, 1)
        self.labelNIK = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelNIK.setFont(font)
        self.labelNIK.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelNIK.setObjectName(_fromUtf8("labelNIK"))
        self.gridLayout.addWidget(self.labelNIK, 5, 0, 1, 4)
        self.labelNama = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNama.sizePolicy().hasHeightForWidth())
        self.labelNama.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.labelNama.setFont(font)
        self.labelNama.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.labelNama.setObjectName(_fromUtf8("labelNama"))
        self.gridLayout.addWidget(self.labelNama, 6, 0, 1, 4)
        self.lineEditNIK = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditNIK.setFont(font)
        self.lineEditNIK.setObjectName(_fromUtf8("lineEditNIK"))
        self.gridLayout.addWidget(self.lineEditNIK, 0, 2, 1, 1)
        self.pushButtonPulang = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonPulang.setFont(font)
        self.pushButtonPulang.setObjectName(_fromUtf8("pushButtonPulang"))
        self.gridLayout.addWidget(self.pushButtonPulang, 1, 1, 1, 1)
        self.labelJabatan = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelJabatan.setFont(font)
        self.labelJabatan.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelJabatan.setObjectName(_fromUtf8("labelJabatan"))
        self.gridLayout.addWidget(self.labelJabatan, 7, 0, 1, 4)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButtonDatang = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonDatang.setFont(font)
        self.pushButtonDatang.setObjectName(_fromUtf8("pushButtonDatang"))
        self.gridLayout.addWidget(self.pushButtonDatang, 1, 0, 1, 1)
        self.pushButtonBatal = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBatal.setIcon(icon)
        self.pushButtonBatal.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonBatal.setObjectName(_fromUtf8("pushButtonBatal"))
        self.gridLayout.addWidget(self.pushButtonBatal, 0, 3, 1, 1)
        self.labelJamDatang = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelJamDatang.setFont(font)
        self.labelJamDatang.setText(_fromUtf8(""))
        self.labelJamDatang.setObjectName(_fromUtf8("labelJamDatang"))
        self.gridLayout.addWidget(self.labelJamDatang, 3, 1, 1, 1)
        self.labelJamPulang = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelJamPulang.setFont(font)
        self.labelJamPulang.setText(_fromUtf8(""))
        self.labelJamPulang.setObjectName(_fromUtf8("labelJamPulang"))
        self.gridLayout.addWidget(self.labelJamPulang, 4, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.lineEditAlasan = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEditAlasan.setFont(font)
        self.lineEditAlasan.setText(_fromUtf8(""))
        self.lineEditAlasan.setObjectName(_fromUtf8("lineEditAlasan"))
        self.gridLayout.addWidget(self.lineEditAlasan, 9, 0, 1, 4)
        self.labelAlasan = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelAlasan.setFont(font)
        self.labelAlasan.setObjectName(_fromUtf8("labelAlasan"))
        self.gridLayout.addWidget(self.labelAlasan, 8, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditNIK, self.pushButtonDatang)
        MainWindow.setTabOrder(self.pushButtonDatang, self.pushButtonPulang)
        MainWindow.setTabOrder(self.pushButtonPulang, self.pushButtonBatal)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Jam Pulang :", None))
        self.label_2.setText(_translate("MainWindow", "Absen Terakhir :", None))
        self.label_3.setText(_translate("MainWindow", "Jam Datang :", None))
        self.labelNIK.setText(_translate("MainWindow", "TextLabel", None))
        self.labelNama.setText(_translate("MainWindow", "Nama", None))
        self.pushButtonPulang.setText(_translate("MainWindow", "Absen Pulang", None))
        self.labelJabatan.setText(_translate("MainWindow", "TextLabel", None))
        self.label.setText(_translate("MainWindow", "MASUKKAN PIN", None))
        self.pushButtonDatang.setText(_translate("MainWindow", "Absen Datang", None))
        self.pushButtonBatal.setText(_translate("MainWindow", "Batal", None))
        self.labelAlasan.setText(_translate("MainWindow", "Silahkan Masukkan Alasan :", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

