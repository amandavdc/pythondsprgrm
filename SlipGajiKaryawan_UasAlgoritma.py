# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 19:37:57 2021

@author: Amanda Veby DC. 20083000092, 2E.
"""

# import library
from os import system, __name__
from datetime import date, datetime


# format nama
def formatnama(nama):
    array_kata = nama.split(" ")
    list_kata = []
    panjang_kata = len(array_kata)

    i = 0
    while(i < panjang_kata):

        cek_kata = array_kata[i].istitle()
        if(cek_kata == False):
            konvers = array_kata[i].capitalize()
            list_kata.append(konvers)
            i += 1
        else:
            break

    hasil = " ".join(list_kata)
    return hasil


# panduan mengulang program lagi atu tidak
def inputpilihan(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Input Ulang Data [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [Y/T]\n")
            pass


# petunjuk input golongan
def inputgol(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan Golongan Anda   : "))
        except:
            print("\n\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan


# panduan input nama
def inputnama(pesan):
    while True:
        try:
            pesan = input(">> Masukkan Nama Anda       : ")
        except:
            print("\n\nWARNING!! : Masukkan Inputan Hanya Berupa alphabet\n")
        else:
            return pesan


# petunjuk input jenis kelamin
def input_jns_kelamin(pesan):
    while(pesan != "L" and pesan != "l" and pesan != "P" and pesan != "p"):
        ulang = input(">> Jenis Kelamin Anda [L/P] : ")

        if(ulang == "L" or ulang == "l" or ulang == "P" or ulang == "p"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [L/P]\n")
            pass


# panduan input status nikah
def input_sts_nikah(pesan):
    while(pesan != "M" and pesan != "m" and pesan != "L" and pesan != "l"):
        ulang = input(">> Status Pernikahan [M/L]  : ")

        if(ulang == "M" or ulang == "m" or ulang == "L" or ulang == "l"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [M/L]\n")
            pass


# petunjuk input status anak
def input_sts_anak(pesan):
    while(pesan != "S" and pesan != "s" and pesan != "B" and pesan != "b"):
        ulang = input(">> Status Anak Anda [S/B]   : ")

        if(ulang == "S" or ulang == "s" or ulang == "B" or ulang == "b"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [S/B]\n")
            pass


# fungsi konversi dari integer menjadi format mata uang
def uang(nilai):
    x = str(nilai)

    if(len(x) <= 3):
        return "Rp. " + x
    else:
        a = x[:-3]
        b = x[-3:]
        return uang(a) + "." + b


# program jalan
while True:

# inisiasi variabel
    gaji = [2500000, 4500000, 6500000, 0]
    persen_tunjangan = [0.01, 0.03, 0.05, 0]
    status_nikah = False
    status_anak = False
    tunjangan_anak = 0
    tunjangan_istri = 0

    _ = system('cls')
    print( )
    print("PENDATAAN SLIP GAJI KARYAWAN CV.LOGOS".center(50), "\n")

# input data nama karyawan
    nama = inputnama(">> Masukkan Nama Anda       : ")
    print("+---------------------------+\n")

# input data golongan karyawan
    gol = inputgol(">> Masukkan Golongan Anda   : ")

    while(gol < 0 or gol > 3):
        print("\nWARNING!! : Masukkan Inputan Harus >= 0 dan <= 4\n")
        gol = inputgol(">> Masukkan Jumlah Porsi : ")

        if(gol >= 0 and gol < 4):
            break
        else:
            pass
    print("+---------------------------+\n")

# input data Jenis Kelamin karyawan
    print("Note : L = Laki-laki dan P = Perempuan\n")
    ipt_jns_kelamin = input_jns_kelamin(">> Jenis Kelamin Anda [L/P] : ")
    print("+---------------------------+\n")
    if(ipt_jns_kelamin == "L" or ipt_jns_kelamin == "l"):
        jenis_kelamin = "Laki-laki"
    else:
        jenis_kelamin = "Perempuan"

# input data status pernikahan karyawan
    print("Note : M = Menikah dan L = Lajang\n")
    ipt_sts_nikah = input_sts_nikah(">> Status Pernikahan [M/L]  : ")
    print("+---------------------------+\n")
    if(ipt_sts_nikah == "M" or ipt_sts_nikah == "m"):
        sts = "Menikah"
        status_nikah = True
    else:
        sts = "Lajang"
        status_nikah = False

# input data status sudah memiliki anak atau belum
    print("Note : S = Sudah ada dan B = Belum ada\n")
    ipt_sts_anak = input_sts_anak(">> Status Anak Anda [S/B]   : ")
    print("+---------------------------+\n")
    if(ipt_sts_anak == "S" or ipt_sts_anak == "s"):
        status_anak = True
    else:
        status_anak = False

# pengkondisian if untuk menyeleksi biaya gaji dari masing-masing karyawan
    if((ipt_jns_kelamin == "L" or ipt_jns_kelamin == "l") and status_nikah == True):
        tunjangan_istri = persen_tunjangan[gol - 1] * gaji[gol - 1]

    if(status_nikah == True and status_anak == True):
        tunjangan_anak = 0.02 * gaji[gol - 1]

# menghitung gaji bruto
    gaji_bruto = gaji[gol - 1] + tunjangan_anak + tunjangan_istri

# variabel beban gaji karyawan
    biaya_jbtn = 0.005 * gaji_bruto
    iuran_pensiun = 15500
    iuran_organisasi = 3500

# hitung gaji netto
    gaji_netto = gaji_bruto - (iuran_organisasi + iuran_pensiun + biaya_jbtn)

# cetak output dari data slip gaji karyawan
    _ = system('cls')
    teks = "SLIP GAJI".center(50)
    teks1 = "KARYAWAN CV.LOGOS".center(50)
    print(teks)
    print(teks1)

    tanggal = date.today()
    print("\nTanggal :", tanggal.strftime("%d/%m/%Y"), "\n\n")
    print("<> Nama Karyawan     :", formatnama(nama))
    print("<> Golongan          :", gol)
    print("<> Jenis Kelamin     :", jenis_kelamin)
    print("<> Status Pernikahan :", sts)
    print("<> Gaji Pokok        :", uang(int(gaji[gol - 1])))
    print("<> Tunjangan Istri   :", uang(int(tunjangan_istri)))
    print("<> Tunjangan Anak    :", uang(int(tunjangan_anak)), "\n")
    print(">> Gaji Bruto        :", uang(int(gaji_bruto)))
    print("_"*50, "\n")
    print("<> Biaya Jabatan     :", uang(int(biaya_jbtn)))
    print("<> Iuran Pensiun     :", uang(int(iuran_pensiun)))
    print("<> Iuran Organisasi  :", uang(int(iuran_organisasi)), "\n")
    print(">> Gaji Netto        :", uang(int(gaji_netto)))

# pilihan agar user dapat mengulang input data karyawan
    ulang = inputpilihan("\n>> Input Ulang Data [Y/T] : ")

    if(ulang == "Y" or ulang == "y"):
        True
    else:
        break

# program berakhir
print()
print("PROGRAM TELAH BERAKHIR".center(50), "\n")
