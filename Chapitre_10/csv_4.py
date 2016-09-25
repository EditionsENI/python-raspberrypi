#!/usr/bin/env python3
import csv
from csv_3 import enregistrer_dialecte

def main():
    enregistrer_dialecte()
    chemin = 'bdd/dialecte.csv'
    print("Lecture de %s..." % (chemin))
    with open(chemin, 'r') as f:
        reader = csv.reader(f, dialect='pourcent')
        for ligne in reader:
            print(ligne)
    print('OK!')

if __name__ == '__main__':
    main()
