#!/usr/bin/env python3
from lcd16x2 import LCD16x2
import time

def main():
    lcd = LCD16x2()
    lcd.clear()
    lcd.write_string('TestLCD123456')
    time.sleep(5)
    lcd.close(clear=True)

if __name__ == '__main__':
    main()
