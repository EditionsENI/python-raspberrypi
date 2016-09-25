#!/usr/bin/env python3
import csv

def generer_donnees():
    return (
        ('Code', 'Nom', 'Quantité'),
        ('HP03', 'Imprimante HP', '3'),
        ('RP04', 'Raspberry Pi 1 version B+', '4'),
        ('IB02', 'Souris IBM', '2')
    )

def main():
    chemin = 'bdd/fichier.csv'
    print("Ecriture dans le fichier '%s'..." % (chemin))
    with open(chemin, 'w') as f:
        writer = csv.writer(f)
        for ligne in generer_donnees():
            writer.writerow(ligne)
    print('OK!')

if __name__ == '__main__':
    main()
