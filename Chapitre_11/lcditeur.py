#!/usr/bin/env python3
from tkinter.messagebox import *
from lcd16x2 import LCD16x2
from tkinter import *

class LCDiteur(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.nom_editeur = self.__class__.__name__
        self.creer_composants()
        self.lcd = LCD16x2()

    def creer_composants(self):
        self.zone_texte = Text(
            self,
            padx=5,
            pady=5,
            wrap=WORD,
            relief=SUNKEN,
            width=20,
            height=5,
            bg='white',
            fg='black',
            undo=True,
            autoseparators=True,
            font=('courier', 14, 'normal')
        )
        self.zone_texte.pack(side=LEFT, fill=BOTH, expand=YES)
        self.bouton_frame = Frame(self, padx=25, pady=25)
        self.bouton_frame.pack(side=RIGHT, fill=BOTH)
        self.bouton_envoyer = Button(self.bouton_frame, command=lambda: self.envoyer_message(), text='Envoyer le message')
        self.bouton_envoyer.pack(fill=BOTH)
        self.bouton_effacer = Button(self.bouton_frame, command=lambda: self.effacer(), text='Effacer')
        self.bouton_effacer.pack(fill=BOTH)
        self.zone_texte.focus()
        self.master.title('%s' % (self.nom_editeur))
        self.master.protocol('WM_DELETE_WINDOW', self.quitter)

    def envoyer_message(self):
        message = self.zone_texte.get('0.0', END).strip()
        if not self.verifier_taille_message(message):
            return
        if message.find('\n') > 0:
            haut, bas = message.split('\n')
            message = '{}\n\r{}'.format(haut, bas)
        self.lcd.clear()
        self.lcd.write_string(message)

    def verifier_taille_message(self, message):
        message = message.split('\n')
        if len(message) > 2:
            showerror(message='Le message ne peut excéder deux lignes !')
            return False
        for ligne in message:
            if len(ligne) > 16:
                showerror(message="La ligne '%s' excède 16 caractères !" % (ligne))
                return False
        return True

    def effacer(self):
        self.zone_texte.delete('0.0', END)
        self.lcd.clear()
        self.lcd.write_string('')

    def quitter(self):
        if askyesno('Confirmation',
                    'Voulez-vous vraiment fermer {0} ?'.format(self.nom_editeur)):
            self.lcd.nettoyer()
            Frame.quit(self)

if __name__ == '__main__':
    LCDiteur().mainloop()
