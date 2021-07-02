# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:09:10 2021

@author: AmandaVDC 2008300092 2E

"""
#CEK Program 
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    print("")
    print("===================================================================")
    print("                 DAFTAR MENU di KANTIN FTI UNMER                   ")
    print("===================================================================")
    print("          MENU MAKANAN                      MENU MINUMAN           ")
    print("          ------------                     ------------            ")
    print("                                  |                                ")
    print(" a = Nasi Goreng      : Rp 15.000 | a = Teh Dingin/      : Rp 2.500")
    print(" b = Lontong Goreng   : Rp 14.900 |     Hangat/Panas               ") 
    print(" c = Bakso Goreng     : Rp 12.900 | b = Kopi Dingin      : Rp 5.000")
    print(" d = Rujak Goreng     : Rp 13.000 | c = Kopi Teh Panas   : Rp 6.500")
    print(" e = Rujak Bakso      : Rp 15.000 | d = Coca Cola Dingin : Rp 3.500")
    print(" f = Rujak Bkso Pecel : Rp 17.000 | e = Coca Cola Panas  : Rp 5.000")
    
#input nama pembeli
    pembeli = input(">> Masukkan nama Pembeli : ")
    print ("Nama Pembeli : " + pembeli)     

#input dan hitung menu makan
    kode_mkn = ['a','b','c','d','e','f']
    nama_mkn = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso', 'Rujak Bakso Pecel']
    hrga_mkn = [15000,14900,12900,13000,15000,17000]
    
    pilihan_mkn = input(">> Masukkan Kode makanan yang akan dipesan = ")

#identifikasi pilihan            
    i = 0
    while i<len(nama_mkn):
            
        if kode_mkn[i] == pilihan_mkn:
            nm_mkn = nama_mkn[i]
            hrgsat_mkn = hrga_mkn[i]
        i+=1
        
#menampilkan harga satuan           
    print(">>> Nama Makanan         : " + nm_mkn)
    print(">>> Harga Makanan        : " + str(hrgsat_mkn))

#input jumlah pesanan
    qty_mkn     = input(">> Masukkan jumlah yang dipesan            = ")
    print(">>> Jumlah Makanan       : " + qty_mkn)
    
#total awal   
    tot_byr_mkn = hrgsat_mkn * int(qty_mkn)
    print(">>> Total                : " + str(tot_byr_mkn))
          
#input minuman dan harga minuman
    kode_mnm = ['a','b','c','d','e']
    nama_mnm = ['Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    hrga_mnm = [2500,5000,6500,3500,5000]
    
    pilihan_mnm = input(">> Masukkan Kode minuman yang akan dipesan = ")

#identifikasi pilihan        
    i = 0
    while i<len(nama_mnm):
            
        if kode_mnm[i] == pilihan_mnm:
            nm_mnm = nama_mnm[i]
            hrgsat_mnm = hrga_mnm[i]
        i+=1

#menampilkan harga satuan         
    print(">>> Nama Minuman         : " + nm_mnm)
    print(">>> Harga Minuman        : " + str(hrgsat_mnm))

#input jumlah pesanan
    qty_mnm     = input(">> Masukkan jumlah yang dipesan            = ") 
    print(">>> Jumlah Minuman       : " + qty_mnm)

#total awal         
    tot_byr_mnm = hrgsat_mnm * int(qty_mnm)
    print(">>> Total                : " + str(tot_byr_mnm))
    
#hitung total semua pesanan
    tot_byr = tot_byr_mkn + tot_byr_mnm
    print(" ")
    print(">> Total yang harus Dibayar : Rp " + str(tot_byr))

#melakukan pembayaran dan cek apa ada kembalian
    uangpembeli=int(input(">> Uang Tunai Pembeli       : Rp "))
    kembalian= uangpembeli - tot_byr
    print("> Kembalian :" + str(kembalian))
    print(" ")

#print struk   
    print("============================================")
    print("=========  S T R U K   B E L I   ===========")
    print("============================================")
    print (" Nama                       : " + pembeli)
    print (" Menu makanan yang dibeli   : " + nm_mkn)
    print (" Harga Makanan              : " + str(hrgsat_mkn))
    print (" jumlah makanan yang dibeli : " + str(qty_mkn))
    print (" Total Harga Makanan        : " + str(tot_byr_mkn))
    print (" Minuman yang dibeli        : " + nm_mnm)
    print (" Harga Minuman              : " + str(hrgsat_mnm))
    print (" jumlah minuman yang dibeli : " + str(qty_mnm))
    print (" Total Harga Minuman        : " + str(tot_byr_mnm))
    print ("_____________________________________________________+")
    print (" Tagihan                    : Rp. " + str(tot_byr))
    print (" Uang                       : Rp. " + str(uangpembeli))
    print (" Kembalian                  : Rp. " + str(kembalian))
    print("=====================================================")
    print("=============   TERIMA KASIH  =======================")
     
#ingin mengulang program ? 
    jwbprogram = input("ulang program ? (y/t) :  ")
    if jwbprogram=="t" or jwbprogram=="T":
                break
   
     
     
    
    