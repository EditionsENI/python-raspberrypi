#!/usr/bin/env python3
import curses

class MenuPi:
    def __init__(self, screen):
        self.ecran = screen
        self.nom_menu = self.__class__.__name__
        self.ecran.keypad(1)
        self.afficher_options()
        self.ecran.getch()

    def afficher_options(self):
        self.ecran.clear()
        self.ecran.border(0)
        self.ecran.addstr(2, 4, "Bienvenue dans {0} !".format(self.nom_menu))
        self.ecran.addstr(4, 4, "Choisissez une option entre [1] et [4]:")
        self.ecran.addstr(6, 6, "[1] - Demande vos prénom et nom et dit bonjour")
        self.ecran.addstr(7, 6, "[2] - Affiche la date du jour")
        self.ecran.addstr(8, 6, "[3] - Affiche l'espace disponible sur le Raspberry Pi")
        self.ecran.addstr(9, 6, "[4] - Affiche la RAM disponible du Raspberry Pi")
        self.ecran.addstr(10, 6, "[5] - Affiche le nom de l'utilisateur courant")
        self.ecran.addstr(12, 6, "[f] - Ferme le menu")
        self.ecran.refresh()

curses.wrapper(MenuPi)
