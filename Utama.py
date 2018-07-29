from PyQt4 import QtGui,QtCore
from raw_ui import utama_ui
import sys
import myDB
import sqlite3
import time
import login
import menuAbsen
import reportAbsensi
import menuShift

class Main(QtGui.QMainWindow,utama_ui.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        try:
            QtGui.QApplication.setStyle('Plastique')
        except:
            pass
        
        self.koneksiDatabase()
        self.setupUi(self)
        myDB.tampilan()
        self.setWindowTitle('Absensi Manual')        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.Time)
        # Reduced update time to fasten the change from w/ secs to w/o secs
        timer.start(10)
        
        self.showFullScreen()
        self.onAbsensi()
        self.aksi()

    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_F11:
            self.toogleFS()
            
    def toogleFS(self):
        if self.windowState() & QtCore.Qt.WindowFullScreen:
            self.showMaximized()
        else:
            self.showFullScreen()   
    
    def aksi(self):
        self.actionAdministrator.triggered.connect(self.onLogin)
        self.actionAbsen.triggered.connect(self.onAbsensi)
        

    def onReport(self):
        sub2 = menuShift.Main()
        self.mdiArea.addSubWindow(sub2)
        sub2.showMaximized()
        sub = reportAbsensi.Main()
        self.mdiArea.addSubWindow(sub)
        sub.showMaximized()


    def onAbsensi(self):
        self.mdiArea.closeAllSubWindows()
        self.actionAdministrator.setEnabled(True)
        sub = menuAbsen.Main()
        self.mdiArea.addSubWindow(sub)
        sub.showMaximized()

    def onLogin(self):
        app = login.Main()
        app.exec_()
        kode = app.getKode()
        if kode ==1:
            self.actionAdministrator.setEnabled(False)
            self.mdiArea.closeAllSubWindows()
            self.onReport()
        else:
            self.actionAdministrator.setEnabled(True)

    def Time(self):
        waktu = time.strftime("%d %B %Y %H" + ":" + "%M" + ":" + "%S")
        self.labelJam.setText(waktu)

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