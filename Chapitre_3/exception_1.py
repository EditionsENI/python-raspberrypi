#!/usr/bin/env python3

fichier = 'pasla.txt'
print("J'essaye d'ouvrir '{0}' ...".format(fichier))

try:
    open(fichier)
except Exception:
    print("Une exception s'est produite!")
