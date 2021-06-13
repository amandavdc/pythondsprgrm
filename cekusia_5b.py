# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:59:31 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

#cek umur
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    print ("===========================")
    print ("     CEK TINGKAT USIA      ")
    print ("===========================")
    
    u=1
    while int(u)>0 and int(u)<=100: 
#input umur
        u = input ("Masukkan Umur = ")
            
         #cek status
        if int(u)>0 and int(u)<=100:
            if int(u)>=60:
                sts="lansia"
            elif int(u)>=35: sts="Dewasa"
            elif int(u)>=18: sts="Pemuda"
            elif int(u)>=15: sts="Remaja"
            else:
                sts="Anak-anak"
            print(sts)

#ulangi, jika ingin mengecek kembali
            jwbprogram = input("Ulang progam ? y/t = ")
            if jwbprogram=="t" or jwbprogram=="T":
                break 
        
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break
        
    
        
    
    
    