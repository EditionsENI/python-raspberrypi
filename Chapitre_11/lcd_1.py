#!/usr/bin/env python3
from lcd16x2 import LCD16x2
import time

class PiLCD:
    def __init__(self, liste):
        self.liste = liste
        self.lcd = LCD16x2()
        self.boucle()

    def lire_messages(self):
        for element in self.liste:
            self.lcd.clear()
            haut, bas, pause = element
            texte = '{}\n\r{}'.format(haut, bas)
            self.lcd.write_string(texte)
            time.sleep(pause)

    def boucle(self):
        try:
            while True:
                self.lire_messages()
        except KeyboardInterrupt:
            self.lcd.nettoyer()

if __name__ == '__main__':
    PiLCD([
    ( "Le Raspberry Pi",
      "C'est bien ...",
      3 ),
    ( "Avec un LCD",
      "C'est mieux !",
      5 )
    ])
