#!/usr/bin/env python3
import csv

def main():
    chemin = 'bdd/fichier.csv'
    print("Lecture de '%s'..." % (chemin))
    with open(chemin, 'r') as f:
        reader = csv.reader(f)
        for ligne in reader:
            print('## Ligne courante: %s' % (ligne))
            print('# 3ème colonne: %s' % (ligne[2]))
    print('OK!')

if __name__ == '__main__':
    main()
