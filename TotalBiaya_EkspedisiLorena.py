# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 05:57:52 2021

@author: Amanda Veby Dwi Candra. NIM : 20083000092
"""

# Program akan mengulang jika masih mau menghitung
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    print ("===============================")
    print ("     CEK BIAYA TOTAL KIRIM     ") 
    print ("    EKSPEDISI LORENA MALANG    ")
    print ("===============================")
    print (" 1. Kode A = Surabaya ")
    print (" 2. Kode B = Bandung  ")
    print ("===============================")

# input list data
    nomer =[1,2]
    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]

# jika lebih dari 3 saat mencari data, program akan menyuruh tulis ulang
    n=1
    while int(n)>0 and int(n)<=2: 

# menginput kode untuk diambil list datanya
        n = input ("Pilih No Kode Kota = ")
            
#cek status
        if int(n)>0 and int(n)<=2:
            if int(n)==1:
                idx = 0
            elif int(n)==2:
                idx = 1
            else:
                idx = 0

# menampilkan hasil yang telah diambil
            print(">>> Pilihan Tujuan = " + kota[idx])
            print(">>> Jarak          = " + str(jarak[idx]) + " km")
            print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))
            
# menampilkan total bayar
            totongkir = jarak[idx]*ongkirperkm[idx]
    
            print(">>>-------------------------------------")
            print(">>> Total Biaya     = Rp." + str(totongkir))
            
        else:
            print()
            print(">>> Pilihan tidak tersedia")
            print(">>>   Coba input kembali  ")
            print()
            break
        
# ingin mengulang kembali?
        jwbprogram = input("Ulang progam ? y/t = ")
        if jwbprogram=="t" or jwbprogram=="T":
            break 