#!/usr/bin/env python3
ma_liste = [1, 2, 3]
indice = 2

try:
    ma_valeur = ma_liste[indice]
except IndexError:
    print("Cet indice n'est pas disponible!")
else:
    print("Valeur à l'indice {0}: {1}".format(indice, ma_valeur))
