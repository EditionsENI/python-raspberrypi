#!/usr/bin/env python3
import tkinter
from tkinter import *
fenetre = tkinter.Tk()
fenetre.geometry('300x150')
label = Label(fenetre, text='Hello world avec tkinter!', fg='red', bg='blue')
label.pack(expand=YES, fill=BOTH)
bouton = Button(fenetre, text='Fermer', command=fenetre.destroy)
bouton.pack(side=BOTTOM)
fenetre.mainloop()
