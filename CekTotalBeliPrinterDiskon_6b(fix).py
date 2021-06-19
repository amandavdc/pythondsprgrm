# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:27:13 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

# nilai awal variabel = harga 1 printer

HargaPrinter = 660000
Minimdiskon = 1500000
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    
# input jumlah beli
    print ("=====================================================")
    print ("                                                     ")
    print ("       Transakasi Pembelian Printer EPSON T20        ")
    print ("                                                     ")
    print ("=====================================================")
    jmlbeli = input("jumlah printer epson T20 yang dibeli = ")
    
# proses hitung totalawal
    totalawal = int(HargaPrinter)*int(jmlbeli)

# hasil sementara
    print("total awal = Rp " + str (totalawal))

# jika pembelian diata 1.5jt, maka diskon 15%
    if int(totalawal)>1500000:
        diskon = int(totalawal)*15/100
    elif int(totalawal)<1500000:
        diskon = int(totalawal)*0/100
    print("diskon sebesar = Rp " + str (diskon))

# hasil akhir
    totalakhir = int(totalawal)-int(diskon)
    print("Total Akhir = Rp " + str (totalakhir))
    
# transaksi kembali?
    jwbprogram = input("Ulang progam ? y/t = ")
    if jwbprogram=="t" or jwbprogram=="T":
     break 