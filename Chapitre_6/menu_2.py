#!/usr/bin/env python3
import curses

class MenuPi:
    def __init__(self, screen):
        self.ecran = screen
        self.ecran_hauteur, self.ecran_largeur = self.ecran.getmaxyx()
        self.nom_menu = self.__class__.__name__
        self.ecran.keypad(1)
        self.scanner_choix()

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

    def scanner_choix(self):
        while True:
            self.afficher_options()
            touche = self.ecran.getkey()
            if touche == 'f':
                curses.endwin()
                print("Merci d'avoir utilisé {menu} !".format(menu=self.nom_menu))
                break
            if touche == '1':
                self.prenom_nom()
            if touche == '2':
                self.date_du_jour()
            if touche == '3':
                self.stats_disques()
            if touche == '4':
                self.stats_memoire()
            if touche == '5':
                self.utilisateur_courant()

    def afficher_message(self, message):
        self.ecran.clear()
        self.ecran.addstr(
            int(self.ecran_hauteur / 2),
            int(self.ecran_largeur / 2) - int(len(message) / 2),
            message
        )
        self.ecran.getch()

    def prenom_nom(self):
        curses.endwin()
        prenom = input('Quel est votre prénom ? ')
        nom = input('Quel est votre nom ? ')
        prenom_nom = '{p} {n}'.format(n=nom.strip(), p=prenom.strip())
        msg = 'Bonjour {pn} !'.format(pn=prenom_nom)
        self.afficher_message(msg)

    def date_du_jour(self):
        import datetime
        format = '%a %b %d %H:%M:%S %Y'
        date = datetime.datetime.today().strftime(format)
        date = 'Date du jour: {d}'.format(d=date)
        self.afficher_message(date)

    def stats_disques(self):
        import os
        curses.endwin()
        os.system('clear')
        os.system('df -h /')
        print()
        input('Appuyez sur Entrée')

    def stats_memoire(self):
        self.meminfo = {}
        if len(self.meminfo) == 0:
            with open('/proc/meminfo') as f:
                for line in f:
                    line = line.strip()
                    key, value = line.split(':')
                    self.meminfo[key] = value.strip()
        mem = 'Memoire totale du Raspberry Pi: {m}'.format(
            m=self.meminfo['MemTotal']
        )
        self.afficher_message(mem)
        mem = 'Memoire disponible actuellement sur le Raspberry Pi: {m}'.format(
            m=self.meminfo['MemFree']
        )
        self.afficher_message(mem)

    def utilisateur_courant(self):
        import os, pwd
        info_usr = pwd.getpwuid(os.getuid())
        msg = 'Utilisateur courant: {u}'.format(u=info_usr.pw_name)
        self.afficher_message(msg)

if __name__ == '__main__':
    curses.wrapper(MenuPi)
