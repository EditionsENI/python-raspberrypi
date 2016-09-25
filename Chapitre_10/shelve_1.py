#!/usr/bin/env python3
import shelve
from klasse import MaClasse

def main():
    chemin = 'bdd/shelve.db'
    print("Ecriture dans '%s'..." % (chemin))
    bdd = shelve.open(chemin, 'n')
    for i in (90, 150, 300):
        bdd[str(i)] = MaClasse(i)
    bdd['dict'] = {
        'fruits': ['abricot', 'fraise', 'banane'],
        'legumes': ['carotte', 'salade', 'maïs']
    }
    bdd['liste'] = list(range(1, 11))
    bdd['str'] = 'Vive shelve!'
    bdd.close()
    print('OK!')

if __name__ == '__main__':
    main()
