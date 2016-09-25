#!/usr/bin/env python3
import curses

screen = curses.initscr()
curses.cbreak()
screen.keypad(1)
screen.addstr(
    5,
    15,
    "Hello world with curses!"
)
screen.refresh()
key = screen.getkey()
curses.endwin()

if key.strip() == '':
    key = 'Enter/Space'

print("Touche appuyée: {0}".format(key))
