#!/usr/bin/env python3
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter import *
import alsaaudio, wave, threading

class PiAudio(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.nom_carte = 'sysdefault:CARD=U0x46d0x825'
        self.fichier_courant = None
        self.stop_thread = False
        self.options_fichier = {'filetypes': [('Fichiers .wav', '.wav')]}
        self.creer_composant()
        self.mainloop()

    def creer_composant(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame_haut = Frame(self)
        self.frame_haut.grid(row=0)
        self.frame_bas = Frame(self)
        self.frame_bas.grid(row=1)
        self.bouton_ouvrir = Button(self.frame_haut,
                text='Lire\nun enregistrement',
                command=lambda: self.ouvrir())
        self.bouton_ouvrir.grid(row=0, column=0)
        self.bouton_enreg_sous = Button(self.frame_haut,
                text='Enregistrer\ndu son',
                command=lambda: self.enregistrer_sous())
        self.bouton_enreg_sous.grid(row=0, column=1)
        self.lire_image = PhotoImage(file='resources/lire.png'),
        self.bouton_lire = Button(self.frame_bas,
                image=self.lire_image,
                command=lambda: self.lire())
        self.bouton_lire.grid(row=1, column=0)
        self.bouton_lire.configure(state='disabled')
        self.stop_image = PhotoImage(file='resources/stop.png'),
        self.bouton_stop = Button(self.frame_bas,
                image=self.stop_image,
                command=lambda: self.stop())
        self.bouton_stop.grid(row=1, column=1)
        self.bouton_stop.configure(state='disabled')
        self.enreg_image = PhotoImage(file='resources/enreg.png'),
        self.bouton_enreg = Button(self.frame_bas,
                image=self.enreg_image,
                command=lambda: self.enregistrer())
        self.bouton_enreg.grid(row=1, column=2)
        self.bouton_enreg.configure(state='disabled')
        self.title(self.__class__.__name__)

    def ouvrir(self):
        fichier = askopenfilename(**self.options_fichier)
        if fichier:
            self.fichier_courant = fichier
            self.bouton_lire.configure(state='active')
            self.bouton_stop.configure(state='active')
            self.bouton_enreg.configure(state='disabled')

    def enregistrer_sous(self):
        fichier = asksaveasfilename(**self.options_fichier)
        if fichier:
            self.fichier_courant = fichier
            self.bouton_lire.configure(state='disabled')
            self.bouton_stop.configure(state='active')
            self.bouton_enreg.configure(state='active')

    def lire(self):
        self.stop_thread = False
        t = threading.Thread(target=self._lire)
        t.start()

    def _lire(self):
        with wave.open(self.fichier_courant, 'rb') as w:
            output = alsaaudio.PCM()
            output.setchannels(w.getnchannels())
            output.setrate(w.getframerate())
            output.setformat(alsaaudio.PCM_FORMAT_S16_LE)
            output.setperiodsize(1024)
            self.stop_thread = False
            while True:
                data = w.readframes(320)
                if not data or self.stop_thread: break
                output.write(data)

    def stop(self):
        self.stop_thread = True
        self.bouton_lire.configure(state='active')
        self.bouton_enreg.configure(state='active')

    def enregistrer(self):
        self.stop_thread = False
        self.bouton_lire.configure(state='disabled')
        self.bouton_enreg.configure(state='disabled')
        t = threading.Thread(target=self._enregistrer)
        t.start()

    def _enregistrer(self):
        entree = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, self.nom_carte)
        entree.setchannels(1)
        entree.setrate(44100)
        entree.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        entree.setperiodsize(1024)
        with wave.open(self.fichier_courant, 'w') as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(44100)
            while True:
                _, data = entree.read()
                w.writeframes(data)
                if self.stop_thread: break

if __name__ == '__main__':
    PiAudio()
