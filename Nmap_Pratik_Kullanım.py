#!usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt install tcptraceroute")
os.system("apt install traceroute")
os.system("apt install figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet MAKRO")



print("""Nmap pratik programına hoş geldiniz (nmap yazısından sonrakiler örnektir siz oraya hedef ip veya domain girin)


""")



print("""
1)Kısa Tarama
2)Port tarama
3)Agresif tarama
4)Hızlı Tarama
5)Gizli Tarama(mac adres)
6)Gizli Tarama(İP adres)
7)Hedef İşletim sistemini Öğrenme
8)Hedef Servis Sürümleni Öğrenme
9)Firewall Algılama
10)Firewall Atlatma

""")


secim = raw_input("Lütfen Seçim Yapınız: ")


if(secim=="1"):
	print("""nmap 12.23.56.87""")
elif(secim=="2"):
	print("""nmap  örnek.com -sS -sV""")
elif(secim=="3"):
	print("nmap örnek.com -A")
elif(secim=="4"):
	print("""nmap örnek.com -F """)
elif(secim=="5"):
	print("""nmap örnek.com --spoof-mac 12:34:56:78:89 """)
elif(secim=="6"):
	print("""nmap örnek.com -D 123.12.456.78 """)
elif(secim=="7"):
	print("nmap örnek.com -O")
elif(secim=="8"):
	print("nmap örnek.com -sV")
elif(secim=="9"):
	print("""nmap örnek.com -sA """)
elif(secim=="10"):
	print("""nmap örnek.com -f (-f parametresini nekadar çok yazarsanız okadar atlatır ama bekletir:D)""")



else:
	print("Hatlı Seçim Yeniden Dene")

tek = raw_input("Programdan Çıkılsın mı? y/n: ")

if(tek=="y"):
	print("Güle Güle")

elif(tek=="n"):
	os.system("python Nmap_Pratik_Kullanım.py")
else:
	print("Yanlış Seçim Program Kapatılıyor")
