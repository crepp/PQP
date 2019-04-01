# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine
from ds3231_port import DS3231

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
ds = DS3231(i2c)

def test():
	print(ds.get_time())

def save_datetime(an, mo, jo, h, mn):
	#print(h, mn)
	rtc = machine.RTC()
	rtc.datetime((an, mo, jo, 6, h, mn, 0, 0)) # 6:dimanche
	print(rtc.datetime())
	ds.save_time()	# ecriture et sauvegarde de l'heure

def get_next():
	# quantité de minutes jusqu'a la prochaine heure
	try:
		t = ds.get_time()
	except OSError:
		t[4] = 0
	mn = 60 - t[4] 
	if mn <= 10 :
		mn += 60
	return round(mn * 1.1) # *1.2 à cause d'une grande dérive du RTC de l'ESP...

def get_datehour():
	try:
		t = ds.get_time()
		dateheure = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2]) + " " + str(t[3]) + ":" + str(t[4])
		return dateheure
	except OSError:
		return "-1"

