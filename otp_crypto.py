#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import binascii
import os
import random
sifre_dir = 'sifreler'

mesaj="Kedi yemeği yedi"
parola="a"


def sifre_yarat(mesaj,parola):
    mesaj_uzunlugu = len(mesaj)
    parola_uzunlugu = len(parola)
    sifreli_mesaj=""
    for harf_sayisi in range(0,mesaj_uzunlugu):
        mesaj_harf = mesaj[harf_sayisi]
        parola_harf = parola[harf_sayisi%parola_uzunlugu]
        yeni_harf = chr( (ord(mesaj_harf) + ord(parola_harf))%65535)
        sifreli_mesaj = sifreli_mesaj+yeni_harf
    return sifreli_mesaj

def sifre_coz(mesaj,parola):
    mesaj_uzunlugu = len(mesaj)
    parola_uzunlugu = len(parola)

    cozulmus_mesaj=""
    for harf_sayisi in range(0,mesaj_uzunlugu):
        mesaj_harf = mesaj[harf_sayisi]
        parola_harf = parola[harf_sayisi%parola_uzunlugu]
        yeni_harf = chr( (ord(mesaj_harf) - ord(parola_harf))%65535)
        cozulmus_mesaj = cozulmus_mesaj+yeni_harf
    return cozulmus_mesaj

import sys

def print_usage():
    print("use: %s [-d] message"%(sys.argv[0]))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
    elif(sys.argv[1] == "-d"):
        if len(sys.argv) < 3:
            print_usage()
        else:
            #sifre cozuyoruz
            anahtar_dosya_ve_mesaj = sys.argv[2]
            #print(anahtar_dosya_ve_mesaj)
            anahtar_dosya=anahtar_dosya_ve_mesaj.split('_')[0]
            hex_mesaj=anahtar_dosya_ve_mesaj.split('_')[1]
            #print("hex_mesaj:"+hex_mesaj)
            mesaj = binascii.unhexlify(hex_mesaj).decode('utf-8')
            f=open(sifre_dir+"/"+anahtar_dosya)
            anahtar=str(f.read())
            #print(anahtar)
            f.close()
##            print("mesaj: "+mesaj)
##            print("anahtar: "+anahtar)
            cozulmus_mesaj = sifre_coz(mesaj,anahtar)
            #cozulmus_mesaj = sifre_coz(str(binascii.a2b_base64(mesaj)),parola)
            print(cozulmus_mesaj)
    else:
        #yalnizca sifreli mesaj yaratiyoruz
        mesaj = sys.argv[1]
        #print("mesaj: "+mesaj)
        #tek kullanimlik serit (One Time Pad) dosyasini secelim
        dosyalar=os.listdir(sifre_dir)
        anahtar_dosya=random.choice(dosyalar)
        f=open(sifre_dir+"/"+anahtar_dosya)
        anahtar=f.read()
        f.close()
        sifreli_mesaj = sifre_yarat(mesaj,anahtar)
        #print(binascii.b2a_base64(bytes(sifreli_mesaj,'utf-8'))),
        sifreli_mesaj_hex = binascii.hexlify(sifreli_mesaj.encode('utf-8'))
        print(anahtar_dosya+"_"+sifreli_mesaj_hex.decode())
        #print(str(binascii.hexlify(sifreli_mesaj.encode('utf-8'))))



