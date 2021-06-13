# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:27:13 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

# nilai awal variabel = harga 1 printer

HargaPrinter = 660000
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    
# input jumlah beli
    print ("=====================================================")
    print ("                                                     ")
    print ("       Transakasi Pemeblian Printer EPSON T20        ")
    print ("                                                     ")
    print ("=====================================================")
    jmlbeli = input("jumlah printer epson T20 yang dibeli = ")
    
# proses hitung total
    totalbayar = int(HargaPrinter)*int(jmlbeli)

# hasil
    print("total bayar = Rp " + str (totalbayar))
    jwbprogram = input("Ulang progam ? y/t = ")
    if jwbprogram=="t" or jwbprogram=="T":
     break 