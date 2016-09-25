#!/usr/bin/env python3
import csv
from csv_1 import generer_donnees

def enregistrer_dialecte():
    csv.register_dialect('pourcent', delimiter='%')

def main():
    enregistrer_dialecte()
    chemin = 'bdd/dialecte.csv'
    print("Ecriture dans le fichier '%s'..." % (chemin))
    with open(chemin, 'w') as f:
        writer = csv.writer(f, dialect='pourcent')
        for ligne in generer_donnees():
            writer.writerow(ligne)
    print('OK!')

if __name__ == '__main__':
    main()
