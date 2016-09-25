#!/usr/bin/env python3
import curses, string, math

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
        self.ecran.getch()

        #self.lire_clavier()

    def dessiner_calculatrice(self):
        self.ecran.clear()

        # Screen
        screen_height, screen_width = self.ecran.getmaxyx()
        screen_vertical_centre = screen_height // 2
        screen_horizontal_centre = screen_width // 2

        # Keypad buttons
        buttons = ('789/' '456*' '123-' '0.=+')
        num_buttons = len(buttons)

        # Keypad dimensions
        keypad_num_columns = 4
        keypad_num_rows = int(math.ceil(num_buttons / keypad_num_columns))

        # Calculator dimensions
        calculator_width = 60
        calculator_height = 40
        calculator_display_height = 4

        # Layout preferences
        vertical_margin = 5
        horizontal_margin = 10

        # Window co-ordinates
        top = screen_vertical_centre - calculator_height // 2
        left = screen_horizontal_centre - calculator_width // 2

        # Window painting
        my_window = curses.newwin(calculator_height, calculator_width,
                                  top, left)
        my_window.box()
        self.ecran.refresh()
        my_window.border(0)
        my_window.refresh()

        # Keypad dimensions
        keypad_height = (calculator_height - calculator_display_height
                         - vertical_margin * 2)
        keypad_width = calculator_width - horizontal_margin * 2

        # Vertical spacing
        vertical_space = keypad_height - keypad_num_rows
        vertical_spacing = int(math.ceil(vertical_space / (keypad_num_rows - 1)))

        # Horizontal spacing
        horizontal_space = keypad_width - keypad_num_columns
        horizontal_spacing = int(math.ceil(horizontal_space
                                           / (keypad_num_columns - 1)))

        # Keypad offsets
        keypad_y_start = top + calculator_display_height + vertical_margin
        keypad_x_start = left + horizontal_margin

        # Display separator
        separator_char = '-'
        self.ecran.addstr(top + calculator_display_height,
                      left + 1,
                      separator_char * (calculator_width - 2))

        # Display keypad buttons
        for row in range(keypad_num_rows):
            y = keypad_y_start + vertical_spacing * row
            for column in range(keypad_num_columns):
                button = buttons[keypad_num_columns * row + column]
                x = keypad_x_start + horizontal_spacing * column
                self.ecran.addstr(y, x, button)

        #self.calculatrice_hauteur = 20
        #self.calculatrice_largeur = 60

        #self.calculatrice = curses.newwin(
        #    self.calculatrice_hauteur, 
        #    self.calculatrice_largeur, 
        #    (self.ecran_hauteur // 2) - (self.calculatrice_hauteur // 2),
        #    (self.ecran_largeur // 2) - (self.calculatrice_largeur // 2)
        #)

        #self.calculatrice.box()
        #self.ecran.refresh()

        #ligne = '-' * self.calculatrice_largeur
        #instructions = 'Nettoyer (C ou c) - Fermer (F ou f)'

        #self.marge_ecran = 8

        #self.calculatrice.addstr(self.marge_ecran - 4, 0, ligne)
        #self.calculatrice.addstr(self.marge_ecran - 2, (self.calculatrice_largeur - 5) - len(instructions), instructions)
        #self.calculatrice.addstr(self.marge_ecran, 0, ligne)

        #pave = ('789/' '456*' '123-' '0.=+')
        #num_pave = len(pave)
        #pave_hauteur = self.calculatrice_hauteur - self.marge_ecran
        #pave_largeur = self.calculatrice_largeur
        #pave_colonnes = 4
        #pave_lignes = num_pave // pave_colonnes

        #for ligne in range(pave_lignes):
        #    for col in range(pave_colonnes):
        #        touches = pave[pave_colonnes * ligne + col]
        #        for touche in touches:
        #            c = ligne * pave_lignes + self.marge_ecran
        #            self.calculatrice.addstr(
        #                c,
        #                col * pave_colonnes, 
        #                str(c)
        #            )
        #            #self.calculatrice.addstr(ligne * pave_lignes, col * pave_colonnes, touche)

        #self.calculatrice.refresh()

    def afficher_resultat(self, key):
        self.calculatrice.addstr(self.marge_ecran - 6, (self.calculatrice_largeur - 4) - len(key), key)
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
