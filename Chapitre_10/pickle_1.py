#!/usr/bin/env python3
import pickle
from klasse import MaClasse

def main():
    chemin = 'bdd/pickle.db'
    print("Ecriture dans '%s'..." % (chemin))
    with open(chemin, 'wb') as f:
        maClasse = MaClasse(150)
        pickle.dump(maClasse, f)
    print('OK!')

if __name__ == '__main__':
    main()
