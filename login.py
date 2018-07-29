from PyQt4 import QtGui, QtCore
from raw_ui import login_ui
import sys
import myDB
import sqlite3





class Main(QtGui.QDialog,login_ui.Ui_Dialog):
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self)
        self.koneksiDatabase()
        myDB.tampilan()
        self.setupUi(self)
        self.setWindowTitle('Login Administrator')
        self.lineEditNIK.setFocus()
        self.aksi()
        self.sukses =0

    def aksi(self):
        self.pushButtonLogin.pressed.connect(self.onLoginKlik)
        self.pushButtonBatal.pressed.connect(self.onClose)
        self.lineEditNIK.returnPressed.connect(self.lineEditPassword.setFocus)
        self.lineEditPassword.returnPressed.connect(self.onLoginKlik)

    def onLoginKlik(self):
        NIK = str(self.lineEditNIK.text())
        password = str(self.lineEditPassword.text())
        if NIK =='admin' and password =='admin123':
            self.sukses =1
            self.onClose()
        else:
            QtGui.QMessageBox.critical(self,"Gagal Login!","Tidak dapat login!")
    
    def getKode(self):
        return self.sukses
        
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