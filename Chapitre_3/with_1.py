#!/usr/bin/env python3
import os

# Nom du fichier
fichier = 'monfichier.txt'

# Écriture
f = open(fichier, 'w')
f.write("J'écris une ligne dans le fichier.\n")
f.write("Puis une autre.\n")
f.close()

# Lecture
f = open(fichier, 'r')
for line in f:
    print(line.strip())
f.close()

# Nettoyage
os.unlink(fichier)
