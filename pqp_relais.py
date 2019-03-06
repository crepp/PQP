# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine

rel = machine.Pin(14, machine.Pin.OUT)

def test():
	if rel.value() == True :
		rel.off()
	else:
		rel.on()

def on():
	rel.on()

def off():
	rel.off()




