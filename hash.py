#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#LO MAU RIKOD? BIAR KEREN GITU?
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
import requests as r
from bs4 import BeautifulSoup as bs
import os
os.system('clear')
print (f'''{G1}
·▄▄▄▄  ▄▄▄ . ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄
██▪ ██ ▀▄.▀·▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  
▐█· ▐█▌▐▀▀▪▄██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪
██. ██ ▐█▄▄▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·
▀▀▀▀▀•  ▀▀▀ ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ 

{G1}[{Y1}>{G1}] {W0}Author D4RK5H4D0W5
{G1}[{Y1}>{G1}] {W0}Powered by https://hashtoolkit.com
''')
try:
	cari=input(f'{G1}[{Y1}?{G1}] {W0}Hash : ')
	if cari == '':
		print (f"{G1}[{R1}>{G1}] {W0}Don't be empty")
		exit()
	a=r.get('https://hashtoolkit.com/decrypt-hash/?hash='+cari,headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'}).text
	if 'No hashes found for' in a:
		print (f'{G1}[{R1}>{G1}] {W0}No hashes found for :',cari)
		exit()
	b=bs(a,'html.parser')
	c=b.find_all('div',class_='panel-heading')[1]
	d=b.find_all('td')[0]
	e=c.text.replace('Hashes for: ','')
	print (f'{G1}[{Y1}>{G1}] {W0}Hash type :',d.text)
	print (f'{G1}[{Y1}>{G1}] {W0}Result :',e)
except r.exceptions.ConnectionError:
	print ('Not connection')
