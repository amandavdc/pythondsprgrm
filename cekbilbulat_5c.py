# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:07:16 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

#cek sttus bilangan bulat
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    print ("=====================================================")
    print ("                                                     ")
    print ("           Menampilkan Nilai Huruf Dengan            ")
    print ("   Menginputkan Sebuah Bilangan Bulat Dari 0 - 100   ")
    print ("                                                     ")
    print ("=====================================================")
    
    n=1
    while int(n)>0 and int(n)<=100: 
#input umur
        n = input ("Masukkan nilai = ")
            
         #cek status
        if int(n)>0 and int(n)<=100:
            if int(n)>80:
                sts="Baik Sekali"
            elif int(n)>=65: sts="Baik"
            elif int(n)>=55: sts="Cukup"
            elif int(n)>=40: sts="Kurang"
            else:
                sts="Kurang Sekali"
            print(sts)

#ulangi, jika ingin mengecek kembali
            jwbprogram = input("Ulang progam ? y/t = ")
            if jwbprogram=="t" or jwbprogram=="T":
                break 
        
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break
        
    
        
    
    
    