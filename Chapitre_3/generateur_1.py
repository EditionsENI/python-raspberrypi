#!/usr/bin/env python3
def fois_deux(ma_liste):
    liste = []
    for element in ma_liste:
        liste.append(element * 2)
    return liste

liste = [5, 10, 50, 100]
print('Avant fois_deux(): {0}'.format(liste))
nliste = fois_deux(liste)
print('Apres fois_deux(): {0}'.format(nliste))
