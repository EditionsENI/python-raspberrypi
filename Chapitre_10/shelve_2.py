#!/usr/bin/env python3
import shelve


def main():
    chemin = 'bdd/shelve.db'
    print("Lecture de '%s'..." % (chemin))
    bdd = shelve.open(chemin)
    print('Objets stockés: Clé => Valeur')
    for cle, valeur in bdd.items():
        print('%s => %s' % (cle, valeur))
    print(bdd['str'])
    bdd.close()

if __name__ == '__main__':
    main()
