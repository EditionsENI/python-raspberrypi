#!/usr/bin/env python3
import curses

screen = curses.initscr()
curses.cbreak()
screen.keypad(1)
screen.addch(
    5,
    15,
    "H"
)
screen.refresh()
screen.getch()
curses.endwin()
