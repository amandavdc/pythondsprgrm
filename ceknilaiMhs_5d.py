# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 21:18:49 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

#cek status huruf mahasiswa saat mendapat nilai
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    print ("=========================================")
    print ("                                         ")
    print ("           Penilaian Mahasiwa            ")
    print ("                                         ")
    print ("=========================================")
    
    n=1
    while int(n)>0 and int(n)<=100: 
#input umur
        n = input ("Masukkan nilai = ")
            
         #cek status
        if int(n)>0 and int(n)<=100:
            if int(n)>=91:
                sts="A"
            elif int(n)>=81: sts="B"
            elif int(n)>=71: sts="C"
            else:
                sts="D"
            print(sts)

#ulangi, jika ingin mengecek kembali
            jwbprogram = input("Ulang progam ? y/t = ")
            if jwbprogram=="t" or jwbprogram=="T":
             break 
        
        else:
            pesan=">>> Masukkan angka usia 0-100 saja"
            print(pesan)
            break
        
    
        
    
    
    
