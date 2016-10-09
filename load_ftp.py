#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import getpass
from ftplib import FTP


def downloadFile(connect, chemin):
	files= []
	connect.retrlines('LIST '+chemin,files.append)

	for i in files:
		if i.split()[8]!="." and i.split()[8]!="..":
			print "Download of "+i.split()[8]
			try:
				if i[0]!='d':
					connect.retrbinary('RETR '+chemin+'/'+i.split()[8], open("./data/"+chemin+'/'+i.split()[8], 'wb').write)
				else : 
					if not os.path.exists("./data/"+chemin+'/'+i.split()[8]):
						os.makedirs("./data/"+chemin+'/'+i.split()[8])
					downloadFile(connect,chemin+'/'+i.split()[8])
			except:
				print "Error with the file "+i.split()[8]
	

hote=raw_input("Enter the host : ")
ident=raw_input("Enter the login : ")
mdp=getpass.getpass("Enter the password : ")

if not os.path.exists("data"):
    os.makedirs("data")

try:
	connect = FTP(hote, ident, mdp) 
	downloadFile(connect,"./")
	print "\nDownload finished\nDisconnection from the server"
	connect.quit() 
except:
	print "Error in the informations"
