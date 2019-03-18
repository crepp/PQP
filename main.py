# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

import machine, time
import pqp_task
import pqp_config as co
import pqp_horloge as h

wifitime = co.wifitime_hardreset # 3mn en ms

# 2 Modes de démarrage de l'ESP8266
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
	# 1. DEEPSLEEP_RESET
	wifitime = co.wifitime # Ne dois pas etre plus court que la durée de la tache courante !
	if wifitime == 0: 
		wifitime = 15*1000 # 15s
else:
	# 2. HARD_RESET ou SOFT_RESET ou ...
	wifitime = co.wifitime_hardreset
	if wifitime < 3*60*1000: 
		wifitime = 3*60*1000 # Attention ! Jamais moins de 3mn (en ms) !

# Fixe la durée de wifi actif jusqu'a la mise en veille
tim = machine.Timer(-1)
tim.init(period=wifitime, mode=machine.Timer.ONE_SHOT, callback=lambda t:sleeping())

# Lancement de la tache courante
pqp_task.start() 

# Relier le GPIO16 (l'alarme RTC) avec la broche Reset (RST) de l'ESP8266
def sleeping():
	sleeptime = co.sleeptime
	if sleeptime == -1: 
		print("-- pas de mise en veille\n")
		return # Pas de mise en veille
	if sleeptime == 0:
		sleeptime = h.get_next()*60*1000
		if sleeptime == 0:
			sleeptime = 50*60*1000 #  Si l'horloge ne répond pas : 50mn par défaut
	#
	print("-- deepsleep()", sleeptime, "ms\n")
	time.sleep_ms(1000) # 1 seconde : le temps d'afficher avant la mise en sommeil
	#
	rtc = machine.RTC() 
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP) # On configure RTC.ALARM0 pour re-démarrer
	rtc.alarm(rtc.ALARM0, sleeptime) #  Après sleeptime RTC.ALARM0 redémarrera la machine !
	machine.deepsleep() # Mise en sommeil profond

