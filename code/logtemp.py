#!/usr/bin/python
import os
import time

import sqlite3 as mydb
import sys

con = None




""" Log Current Time, Temperature in Celsius and Fahrenheit
    Returns a list [time, tempC, tempF] """

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-00000697426f/w1_slave")
	tempfile_text = tempfile.read()
	currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	try:
		con = mydb.connect('temperature.db')
		cur = con.cursor()    
		cur.execute("INSERT INTO TempData VALUES(?,?,?)",(currentTime,tempC,tempF))
		msg='Today: ',currentTime,'Temp C:',tempC,' TempF: ',tempF             
	except mydb.Error, e:
		print "Erro ao inserir na tabela";
  		sys.exit(1)
    
	finally:
    
			if con:
  				con.commit()
				con.close()

	return [msg]
print readTemp()
