#!/usr/bin/python2
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
import os,time

def logo():
	os.system('clear')
	print ('''%s
·▄▄▄▄  ▄▄▄ . ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄
██▪ ██ ▀▄.▀·▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  
▐█· ▐█▌▐▀▀▪▄██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪
██. ██ ▐█▄▄▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·
▀▀▀▀▀•  ▀▀▀ ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ 

[%s>%s] %sAuthor D4RK5H4D0W5
%s[%s>%s] %sPowered by https://hashtoolkit.com
'''%(G1,Y1,G1,W0,G1,Y1,G1,W0))

def single():
	logo()
	try:
		cari=raw_input('\033[1;37m[\033[1;32m?\033[1;37m]\033[0;37m Hash : ')
		if cari == '':
			print ("[!] Don't be empty")
			exit()
		a=r.get('https://hashtoolkit.com/decrypt-hash/?hash='+cari,headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'}).text
		print
		if 'No hashes found for' in a:
			print ('%s[ %sNo found %s] %s'%(W0,R0,W0,cari))
			exit()
		b=bs(a,'html.parser')
		c=b.find_all('div',class_='panel-heading')[1]
		d=b.find_all('td')[0]
		e=c.text.replace('Hashes for: ','')
		print ('%s[ %sType. %s] %s'%(W0,G0,W0,d.text))
		print ('%s[ %sFound %s] %s'%(W0,G0,W0,e))
	except r.exceptions.ConnectionError:
		print ('Not connection')

def mass():
	logo()
	try:
		file=open(raw_input('\033[1;37m[\033[1;32m?\033[1;37m] \033[0;37mFile : ')).read().splitlines()
		if file == '':
			print ("[!] Don't be empty")
			exit()
		for hash in file:
			a=r.get('https://hashtoolkit.com/decrypt-hash/?hash='+hash,headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'}).text
			print ('%s[ %sStart %s] %s'%(W0,Y0,W0,hash))
			if 'No hashes found for' in a:
				print ('%s[ %sNo found %s] %s'%(W0,R0,W0,hash))
			else:
				b=bs(a,'html.parser')
				c=b.find_all('div',class_='panel-heading')[1]
				d=b.find_all('td')[0]
				e=c.text.replace('Hashes for: ','')
				print ('%s[ %sType. %s] %s'%(W0,G0,W0,d.text))
				print ('%s[ %sFound %s] %s'%(W0,G0,W0,e))
			print ('-'*50)
	except IOError:
		print ('File not found')
	except r.exceptions.ConnectionError:
		print ('Not connection')

def main():
	logo()
	print ('''%s{%s01%s} %sSingle
%s{%s02%s} %sMass
%s{%s00%s} %sExit
'''%(W1,G1,W1,W0,W1,G1,W1,W0,W1,R1,W1,R0))
	chc=raw_input('\033[1;32m[\033[1;33m?\033[1;32m] \033[0;37m@ImamSy > ')
	if chc == '':
		print
		print '%s[%s!%s] %sDont be empty'%(W1,R1,W1,W0)
		time.sleep(0.8)
		main()
	elif chc == '1' or chc == '01':
		single()
	elif chc == '2' or chc == '02':
		mass()
	elif chc == '0' or chc == '00':
		exit('Bye')
	else:
		exit('Bye')
		
if __name__=='__main__':
	#os.system('git pull')
	#time.sleep(1)
	main()