import machine
import bh1750

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
lum = bh1750.BH1750(i2c)

def test():
	print(lum.lecture_lumiere(bh1750.MODE_CONTINU_HAUTE_RESOLUTION))

