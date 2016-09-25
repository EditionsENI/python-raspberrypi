#!/usr/bin/env python3
from lcd16x2 import LCD16x2
import os

class FIFOLCD(LCD16x2):
    def __init__(self):
        self.lcd = LCD16x2()
        self.fifo = '/dev/lcd16x2'
        self.creer_fifo()

    def creer_fifo(self):
        try:
            os.mkfifo(self.fifo)
            os.chmod(self.fifo, 0o777)
        except OSError:
            pass

    def lire_fifo(self):
        with open(self.fifo, 'r') as fifo:
            message = fifo.read().strip()
        if message.find('//') > 0:
            haut, bas = message.split('//')
            message = '{}\n\r{}'.format(haut, bas)
        print('Message: %s' % (message))
        self.lcd.clear()
        self.lcd.write_string(message)

    def boucle(self):
        try:
            while True:
                self.lire_fifo()
        except KeyboardInterrupt:
            os.remove(self.fifo)
            self.lcd.nettoyer()

if __name__ == '__main__':
    FIFOLCD().boucle()
