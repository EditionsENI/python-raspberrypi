#!/usr/bin/env python3
import tkinter
from tkinter import *
fenetre = Tk()
fenetre_x = 400
fenetre_y = 300
placement_x = (fenetre.winfo_screenwidth() - fenetre_x) // 2
placement_y = (fenetre.winfo_screenheight() - fenetre_y) // 2
dimensions = '{f_x}x{f_y}+{p_x}+{p_y}'.format(
    f_x=fenetre_x,
    f_y=fenetre_y,
    p_x=placement_x,
    p_y=placement_y
)
fenetre.geometry(dimensions)
fenetre.mainloop()
