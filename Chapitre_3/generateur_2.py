#!/usr/bin/env python3
def fois_deux(ma_liste):
    liste = []
    for element in ma_liste:
        yield element * 2

liste = [5, 10, 50, 100]
print('Avant fois_deux(): {0}'.format(liste))
ngen = fois_deux(liste)
print('Générateur: {0}'.format(ngen))
print('Élement: {0}'.format(next(ngen)))
print('Élement: {0}'.format(next(ngen)))
print('Élement: {0}'.format(next(ngen)))
print('Élement: {0}'.format(next(ngen)))
print('Élement: {0}'.format(next(ngen)))
