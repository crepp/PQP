# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine
from ads1x15 import ADS1115

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
can = ADS1115(i2c=i2c, address=72, gain=0)

def test():
	print(can.read(rate=0, channel1=0))


