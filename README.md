# PQP - Pot qui pense - Code Micropython - ESP8266

http://www.crepp.org/projets/pot-qui-pense/

## Librairies utilisées

- Convertisseur A/N - ads1115  
https://github.com/robert-hh/ads1x15

- Horloge - ds3231  
https://github.com/peterhinch/micropython-samples/tree/master/DS3231

- Capteur de luminosite - bh1750  
https://github.com/itechnofrance/micropython/tree/master/librairies/bh1750

- Ecran oled - ssd1306  
https://github.com/micropython/micropython/tree/master/drivers/display


## Brochage bus et capteurs

| Libellé             | GPIO Micropython  | ESP8266 | 
|---------------------|-------------------|---------|
| I2C - sda           | Pin(4)            | D2      |
| I2C - scl           | Pin(5)            | D1      |
| Thermomètre - DHT22 | Pin(12)           | D6      |
| Relais pompe        | Pin(14)           | D5      |
| Réveil alarme       | Pin(16)           | D0      |
| Bouton d'arrosage   | Pin(9)            | SD2     |

| Libellé             | Convertisseur A/N |
|---------------------|-------------------|
| Hygromètre terre    | A0                |
| Voltmètre batteries | A1                |


## Principe du cycle de réveil

![chronogramme](img/chronogramme.png)

