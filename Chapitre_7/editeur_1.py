#!/usr/bin/env python3
from tkinter.filedialog   import asksaveasfilename
from tkinter.filedialog   import askopenfilename
from tkinter.simpledialog import askstring
from tkinter.messagebox   import *
from tkinter.scrolledtext import *
from tkinter import *
import os, sys

class PiDiteur(Frame):
    def __init__(self, parent=None, nom_fichier=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.fichier_courant = nom_fichier
        self.nom_editeur = self.__class__.__name__
        self.creer_composants()
        self.gerer_evenements()
        self.afficher_fichier(nom_fichier)

    def creer_composants(self):
        self.creer_zone_texte()
        self.creer_barre_menu()
        self.creer_barre_texte()

    def creer_zone_texte(self):
        self.zone_texte = ScrolledText(
            self,
            padx=5,
            pady=5,
            wrap=WORD,
            relief=SUNKEN,
            font=('courier', 14, 'normal'),
            bg='white',
            fg='black',
            undo=True,
            autoseparators=True,
        )
        self.zone_texte.pack(side=TOP, fill=BOTH, expand=YES)

    def creer_barre_texte(self):
        self.barre_texte = Label(self, relief=SUNKEN, bd=2)
        self.barre_texte.pack(side=BOTTOM, fill=X)

    def creer_barre_menu(self):
        self.barre_menu = Menu(self.master)
        self.master.config(menu=self.barre_menu)
        self.menu_fichier()
        self.menu_editer()

    def menu_fichier(self):
        menu = Menu(self.barre_menu, tearoff=False)
        menu.add_command(label='Ouvrir (Ctrl+o)', command=self.ouvrir)
        menu.add_command(label='Nouveau (Ctrl+n)', command=self.afficher_fichier)
        menu.add_command(label='Enregistrer (Ctrl+s)', command=self.enregistrer)
        menu.add_command(label='Enregistrer sous', command=self.enregistrer_sous)
        menu.add_command(label='Fermer (Alt+F4)', command=self.quitter)
        self.barre_menu.add_cascade(label='Fichier', menu=menu)

    def menu_editer(self):
        menu = Menu(self.barre_menu, tearoff=False)
        menu.add_command(label='Couper (Ctrl+x)', command=lambda: self.copier(True))
        menu.add_command(label='Copier (Ctrl+c)', command=self.copier)
        menu.add_command(label='Coller (Ctrl+v)', command=self.coller)
        menu.add_command(label='Chercher (Ctrl+f)', command=self.chercher)
        self.barre_menu.add_cascade(label='Edition', menu=menu)

    def gerer_evenements(self):
        self.master.bind('<Control-Key-f>', lambda ev: self.chercher())
        self.master.bind('<Control-Key-o>', lambda ev: self.ouvrir())
        self.master.bind('<Control-Key-s>', lambda ev: self.enregistrer())
        self.master.bind('<Control-Key-n>', lambda ev: self.afficher_fichier())
        self.master.protocol("WM_DELETE_WINDOW", self.quitter)

    def afficher_fichier(self, nom_fichier=None):
        if nom_fichier:
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                texte = f.read()
            self.barre_texte.config(text=nom_fichier)
            self.master.title('%s - %s' % (self.nom_editeur, nom_fichier))
        else:
            texte = ''
            nouveau = 'Nouveau fichier'
            self.barre_texte.config(text=nouveau)
            self.master.title('%s - %s' % (self.nom_editeur, nouveau))
        self.fichier_courant = nom_fichier
        self.zone_texte.delete('0.0', END)
        self.zone_texte.insert('0.0', texte)
        self.zone_texte.mark_set(INSERT, '0.0')
        self.zone_texte.focus()
        self.update()

    def ouvrir(self):
        fichier = askopenfilename()
        if fichier:
            self.afficher_fichier(nom_fichier=fichier)

    def enregistrer(self):
        if not self.fichier_courant:
            fichier = asksaveasfilename()
            if fichier:
                self.fichier_courant = fichier
            else:
                return
        fichier = self.fichier_courant
        texte = self.zone_texte.get('0.0', END)
        with open(fichier, 'w', encoding='utf-8') as f:
            f.write(texte)
        self.barre_texte.config(text=fichier)
        self.master.title('%s - %s' % (self.nom_editeur, fichier))

    def enregistrer_sous(self):
        fichier = asksaveasfilename()
        if fichier:
            self.fichier_courant = fichier
            self.enregistrer()

    def copier(self, couper=False):
        try:
            texte = self.zone_texte.get(SEL_FIRST, SEL_LAST)
        except TclError:
            showinfo(message='Selectionnez du texte à copier !')
            return
        if couper: self.zone_texte.delete(SEL_FIRST, SEL_LAST)
        self.clipboard_clear()
        self.clipboard_append(texte)

    def coller(self):
        try:
            texte = self.selection_get(selection='CLIPBOARD')
            self.zone_texte.insert(INSERT, texte)
        except TclError:
            pass

    def chercher(self):
        caractere = askstring('Recherche', 'Tapez votre chaîne de caractères :')
        if caractere:
            trouve = self.zone_texte.search(caractere, INSERT, END)
            if trouve:
                aprestrouve = trouve + ('+%dc' % len(caractere))
                self.zone_texte.tag_add(SEL, trouve, aprestrouve)
                self.zone_texte.mark_set(INSERT, aprestrouve)
                self.zone_texte.see(INSERT)
                self.zone_texte.focus()

    def quitter(self):
        if askyesno('Confirmation',
                'Voulez-vous vraiment fermer {0} ?'.format(self.nom_editeur)):
            Frame.quit(self)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fichier = sys.argv[1]
        if not os.path.isfile(fichier):
            print("Le fichier \"{f}\" n'existe pas!".format(f=fichier))
            sys.exit(1)
        PiDiteur(nom_fichier=fichier).mainloop()
    else:
        PiDiteur().mainloop()
