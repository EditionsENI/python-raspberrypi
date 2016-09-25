#!/usr/bin/env python3
import tkinter
from tkinter import *
fenetre = tkinter.Tk()
fenetre.geometry('300x150')
label1 = Label(fenetre, text='Hello world')
label1.grid(row=0, column=0)
label2 = Label(fenetre, text='avec tkinter!')
label2.grid(row=1, column=0)
fenetre.mainloop()
