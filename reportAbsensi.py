from PyQt4 import QtGui, QtCore
from raw_ui import reportPeriode_ui
import sys,os
import myDB
import sqlite3
import time
from xlwt import *
import lihatData
import exportPeriode

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


class Main(QtGui.QMainWindow,reportPeriode_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.judul="Report Absensi"
        self.folder_tgl='\\data\\Laporan\\'
        self.simpan = os.getcwd()+self.folder_tgl+"reportAbsensi"
        
        self.koneksiDatabase()
        self.setupUi(self)
        myDB.tampilan()
        self.setWindowTitle(self.judul)
        self.formNormal()
        self.aksi()
        self.onShow()

    def formNormal(self):
        self.dateEditAwal.setDate(QtCore.QDate.currentDate())
        self.tableWidget.clear()
        h = (        
        ("NIK"),
        ("Nama"),
        ('ID Absen'),
        ("   Jam Datang   "),
        ("   Jam Pulang   "),
        ("   Alasan Datang Terlambat   "),
        ("   Alasan Pulang Cepat   ")
        )
        self.tableWidget.setColumnCount(len(h))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(h)


    def aksi(self):
        self.tableWidget.doubleClicked.connect(self.onDblKlik)
        self.actionTambah_User.triggered.connect(self.onTambahUser)
        self.actionHapus.triggered.connect(self.onHapusUser)
        self.dateEditAwal.dateChanged.connect(self.onShow)
        self.pushButton.pressed.connect(self.onExport)
        
    def onExport(self):
        app = exportPeriode.Main()
        app.exec_()

    def onHapusUser(self):
        r = self.tableWidget.currentRow()
        if r < 0:
            pass
        else:
            NIK = str(self.tableWidget.item(r,0).text())
            nama = str(self.tableWidget.item(r,1).text())
            tanya = QtGui.QMessageBox.question(self, "Hapus Data:", "Anda yakin akan menghapus %s ?"%nama, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if tanya == QtGui.QMessageBox.Yes:
                try:
                    teks = "DELETE FROM karyawan WHERE NIK = '%s'"%(NIK)
                    self.cur.execute(teks)
                    self.db.commit()
                    QtGui.QMessageBox.information(self,"Berhasil","%s berhasil dihapus!"%nama)
                except Exception,e:
                    QtGui.QMessageBox.critical(self,"Gagal","Gagal menghapus %s \n %s"%(nama,e))
                self.onShow()
        

    def onTambahUser(self):
        a = lihatData.Main()
        a.exec_()
        self.onShow()

    def onDblKlik(self,item):
        r=item.row()        
        NIK = self.tableWidget.item(r,0).text()
        a = lihatData.Main(NIK = NIK)
        a.exec_()
        self.onShow()   

    def onShow(self):
        self.tableWidget.setRowCount(0)
        tgl_awal = self.dateEditAwal.date().toPyDate()
        self.sql = """      
            SELECT                 
                karyawan.NIK,
                nama,
                id_absen,
                datang,
                pulang,
                alasan1,
                alasan2                
            FROM karyawan LEFT JOIN absensi ON karyawan.NIK =absensi.NIK AND
                (absensi.tanggal = '%s') 
        """ %(tgl_awal)
        
        bar, jum = self.eksekusi(self.sql)
        self.tableWidget.setRowCount(jum)
        self.tableWidget.setSortingEnabled(False)
                
        for data in range(jum):
            id_absen = bar[data][2]
            datang = bar[data][3]
            pulang = bar[data][4]
            alasan1 = bar[data][5]
            alasan2 = bar[data][6]
            if datang ==None:
                datang = ""
            if pulang ==None:
                pulang =""
            if alasan1 == None:
                alasan1 = ""
            if alasan2 == None:
                alasan2 = ""
            teks=(
            bar[data][0],
            bar[data][1],
            id_absen,
            datang,
            pulang,
            alasan1,
            alasan2   
            )
            for i in range(len(teks)):
                item = QCustomTableWidgetItem(QtCore.QString(str(teks[i])))
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item.setToolTip(str(teks[i]))
                item.setText(str(teks[i]))
                self.tableWidget.setItem(data,i,item)
            
        self.warnaTabel()
        self.tableWidget.setSortingEnabled(True)        

    def warnaTabel(self):
        r = self.tableWidget.rowCount()
        for i in range(r):
            self.tableWidget.item(i, 2).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.tableWidget.item(i, 3).setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)                        
        self.tableWidget.resizeColumnsToContents()    
    
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