from PyQt4 import QtGui, QtCore
from raw_ui import lihatData_ui
import sys
import myDB
import sqlite3

class Main(QtGui.QDialog,lihatData_ui.Ui_Dialog):
    def __init__(self,parent = None,NIK = None):

        QtGui.QDialog.__init__(self)
        self.koneksiDatabase()
        self.setupUi(self)
        myDB.tampilan()
        self.setWindowTitle('Data Pengguna')
        self.comboShift()
        self.aksi()
        if NIK == None:
            self.lineEditNIK.setEnabled(True)
            self.lineEditNIK.setFocus()
        else:
            self.lineEditNIK.setText(NIK)
            self.onNIKEnter()

    def aksi(self):
        self.pushButtonKeluar.pressed.connect(self.onClose)
        self.lineEditNIK.returnPressed.connect(self.onNIKEnter)
        self.lineEditNama.returnPressed.connect(self.onNamaEnter)
        self.lineEditID.returnPressed.connect(self.onIDEnter)
        self.pushButtonSimpan.pressed.connect(self.onSimpanKlik)
        self.lineEditJobTitle.returnPressed.connect(self.onJobEnter)
        self.lineEditJobTitle.returnPressed.connect(self.pushButtonSimpan.setFocus)
        self.connect(QtGui.QShortcut(QtGui.QKeySequence(
            "Ctrl+S"), self), QtCore.SIGNAL('activated()'), self.onSimpanKlik)
        self.comboBox.currentIndexChanged.connect(self.onComboEnter)

    def onNamaEnter(self):
        self.lineEditID.setEnabled(True)
        self.lineEditID.setFocus()

    def onIDEnter(self):
        self.lineEditJobTitle.setEnabled(True)
        self.lineEditJobTitle.setFocus()

    def onJobEnter(self):
        self.comboBox.setEnabled(True)
        self.comboBox.setFocus()
        self.comboBox.showPopup()

    def comboShift(self):
        self.comboBox.clear()
        sql = "SELECT kode_shift FROM shift"
        bar,jum = self.eksekusi(sql)
        a = ['%s'%(bar[i][0]) for i in range(jum)]
        # self.comboBox.addItem("")
        self.comboBox.addItems(a)

    def onComboEnter(self):
        a = str(self.comboBox.currentText())
        if a!="":            
            sql = "SELECT keterangan FROM shift WHERE kode_shift = '%s'"%a
            bar,jum = self.eksekusi(sql)
            self.labelKeterangan.setText(bar[0][0])
        else:
            self.labelKeterangan.setText("")
        self.pushButtonSimpan.setEnabled(True)
        self.pushButtonSimpan.setFocus()

        
    def onSimpanKlik(self):
        NIK = str(self.lineEditNIK.text())
        nama = str(self.lineEditNama.text())
        id_absen = str(self.lineEditID.text())
        job_title = str(self.lineEditJobTitle.text())
        kode_shift = str(self.comboBox.currentText())
        if NIK=="":
            QtGui.QMessageBox.warning(self,"Perhatian!","NIK tidak boleh kosong!")
            self.lineEditNIK.setFocus()
        elif nama=="":
            QtGui.QMessageBox.warning(self,"Perhatian!","Nama tidak boleh kosong!")
            self.lineEditNama.setFocus()
        elif id_absen=="":
            QtGui.QMessageBox.warning(self,"Perhatian!","ID tidak boleh kosong!")
            self.lineEditID.setFocus()
        elif job_title=="":
            QtGui.QMessageBox.warning(self,"Perhatian!","Job Title tidak boleh kosong!")
            self.lineEditJobTitle.setFocus()
        else:
            if self.lineEditNIK.isEnabled():                
                cek = "SELECT id_absen FROM karyawan WHERE id_absen = '%s'"%(id_absen)
                bar,jum = self.eksekusi(cek)
                if jum==0:
                    try:
                        teks = "INSERT INTO karyawan VALUES('%s','%s','%s','%s','%s')"%(NIK,nama,id_absen,job_title, kode_shift)
                        self.cur.execute(teks)
                        self.db.commit()
                        QtGui.QMessageBox.information(self,"Informasi!","Data telah ditambah!")
                        self.onClose()
                    except Exception,e:
                        QtGui.QMessageBox.critical(self,"Gagal!","Gagal simpan data!%s"%str(e))
                else:
                    QtGui.QMessageBox.critical(self,"Perhatian!","ID absen sudah ada yang pake")
                    self.lineEditID.setFocus()
            else:
                try:
                    teks = "UPDATE karyawan SET nama = '%s',id_absen = '%s',job_title='%s', kode_shift = '%s' WHERE NIK = '%s'"%(nama,id_absen,job_title, kode_shift,  NIK)
                    self.cur.execute(teks)
                    self.db.commit()
                    QtGui.QMessageBox.information(self,"Informasi!","Data telah diupdate!")
                    self.onClose()
                except Exception,e:
                    QtGui.QMessageBox.critical(self,"Gagal!","Gagal simpan data!%s"%str(e))

    def onNIKEnter(self):
        NIK = self.lineEditNIK.text()
        cari = "SELECT NIK,nama,id_absen,job_title, kode_shift FROM karyawan WHERE NIK='%s' "%(NIK)        
        bar,jum = self.eksekusi(cari)
        if jum==0:
            self.lineEditNama.setEnabled(True)
            self.lineEditNama.setFocus()         
        else:
            self.lineEditNIK.setEnabled(False)
            self.lineEditNama.setText(bar[0][1])
            self.lineEditID.setText(bar[0][2])
            self.lineEditJobTitle.setText(bar[0][3])
            self.comboBox.setCurrentIndex(self.comboBox.findText(bar[0][4]))
            
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