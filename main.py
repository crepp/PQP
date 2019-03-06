# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine, time
import pqp_task

wifitime = 3*60*1000 # 3mn en ms
sleeptime = 60*1000 # 1mn

# 2 Modes de démarrage de l'ESP8266
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
	# 1. DEEPSLEEP_RESET
	wifitime = 10*1000 # 10s ! Ne dois pas etre plus court que la durée de la tache courante
else:
	# 2. HARD_RESET ou SOFT_RESET ou ...
	wifitime = 3*60*1000 # Attention ! Jamais moins de 3mn (en ms) !

# Fixe la durée de wifi actif jusqu'a la mise en veille
tim = machine.Timer(-1)
tim.init(period=wifitime, mode=machine.Timer.ONE_SHOT, callback=lambda t:sleeping())

# Lancement de la tache courante
pqp_task.start() 

# Relier le GPIO16 (l'alarme RTC) avec la broche Reset (RST) de l'ESP8266
def sleeping():
	print("-- deepsleep()\n")
	time.sleep_ms(1000)
	#
	rtc = machine.RTC() 
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP) # On configure RTC.ALARM0 pour re-démarrer
	rtc.alarm(rtc.ALARM0, sleeptime) #  Après sleeptime RTC.ALARM0 redémarrera la machine !
	machine.deepsleep() # Mise en sommeil profond

