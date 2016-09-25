#!/usr/bin/env python3
import curses, string

class PiCalc:
    def __init__(self, screen):
        self.ecran = screen
        self.ecran.keypad(1)
        self.dessiner_calculatrice()

        self.pile = []
        self.nombre = ''
        self.historique = ''
        self.caracteres_calc = string.digits + '+/-*=.CcFf'
        self.lire_clavier()

    def dessiner_calculatrice(self):
        self.ecran.clear()

        self.ecran_hauteur, self.ecran_largeur = self.ecran.getmaxyx()

        self.calculatrice_hauteur = 30
        self.calculatrice_largeur = 60

        self.calculatrice = curses.newwin(
            self.calculatrice_hauteur,
            self.calculatrice_largeur,
            (self.ecran_hauteur // 2) - (self.calculatrice_hauteur // 2),
            (self.ecran_largeur // 2) - (self.calculatrice_largeur // 2)
        )

        self.calculatrice.box()
        self.ecran.refresh()

        ligne = '-' * self.calculatrice_largeur
        caractere_pos = int((self.calculatrice_largeur / 4) // 1.25)
        instructions = 'Nettoyer (C ou c) - Fermer (F ou f)'

        self.calculatrice.addstr(4, 0, ligne)
        self.calculatrice.addstr(6, (self.calculatrice_largeur - 5) - len(instructions), instructions)
        self.calculatrice.addstr(8, 0, ligne)

        self.calculatrice.addstr(12, caractere_pos,     '7')
        self.calculatrice.addstr(12, caractere_pos * 2, '8')
        self.calculatrice.addstr(12, caractere_pos * 3, '9')
        self.calculatrice.addstr(12, caractere_pos * 4, '/')

        self.calculatrice.addstr(16, caractere_pos,     '4')
        self.calculatrice.addstr(16, caractere_pos * 2, '5')
        self.calculatrice.addstr(16, caractere_pos * 3, '6')
        self.calculatrice.addstr(16, caractere_pos * 4, '*')

        self.calculatrice.addstr(20, caractere_pos,     '1')
        self.calculatrice.addstr(20, caractere_pos * 2, '2')
        self.calculatrice.addstr(20, caractere_pos * 3, '3')
        self.calculatrice.addstr(20, caractere_pos * 4, '-')

        self.calculatrice.addstr(24, caractere_pos,     '0')
        self.calculatrice.addstr(24, caractere_pos * 2, '.')
        self.calculatrice.addstr(24, caractere_pos * 3, '=')
        self.calculatrice.addstr(24, caractere_pos * 4, '+')

        self.calculatrice.refresh()

    def afficher_resultat(self, key):
        self.calculatrice.addstr(2, (self.calculatrice_largeur - 4) - len(key), key)
        self.calculatrice.refresh()

    def lire_clavier(self):
        while True:
            touche = self.ecran.getkey().strip()
            if touche == '':
                touche = '='
            if touche in self.caracteres_calc:
                if touche in 'Ff':
                    break
                if touche in 'Cc':
                    self.nombre = ''
                    self.historique = ''
                    self.dessiner_calculatrice()
                if touche in string.digits:
                    if len(self.historique) > 0 and self.historique[-1] == '=':
                        self.dessiner_calculatrice()
                        self.historique = ''
                    self.nombre = self.nombre + touche
                    self.historique = self.historique + touche
                    self.afficher_resultat(self.historique)
                if touche == '.':
                    if len(self.historique) == 0 or '.' in self.nombre:
                        continue
                    if len(self.historique) > 0 and self.historique[-1] == '=':
                        self.dessiner_calculatrice()
                        self.historique = ''
                    self.nombre = self.nombre + touche
                    self.historique = self.historique + touche
                    self.afficher_resultat(self.historique)
                if touche in '+/-*':
                    if len(self.historique) == 0:
                        continue
                    if len(self.historique) > 0 and self.historique[-1] in '+/-*=.':
                        continue
                    self.pile.append(self.nombre)
                    self.pile.append(touche)
                    self.nombre = ''
                    self.historique = self.historique + touche
                    self.afficher_resultat(self.historique)
                if touche == '=':
                    if len(self.pile) == 0:
                        continue
                    if len(self.historique) > 0 and self.historique[-1] in '+/-*.':
                        continue
                    self.pile.append(self.nombre)
                    resultat = eval(''.join(self.pile))
                    self.dessiner_calculatrice()
                    self.afficher_resultat(str(resultat))
                    self.pile = []
                    self.nombre = ''
                    self.historique = touche


if __name__ == '__main__':
    curses.wrapper(PiCalc)
