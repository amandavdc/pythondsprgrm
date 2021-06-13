# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:22:03 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

#cek kelulusan, jika nilai > 60 maka LULUS, selain itu ULANG
jwb = "y"
while  jwb=="y" or jwb=="Y":
    print ("===========================")
    print ("       CEK KELULUSAN       ")
    print ("===========================")
    
    #input variabel
    n = input ("Masukkan Nilaimu = ")
    
    #cek status
    if int(n)>60:
        sts = "LULUS"
    else: 
        sts = "ULANG"
    print(sts)
    
    #ulangi, jika ingin mengecek kembali
    jwb = input("Mulai lagi ? y/t = ")
    if jwb=="t" or jwb=="T":
        break 