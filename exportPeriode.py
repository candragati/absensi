from PyQt4 import QtGui, QtCore
from raw_ui import exportPeriode_ui
import sys,os
import myDB
import sqlite3
import datetime
import time

from xlwt import *

class Main(QtGui.QDialog,exportPeriode_ui.Ui_Dialog):
    def __init__(self,parent = None):
        self.folder_tgl='\\data\\Laporan\\'
        self.judul="Report Absensi"
        QtGui.QDialog.__init__(self)
        self.koneksiDatabase()
        myDB.tampilan()
        self.setupUi(self)
        self.setWindowTitle('Export Periode')
        self.aksi()
        self.dateEditAwal.setDate(QtCore.QDate.currentDate())
        self.dateEditAkhir.setDate(QtCore.QDate.currentDate())

    def aksi(self):
        self.pushButtonBatal.pressed.connect(self.onClose)
        self.pushButtonExcel.pressed.connect(self.exportExcel)

    def exportExcel(self):            
        if os.path.exists(os.getcwd()+self.folder_tgl):
            pass
        else:
            os.makedirs(os.getcwd()+self.folder_tgl)        
        wbk=Workbook()
        styleHeader=easyxf(
            'font:bold 1;'
            'border:left thin,top thin,right thin,bottom thin;'
            'pattern:fore_colour yellow,pattern solid;'
            'alignment:horizontal center,vertical center,shrink_to_fit true')
        
        styleCell_R=easyxf(
            'border:left thin,top thin,right thin,bottom thin;'
            'font:name Calibri,height 200;'
            'alignment:horizontal right,vertical center,shrink_to_fit true')
        
        styleCell_Absen=easyxf(
            'border:left thin,top thin,right thin,bottom thin;'
            'font:name Calibri,height 200;'
            'pattern:fore_colour sky_blue,pattern solid;'
            'alignment:horizontal right,vertical center,shrink_to_fit true')

        styleCell_L=easyxf(
            'border:left thin,top thin,right thin,bottom thin;'
            'font:name Calibri,height 200;'
            'alignment:horizontal left,vertical center,shrink_to_fit true')
        
        styleCell_tgl=easyxf(
            'border:left thin,top thin,right thin,bottom thin;'
            'font:name Calibri,height 200;'
            'alignment:horizontal left,vertical center,shrink_to_fit true;',
            num_format_str='d-m-Y')
        
        date_format="%Y-%m-%d"
        tglAwal=datetime.datetime.strptime(str(self.dateEditAwal.date().toPyDate()),date_format)
        tglAkhir=datetime.datetime.strptime(str(self.dateEditAkhir.date().toPyDate()),date_format)
        delta=((tglAkhir-tglAwal).days)+1
        for i in range(delta):
            tgl = tglAwal+datetime.timedelta(days=i)
            tglSheet = tgl.strftime('%d-%m-%Y')
            
            sheet=wbk.add_sheet(str(tglSheet))         
            sheet.portrait=False     

            sheet.write(2,0,'Tanggal',styleHeader)   
            sheet.write(2,1,'Nomor NIK',styleHeader)   
            sheet.write(2,2,'Nama',styleHeader)   
            sheet.write(2,3,'Absen Datang',styleHeader)   
            sheet.write(2,4,'Absen Pulang',styleHeader)   
            sheet.write(2,5,'Alasan',styleHeader)   
            sheet.write(2,6,'Alasan',styleHeader)   

            sheet.col(0).width=270*14
            sheet.col(1).width=270*14
            sheet.col(2).width=270*30
            sheet.col(3).width=270*11
            sheet.col(4).width=269*11
            sheet.col(5).width=269*20
            sheet.col(6).width=269*20
            
            tgl_awal = str(tgl)[:10]
            sql = """      
                SELECT                 
                    karyawan.NIK,
                    nama,
                    datang,
                    pulang,
                    alasan1,
                    alasan2       
                FROM karyawan LEFT JOIN absensi ON karyawan.NIK =absensi.NIK AND
                    (absensi.tanggal = '%s') 
            """ %(tgl_awal)
            
            bar, jum = self.eksekusi(sql)
            for data in range(jum):
                datang = bar[data][2]
                pulang = bar[data][3]
                alasan1 = bar[data][4]
                alasan2 = bar[data][5]
                if datang ==None:
                    datang = ""
                if pulang ==None:
                    pulang =""
                if alasan1 == None:
                    alasan1 = ""
                if alasan2 == None:
                    alasan2 = ""
                
                data0=tglSheet
                data1=bar[data][0]
                data2=bar[data][1]
                data3=datang
                data4=pulang
                data5=alasan1
                data6=alasan2
                

                sheet.write(data+3,0,data0,styleCell_tgl)
                sheet.write(data+3,1,data1,styleCell_L)
                sheet.write(data+3,2,data2,styleCell_L)
                sheet.write(data+3,3,data3,styleCell_Absen)
                sheet.write(data+3,4,data4,styleCell_Absen)
                sheet.write(data+3,5,data5,styleCell_L)
                sheet.write(data+3,6,data6,styleCell_L)

                sheet.row(data+3).set_style(easyxf('font:name Calibri,height 200'))        
            
        
            styleJudul = easyxf(
                'align:vertical center,horizontal center;'
                'font:name Calibri,bold 1,height 400;'
                )
            
            sheet.write_merge(0,0,0,6,"ABSEN MANUAL",styleJudul)
            sheet.row(2).set_style(easyxf('font:height 300'))
            sheet.write_merge(jum+4,jum+4,0,6,"Generated at :"+time.ctime())
        try:
            wbk.save("Report Periode.xls")    
            os.startfile("Report Periode.xls")
        except (IOError,OSError),e:
            QtGui.QMessageBox.critical(self,"Kesalahan!","Gagal export data! \n%s"%e)
    
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