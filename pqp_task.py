# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine, time
import pqp_relais as r
import pqp_horloge as h
import pqp_thermometre as t
import sys

r.off()

def start():
	test()
	datalog()


def test():
	# clignotement relais
	for i in range(0,3):
		time.sleep_ms(250)
		r.on()
		time.sleep_ms(250)
		r.off()


def datalog():
	f = open("pqp_datalog.txt", "a")
	data = h.get_datehour() + "; "
	data += t.get_temp() + "; " + "\n"
	f.write(data)
	f.close()


