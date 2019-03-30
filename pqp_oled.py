# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - patrick.pastor56@gmail.com

# intialisation du bus i2c
# scl=Pin5=GPIO5=d1 sda=Pin4=GPIO4=d2
#del  sys.modules['pqp_oled']

from machine import I2C, Pin
i2c= I2C(scl=Pin(5), sda=Pin(4))

import ssd1306

# adresse Oled 0x3c ?
print(i2c.scan())

#initialisation de l'茅cran 128x64 脿 0x3c
# oled=ssd1306.SSD1306_I2C(128,64, i2c, 0x3c)
oled=ssd1306.SSD1306_I2C(128,32, i2c, 0x3c)


# timer
import time
# time.sleep_ms(5000)

def affiche(Quoi):
  oled.fill(0)
  oled.text(Quoi, 0, 10)
  oled.show()
  
def afficheXY(Quoi,x,y):
  oled.fill(0)	
  oled.text(Quoi, int(x), int(y))
  oled.show()
  
def surafficheXY(Quoi,x,y):
  #oled.fill(0)
  oled.text(Quoi, int(x), int(y))
  oled.show()
  
def efface():
  oled.fill(0)
  oled.show()
  
def  inverse(p):
  oled.invert(p)
  
def test():
  oled.fill(0)
  oled.text("Bonjour", 0, 0)
  oled.text("il fait beau", 0, 20)
  oled.show()
 
def machine():  
 efface()
 import machine, sys
 oled.text('version ' + sys.version, 0,10)
 oled.text('CPU: ' + str(machine.freq()/1000000) + 'MHz', 0,20)
 oled.show() 
 time.sleep_ms(2500)
 # inversion fond blanc=1 / fond noir=0 
 oled.invert(1) 
 time.sleep_ms(2000)
 # 茅cran blanc=1 / noir=0 
 oled.fill(0) 
 oled.show() 
 





