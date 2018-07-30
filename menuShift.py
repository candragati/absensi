from PyQt4 import QtGui, QtCore
from raw_ui import menuShift_ui
import sys
import myDB
import sqlite3
import string
import time
import datetime

class QCustomTableWidgetItem (QtGui.QTableWidgetItem):
    def __init__ (self, value):
        super(QCustomTableWidgetItem, self).__init__(QtCore.QString('%s' % value))

    def __lt__ (self, other):
        if (isinstance(other, QCustomTableWidgetItem)):
            try:
                selfDataValue  = float(self.data(QtCore.Qt.EditRole).toString().replace(',',''))
                otherDataValue = float(other.data(QtCore.Qt.EditRole).toString().replace(',',''))
                return selfDataValue < otherDataValue
            except:
                return QtGui.QTableWidgetItem.__lt__(self, other)
        else:
            return QtGui.QTableWidgetItem.__lt__(self, other)



class Main(QtGui.QMainWindow,menuShift_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.koneksiDatabase()
        self.setupUi(self)
        myDB.tampilan()
        self.setWindowTitle('menu Shift')
        self.onShow()
        self.aksi()
        self.formNormal()
    
    def formNormal(self):
        self.lineEditDept.clear()
        self.lineEditKodeShift.clear()
        self.comboBoxHari.setCurrentIndex(0)
        self.lineEditDept.setEnabled(False)
        self.lineEditKodeShift.setEnabled(False)
        self.comboBoxHari.setEnabled(False)
        self.pushButtonInput.setEnabled(False)
        self.timeEditDatang.setEnabled(False)
        self.timeEditPulang.setEnabled(False)
        self.timeEditDatang.setTime(QtCore.QTime(0,0))
        self.timeEditPulang.setTime(QtCore.QTime(0,0))
        # self.tableWidget.setEnabled(True)
        self.tableWidgetShift.setEnabled(True)
        self.actionTambah_User.setEnabled(True)

    def aksi(self):
        self.tableWidgetShift.currentCellChanged.connect(self.onTabelShiftKlik)
        self.actionTambah_User.triggered.connect(self.onTambah)
        self.actionBatal.triggered.connect(self.formNormal)
        self.lineEditKodeShift.returnPressed.connect(self.onKodeShiftEnter)
        self.comboBoxHari.currentIndexChanged.connect(self.onComboHari)
        self.tableWidgetShift.doubleClicked.connect(self.tabelShiftEdit)

    def tabelShiftEdit(self):
        a = self.tableWidgetShift.currentRow()
        kode_shift = self.tableWidgetShift.item(a,0).text()
        keterangan = self.tableWidgetShift.item(a,1).text()
        self.lineEditKodeShift.setText(kode_shift)
        self.lineEditDept.setText(keterangan)
        self.comboBoxHari.setEnabled(True)
        self.comboBoxHari.setFocus()
        

    def onComboHari(self):
        hari = int(self.comboBoxHari.currentIndex())+1
        kode_shift = str(self.lineEditKodeShift.text())
        sql  = "SELECT masuk,keluar FROM jam_shift WHERE kode_shift = '%s' AND hari = '%s'"%(kode_shift,hari)        
        bar,jum = self.eksekusi(sql)
        try:
            jam_datang = string.split(bar[0][0],':')
            jam_pulang = string.split(bar[0][1],':')

            self.timeEditDatang.setTime(QtCore.QTime(int(jam_datang[0]),int(jam_datang[1])))
            self.timeEditPulang.setTime(QtCore.QTime(int(jam_pulang[0]),int(jam_pulang[1])))
            self.timeEditDatang.setEnabled(True)
            self.timeEditPulang.setEnabled(True)
            self.pushButtonInput.setEnabled(True)
            self.tableWidget.selectRow(hari-1)
        except:
            pass

    def onKodeShiftEnter(self):
        kode = str(self.lineEditKodeShift.text()).upper()
        self.lineEditKodeShift.setText(kode)
        kode_shift = """
        SELECT keterangan FROM shift WHERE kode_shift = '%s'
        """%kode
        bar,jum = self.eksekusi(kode_shift)
        if jum == 0 :
            self.lineEditDept.setEnabled(True)
            self.lineEditDept.setFocus()

        else:

            for i in self.tableWidgetShift.findItems(kode,QtCore.Qt.MatchExactly):
                self.tableWidgetShift.setCurrentItem(i)
                
                
            
            self.lineEditDept.setText(bar[0][0])
            self.comboBoxHari.setEnabled(True)
            self.lineEditKodeShift.setEnabled(False)
            self.comboBoxHari.setFocus()
            self.comboBoxHari.showPopup()

    def onTambah(self):
        self.lineEditKodeShift.clear()
        self.lineEditDept.clear()
        self.lineEditKodeShift.setEnabled(True)
        self.lineEditKodeShift.setFocus()
        self.tableWidget.setEnabled(False)
        self.tableWidgetShift.setEnabled(False)
        self.actionTambah_User.setEnabled(False)

    def onTabelShiftKlik(self):
        a = self.tableWidgetShift.currentRow()
        kode = self.tableWidgetShift.item(a,0).text()
        self.onShowJam(kode)

    def onShowJam(self,kode):

        kode_shift = """
        SELECT hari,masuk,keluar FROM jam_shift WHERE kode_shift = '%s' order by 1 asc
        """%kode
        bar,jum = self.eksekusi(kode_shift)
        for data in range(jum):
            teks=(
            
            bar[data][1],
            bar[data][2]
            )
            for i in range(len(teks)):
                item = QCustomTableWidgetItem(QtCore.QString(str(teks[i])))
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setToolTip(str(teks[i]))
                item.setText(str(teks[i]))
                self.tableWidget.setItem(data,i,item)


    def onShow(self):
        self.tableWidgetShift.setRowCount(0)
        
        self.sql = """      
            SELECT                 
                kode_shift,
                keterangan
            FROM shift ORDER BY kode_shift ASC
        """ 
        
        bar, jum = self.eksekusi(self.sql)
        self.tableWidgetShift.setRowCount(jum)
        self.tableWidgetShift.setSortingEnabled(False)
                
        for data in range(jum):
            teks=(
            bar[data][0],
            bar[data][1]       
            )
            for i in range(len(teks)):
                item = QCustomTableWidgetItem(QtCore.QString(str(teks[i])))
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setToolTip(str(teks[i]))
                item.setText(str(teks[i]))
                self.tableWidgetShift.setItem(data,i,item)
            
        self.warnaTabel()
        self.tableWidgetShift.setSortingEnabled(True)        

    def warnaTabel(self):
        self.tableWidgetShift.resizeColumnsToContents()
    
    def koneksiDatabase(self):
        self.db = sqlite3.connect("data/absensi.db")
        self.cur = self.db.cursor()       

    def eksekusi(self,sql):
        self.cur.execute(sql)
        lineData = self.cur.fetchall()
        totData = len(lineData)
        return lineData, totData

    def onClose(self):
        self.db.close()
        self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())