# Pot qui pense - CREPP 2019
# GPL V3.0
# www.crepp.org - yvoz.lg@gmail.com

# Durée du Wifi actif lors d'une mise sous tension (hard reset)
# wifitime_hardreset = 3mn minimum 
wifitime_hardreset = 3*60*1000

# Durée du Wifi actif apres un reveil par l'alarme (deepsleep reset)
# Cette durée doit être supérieure à la durée totale de la tâche courante (l'arrosage)
# wifitime = 15 secondes
wifitime = 15*1000 

# Durée de la mise en veille - 3 options possibles :
# -1 : pas de mise en veille : mode debug
#  0 : sleeptime jusqu'à la prochaine heure fixe, c'est le fonctionnement normal du PQP
#  30*60*1000 : 30mn de mise en veille : mode test
sleeptime = 0 # 1*60*1000 # réveil toutes les 1mn
 
# Durée de la mise en action de la pompe - tenir compte du temps d'amorçage / la hauteur de pompage
# pumptime = 5 secondes c'est pas mal
pumptime = 5*1000







