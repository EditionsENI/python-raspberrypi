#!/usr/bin/env python3
import curses

def main(screen):
    screen.keypad(1)
    screen.addstr(
        5,
        10,
        "Hello world avec curses!"
    )
    screen.refresh()
    screen.getch()

curses.wrapper(main)
