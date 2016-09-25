#!/usr/bin/env python3
import pickle

def main():
    chemin = 'bdd/pickle.db'
    print("Lecture de '%s'..." % (chemin))
    with open(chemin, 'rb') as f:
        obj = pickle.load(f)
    print("Type de l'objet: %s" % (type(obj)))
    print("__str__ sur l'objet: %s" % (obj))

if __name__ == '__main__':
    main()
