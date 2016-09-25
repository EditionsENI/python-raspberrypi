#!/usr/bin/env python3
import curses

class HelloWorldCurses:
    def __init__(self, screen):
        self.ecran = screen
        self.ecran_hauteur, self.ecran_largeur = self.ecran.getmaxyx()
        self.ecran.keypad(1)
        self.bonjour = "Hello world avec curses!"
        self.dire_bonjour()
        self.ecran.getch()

    def dire_bonjour(self):
        self.ecran.addstr(
            int(self.ecran_hauteur / 2),
            int(self.ecran_largeur / 2) - int(len(self.bonjour) / 2),
            self.bonjour
        )
        self.ecran.refresh()

curses.wrapper(HelloWorldCurses)
