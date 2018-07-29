# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utama.ui'
#
# Created: Thu Jan 26 08:45:28 2017
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
        MainWindow.resize(787, 508)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout_2.addWidget(self.mdiArea, 0, 0, 1, 1)
        self.labelJam = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(14)
        self.labelJam.setFont(font)
        self.labelJam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelJam.setObjectName(_fromUtf8("labelJam"))
        self.gridLayout_2.addWidget(self.labelJam, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAdministrator = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/premium_support.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdministrator.setIcon(icon)
        self.actionAdministrator.setObjectName(_fromUtf8("actionAdministrator"))
        self.actionExcel = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/file_extension_xls.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExcel.setIcon(icon1)
        self.actionExcel.setObjectName(_fromUtf8("actionExcel"))
        self.actionLihatData = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/eye.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLihatData.setIcon(icon2)
        self.actionLihatData.setObjectName(_fromUtf8("actionLihatData"))
        self.actionBatal = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBatal.setIcon(icon3)
        self.actionBatal.setObjectName(_fromUtf8("actionBatal"))
        self.actionAbsen = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/user.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbsen.setIcon(icon4)
        self.actionAbsen.setObjectName(_fromUtf8("actionAbsen"))
        self.toolBar.addAction(self.actionAbsen)
        self.toolBar.addAction(self.actionAdministrator)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelJam.setText(_translate("MainWindow", "TextLabel", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAdministrator.setText(_translate("MainWindow", "Administrator", None))
        self.actionExcel.setText(_translate("MainWindow", "Excel", None))
        self.actionLihatData.setText(_translate("MainWindow", "LihatData", None))
        self.actionBatal.setText(_translate("MainWindow", "Batal", None))
        self.actionAbsen.setText(_translate("MainWindow", "Absen", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

