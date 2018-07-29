from PyQt4 import QtGui, QtCore
from raw_ui import menuAbsen_ui
import sys
import myDB
import sqlite3
import time
import datetime
class Main(QtGui.QMainWindow,menuAbsen_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        self.koneksiDatabase()
        self.setupUi(self)
        myDB.tampilan()
        self.setWindowTitle('menu Absensi')
        self.aksi()
        self.Normal()
        self.status = 0
        
    def aksi(self):
        self.pushButtonDatang.pressed.connect(self.absenDatang)
        self.pushButtonPulang.pressed.connect(self.absenPulang)
        self.pushButtonBatal.pressed.connect(self.Normal)
        self.lineEditNIK.returnPressed.connect(self.onNikEnter)   
        self.lineEditAlasan.returnPressed.connect(self.onAlasanEnter)

    def absenDatang(self):
        now = datetime.datetime.now()
        weekDay = int(datetime.datetime.weekday(now))+1
        NIK = self.labelNIK.text()
        cek = """
            SELECT 
                jam_shift.masuk
            FROM 
                jam_shift,karyawan 
            WHERE                 
                karyawan.kode_shift=jam_shift.kode_shift 
            AND karyawan.NIK = '%s' 
            AND jam_shift.hari = '%s'
            """%(NIK,weekDay)
        barCek,jumCek = self.eksekusi(cek)

        jam_shift =  barCek[0][0]        
        # jam_shift = '07:40'
        if  now.strftime('%H:%M') > jam_shift :
            self.pushButtonDatang.setEnabled(False)
            self.pushButtonPulang.setEnabled(False)
            self.labelAlasan.show()
            self.lineEditAlasan.show()            
            self.lineEditAlasan.setFocus()
            self.status = 1
        else:
            self.inputDatang()

    
    def inputDatang(self):
        jam = str(time.strftime("%X"))
        tanggal = str(datetime.date.today())
        NIK = self.labelNIK.text()   
        alasan1 = str(self.lineEditAlasan.text())
        test = "SELECT * FROM absensi WHERE tanggal = '%s' AND NIK = '%s'"%(tanggal,NIK)
        bar,jum = self.eksekusi(test)             
        if jum == 0:
            teks = "INSERT INTO absensi VALUES('%s','%s','%s','','%s','')"%(tanggal,NIK,jam,alasan1)
        else:
            teks = "UPDATE absensi SET datang = '%s',alasan1 = '%s' WHERE tanggal = '%s' AND NIK = '%s'"%(jam,alasan1,tanggal,NIK)
        self.cur.execute(teks)
        self.db.commit()
        QtGui.QMessageBox.information(self,"Informasi","<font size=20>%s datang jam %s</font>"%(str(self.labelNama.text()),jam))
        self.Normal()

    def Normal(self):
        self.lineEditNIK.clear()
        self.labelJabatan.clear()
        self.labelNIK.clear()
        self.labelNama.clear()
        self.labelAbsenTerakhir.clear()
        self.labelJamDatang.clear()
        self.labelJamPulang.clear()
        self.lineEditAlasan.clear()
        self.pushButtonDatang.setEnabled(False)
        self.pushButtonPulang.setEnabled(False)
        self.lineEditNIK.setEnabled(True)
        self.lineEditNIK.setFocus()
        self.lineEditAlasan.hide()
        self.labelAlasan.hide()

    def onAlasanEnter(self):        
        if self.status ==1:
            if str(self.lineEditAlasan.text())=="":
                QtGui.QMessageBox.warning(self,"Perhatian!","Alasan harus diisi")
                self.lineEditAlasan.setFocus()
            else:
                self.inputDatang()
        elif self.status ==2:
            if str(self.lineEditAlasan.text())=="":
                QtGui.QMessageBox.warning(self,"Perhatian!","Alasan harus diisi")
                self.lineEditAlasan.setFocus()
            else:
                self.inputPulang()
        else:
            pass

        
    def absenPulang(self):
        now = datetime.datetime.now()
        weekDay = int(datetime.datetime.weekday(now))+1
        NIK = self.labelNIK.text()
        cek = """
            SELECT 
                jam_shift.keluar
            FROM 
                jam_shift,karyawan 
            WHERE                 
                karyawan.kode_shift=jam_shift.kode_shift 
            AND karyawan.NIK = '%s' 
            AND jam_shift.hari = '%s'
            """%(NIK,weekDay)
        barCek,jumCek = self.eksekusi(cek)
        
        jam_shift =  barCek[0][0]
        # jam_shift = '08:00'       
        
        if  now.strftime('%H:%M') < jam_shift :
            self.pushButtonDatang.setEnabled(False)
            self.pushButtonPulang.setEnabled(False)
            self.labelAlasan.show()
            self.lineEditAlasan.show()            
            self.lineEditAlasan.setFocus()
            self.status = 2
        else:
            self.inputPulang()

    def inputPulang(self):
        jam = str(time.strftime("%X"))
        tanggal = str(datetime.date.today())
        NIK = self.labelNIK.text()        
        alasan2 = (self.lineEditAlasan.text())
        test = "SELECT * FROM absensi WHERE tanggal = '%s' AND NIK = '%s'"%(tanggal,NIK)
        bar,jum = self.eksekusi(test)
        if jum == 0:
            teks = "INSERT INTO absensi VALUES('%s','%s','','%s','','%s')"%(tanggal,NIK,jam,alasan2)
        else:
            teks = "UPDATE absensi SET pulang = '%s',alasan2 ='%s' WHERE tanggal = '%s' AND NIK = '%s'"%(jam,alasan2,tanggal,NIK)
        self.cur.execute(teks)
        self.db.commit()
        QtGui.QMessageBox.information(self,"Informasi","<font size=20>%s pulang jam %s</font>"%(str(self.labelNama.text()),jam))
        self.Normal()

    def onNikEnter(self):
        self.lineEditNIK.setEnabled(False)
        teks = self.lineEditNIK.text()        
        cari = "SELECT nama,job_title,NIK from karyawan WHERE NIK='%s' OR id_absen='%s'"%(teks,teks)        
        bar,jum = self.eksekusi(cari)
        if jum==0:
            QtGui.QMessageBox.critical(self,"","Tidak ditemukan data!")
            self.Normal()
        else:
            self.labelNama.setText(bar[0][0])
            self.labelJabatan.setText(bar[0][1])
            self.labelNIK.setText(bar[0][2])
            self.lineEditNIK.clear()
            self.pushButtonDatang.setEnabled(True)
            self.pushButtonPulang.setEnabled(True)
            tanggal = str(QtCore.QDate.currentDate().toPyDate())
            absenTerakhir = "SELECT tanggal,datang,pulang from absensi WHERE NIK='%s' AND (tanggal <='%s') ORDER BY 1 DESC LIMIT 1"%(bar[0][2],tanggal)
            bar,jum = self.eksekusi(absenTerakhir)
            a =str(datetime.datetime.strptime(bar[0][0],'%Y-%m-%d'))[:10]
            now = datetime.datetime.now().strftime('%Y-%m-%d')
            
            if a == now and bar[0][1]=="":
                self.pushButtonDatang.setEnabled(True)
                self.pushButtonPulang.setEnabled(False)
                self.pushButtonDatang.setFocus()
            elif a == now and bar[0][2]=="":
                self.pushButtonPulang.setEnabled(True)
                self.pushButtonPulang.setFocus()
                self.pushButtonDatang.setEnabled(False)
            elif a!=now:
                self.pushButtonDatang.setEnabled(True)
                self.pushButtonPulang.setEnabled(False)
                self.pushButtonDatang.setFocus()
            else:
                pass

            self.labelAbsenTerakhir.setText(bar[0][0])
            self.labelJamDatang.setText(bar[0][1])
            self.labelJamPulang.setText(bar[0][2])
            

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