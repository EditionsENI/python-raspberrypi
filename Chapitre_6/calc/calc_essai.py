#!/usr/bin/env python3
import curses, string

class PiCalc:
    def __init__(self, screen):
        self.ecran = screen
        self.ecran_hauteur, self.ecran_largeur = self.ecran.getmaxyx()
        self.ecran.keypad(1)
        self.dessiner_calculatrice()

        self.pile = []
        self.nombre = ''
        self.historique = ''
        self.caracteres_calc = string.digits + '+/-*=.CcFf'
        self.lire_clavier()

    def dessiner_calculatrice(self):
        self.ecran.clear()

        self.calculatrice_hauteur = 20
        self.calculatrice_largeur = 60

        self.marge_ecran = 8

        self.calculatrice = curses.newwin(
            self.calculatrice_hauteur, 
            self.calculatrice_largeur, 
            (self.ecran_hauteur // 2) - (self.calculatrice_hauteur // 2),
            (self.ecran_largeur // 2) - (self.calculatrice_largeur // 2)
        )

        self.calculatrice.box()
        self.ecran.refresh()

        boutons = ('789/' '456*' '123-' '0.=+')
        longueur_boutons = len(boutons)

        lignes_boutons = 4
        colonnes_boutons = lignes_boutons // longueur_boutons

        instructions = 'Nettoyer (C ou c) - Fermer (F ou f)'
        separateur = '-'

        self.calculatrice.addstr(self.marge_ecran - 4, 1, separateur * (self.calculatrice_largeur - 2))
        self.calculatrice.addstr(self.marge_ecran - 2, (self.calculatrice_largeur - 5) - len(instructions), instructions)
        self.calculatrice.addstr(self.marge_ecran, 1, separateur * (self.calculatrice_largeur - 2))

        marge_verticale = 5
        marge_horizontale = 10

        pave_hauteur = self.calculatrice_hauteur - marge_ecran - marge_verticale * 2
        pave_largeur = self.calculatrice_largeur - marge_horizontale * 2

        for ligne in 

        self.calculatrice.refresh()

    def afficher_resultat(self, nombre):
        self.calculatrice.addstr(2, (self.calculatrice_largeur - 4) - len(nombre), nombre)
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

curses.wrapper(PiCalc)
