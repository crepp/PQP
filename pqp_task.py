# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine, time, sys
import pqp_relais as r
import pqp_horloge as h
import pqp_thermometre as t
import pqp_converan as c
import pqp_config as co
time.sleep_ms(3000)
import pqp_oled as p

r.off()

def start():
	if h.get_hour() == 9:
		pump()
	#
	#affichetemperature()
	affichetemphygro()
	affichebatteries()
	#datalog()

def test():
	# clignotement relais
	for i in range(0,3):
		time.sleep_ms(250)
		r.on()
		time.sleep_ms(250)
		r.off()

def pump():
	# irrigation
	r.on()
	time.sleep_ms(co.pumptime)
	r.off()

def datalog():
	f = open("pqp_datalog.csv", "a")
	data = h.get_datehour() + "; "
	data += t.get_temp() + "; "
	data += str(machine.reset_cause()) + "; "
	data += str(c.get_battery()) + "; " + "\n"
	f.write(data)
	f.close()

def affichetemperature():
	temperature=t.get_temp()
	print(temperature)
	p.affiche(str(temperature))
	
def affichebatteries():
	tension=c.get_battery()
	print(tension)
	p.surafficheXY(str(tension),0,25)
	
def affichetemphygro():
	temperature=t.get_temp()
	hygro = c.get_a0()
	print(temperature, hygro)
	p.affiche(str(temperature) +"  "+ str(hygro))

