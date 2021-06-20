# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 06:39:30 2021

@author: Amanda Veby DC, NIM : 20083000092, Kelas : 2E
"""

# program akan mengulang saat menulis tombol y
jwbprogram = "y"
while  jwbprogram=="y" or jwbprogram=="Y":
    print ("====================================")
    print ("      CEK BIAYA PEMBELIAN OLI       ") 
    print ("     PADA BENGKEL UD.MATAHARI       ")
    print ("====================================")
    print (" DAFTAR OLI MOTOR :                 ")
    print ("                                    ")
    print ("  1. Duration SW20 1L      = 53000  ")
    print ("  2. Castrol Magnatec 1L   = 50000  ")
    print ("  3. Federal Supreme XX 1L = 54000  ")
    print ("  4. Yamalube 1L           = 45000  ")
    print ("  5. Shell 1L              = 46000  ")
    print ("====================================")

# menginput list data agar datanya dapat terambil
    nomer = [1,2,3,4,5]
    merk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]

# program akan menampilkan data dari 1 - 5, selain itu program tidak akan menampilkan data
    n=1
    while int(n)>0 and int(n)<=5: 
        
# masukkan pilihan nomer, agar bisa menampilkan data
        n = input (">> Masukkan pilihan barang = ")
            
# cek data
        if int(n)>0 and int(n)<=5:
            if int(n)==1:
                idx = 0
            elif int(n)==2:
                idx = 1
            elif int(n)==3:
                idx = 2
            elif int(n)==4:
                idx = 3
            elif int(n)==5:
                idx = 4
            else:
                idx = 0

# menampilkan hasil data yang telah diambil
            print() 
            print("> Pilihan Merk  = " + merk[idx])
            print("> Harga Merk    = Rp. " + str (harga[idx]))

# input ppn, jumlah beli, dan menampilkan harga awal
            ppnawal = harga[idx]*0.01
            print("> PPN           = Rp. " + str (ppnawal))
            
            jmlBeli = input(">> Masukkan Jumlah Yang Dibeli = ")
            
            hargaawal = harga[idx]*int(jmlBeli)
            print("> Harga Awal     = Rp. " + str (hargaawal))

# jika harga <= 200.000 akan mendapat diskon 5%
            if int(hargaawal)>=200000:
                diskon = int(hargaawal)*0.05
            elif int(hargaawal)<200000:
                diskon = int(hargaawal)*0.0
            print("> diskon sebesar = Rp. " + str (diskon))

# menampilkan hasil total awal
            totalawal = int(hargaawal) - int(diskon)
            print("> Total Awal     = Rp. " + str (totalawal))
        
# menampilkan hsil total akhir atau bayar
            TotalBayar = int(totalawal)+int(ppnawal)
            print("> Total Bayar    = Rp. " + str (TotalBayar))
            
#ulangi, jika ingin mengecek kembali
            
        else:
            pesan=">>> Pilihan tidak tersedia"
            print(pesan)
            break
        
        jwbprogram = input("Ulang progam ? y/t = ")
        if jwbprogram=="t" or jwbprogram=="T":       
            break
        
        
    
        
    
    
    
