#!/usr/bin/env python3
import tkinter as tk
from tkinter import *

class HelloWorldTkinter(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, master=None, padx=25, pady=25, background='white')
        self.pack(expand=YES)
        self.creer_champs_texte()
        self.creer_bouton_fermer()

    def creer_champs_texte(self):
        self.label_un = tk.Label(self, text='Hello world', fg='red', bg='blue')
        self.label_un.pack(fill=BOTH)
        self.label_deux = tk.Label(self, text='avec tkinter!', fg='blue', bg='red')
        self.label_deux.pack(fill=BOTH)

    def creer_bouton_fermer(self):
        self.bouton_fermer = tk.Button(self, text='Fermer', command=self.quit)
        self.bouton_fermer.pack()

hello = HelloWorldTkinter()
hello.master.geometry('300x150')
hello.master.title('Titre fenetre: Hello!')
hello.mainloop()
