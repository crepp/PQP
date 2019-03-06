import machine
import dht

t = dht.DHT22(machine.Pin(12)) 

def test():
	t.measure() 
	print(t.temperature())
	#print(t.humidity())

