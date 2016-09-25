#!/usr/bin/env python3

fichier = 'pasla.txt'
print("J'essaye d'ouvrir '{0}' ...".format(fichier))

try:
    open(fichier)
except (FileNotFoundError, OSError) as e:
    print("Le fichier n'existe pas!")
    print("ou il y a eut une erreur système!")
    print("Nom de l'exception: {0}".format(e))
except Exception:
    print("Une exception s'est produite!")
