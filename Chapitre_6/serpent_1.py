#!/usr/bin/env python3
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

class PiSerpent:
    def __init__(self, screen):
        self.ecran = screen

        self.serpent = [[1, 10], [1, 9], [1, 8], [1, 7]]
        self.nourriture = [5, 20]

        self.score = 0
        self.tete = 'Ö'
        self.corps = 'o'
        self.velocite = 100

        self.directions = (KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN)
        self.touche = KEY_RIGHT
        self.fermer = (ord('f'), ord('F'))

        curses.curs_set(0)

        self.dessiner_fenetre()
        self.boucle_principale()

    def dessiner_fenetre(self):
        self.ecran_hauteur, self.ecran_largeur = self.ecran.getmaxyx()
        self.fenetre_jeu_hauteur = 30
        self.fenetre_jeu_largeur = 80

        self.fenetre_serpent = curses.newwin(
            self.fenetre_jeu_hauteur,
            self.fenetre_jeu_largeur,
            self.ecran_hauteur // 2 - self.fenetre_jeu_hauteur // 2,
            self.ecran_largeur // 2 - self.fenetre_jeu_largeur // 2
        )

        self.fenetre_serpent.box()
        self.fenetre_serpent.border('|', '|', '-', '-', '+', '+', '+', '+')
        self.ecran.refresh()

        if curses.has_colors():
            curses.init_pair(1, curses.COLOR_RED,   curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_CYAN,  curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

        self.fenetre_serpent.keypad(1)

        if curses.has_colors():
            self.fenetre_serpent.attrset(curses.color_pair(1))
        self.fenetre_serpent.addch(self.nourriture[0], self.nourriture[1], '*')

    def afficher_score(self, score):
        self.ecran.clear()
        fin = 'Votre score: {s} point(s)'.format(s=score)
        self.ecran.addstr(
            self.ecran_hauteur // 2,
            self.ecran_largeur // 2 - len(fin) // 2,
            fin
        )
        self.ecran.refresh()
        self.ecran.getch()

    def boucle_principale(self):
        while True:
            if curses.has_colors():
                self.fenetre_serpent.attrset(curses.color_pair(3))
            banniere = '[ {t} - Score : {s} ]'.format(
                t=self.__class__.__name__,
                s=self.score
            )
            self.fenetre_serpent.addstr(0, 2, banniere)
            self.fenetre_serpent.timeout(self.velocite)

            touche = self.fenetre_serpent.getch()
            if touche in self.directions + self.fermer:
                self.touche = touche

            if self.touche in self.fermer:
                curses.endwin()
                self.afficher_score(self.score)
                break

            serpent_x = self.serpent[0][1]
            serpent_y = self.serpent[0][0]
            if self.touche == KEY_RIGHT: serpent_x += 1
            if self.touche == KEY_DOWN:  serpent_y += 1
            if self.touche == KEY_LEFT:  serpent_x -= 1
            if self.touche == KEY_UP:    serpent_y -= 1
            self.serpent.insert(0, [serpent_y, serpent_x])

            if serpent_y == 0: self.serpent[0][0] = self.fenetre_jeu_hauteur - 2
            if serpent_y == self.fenetre_jeu_hauteur - 1: self.serpent[0][0] = 1
            if serpent_x == 0: self.serpent[0][1] = self.fenetre_jeu_largeur - 2
            if serpent_x == self.fenetre_jeu_largeur - 1: self.serpent[0][1] = 1

            if self.serpent[0] in self.serpent[1:]:
                curses.endwin()
                self.afficher_score(self.score)
                break

            if self.serpent[0] == self.nourriture:
                self.score += 1
                self.velocite -= 2
                while True:
                    self.nourriture = [
                        randint(1, self.fenetre_jeu_hauteur - 2),
                        randint(1, self.fenetre_jeu_largeur - 2)
                    ]
                    if self.nourriture not in self.serpent:
                        break
                if curses.has_colors():
                    self.fenetre_serpent.attrset(curses.color_pair(1))
                self.fenetre_serpent.addch(self.nourriture[0], self.nourriture[1], '*')
            else:
                queue = self.serpent.pop()
                self.fenetre_serpent.addch(queue[0], queue[1], ' ')

            if curses.has_colors():
                self.fenetre_serpent.attrset(curses.color_pair(2))
            self.fenetre_serpent.addch(self.serpent[0][0], self.serpent[0][1], self.tete)

            if curses.has_colors():
                self.fenetre_serpent.attrset(curses.color_pair(4))
            for corps in self.serpent[1:]:
                self.fenetre_serpent.addch(corps[0], corps[1], self.corps)

if __name__ == '__main__':
    curses.wrapper(PiSerpent)
