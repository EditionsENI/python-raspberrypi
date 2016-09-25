#!/usr/bin/env python3
class MaRessource:
    def __init__(self):
        print('Dans __init__()')

    def __str__(self):
        return 'Ressource'

    def __enter__(self):
        print('Dans __enter__()')

    def __exit__(self, mon_type, ma_valeur, mon_traceback):
        print('Dans __exit__()')

res = MaRessource()
print('Objet manipulé? ' + str(res))
with res as r:
    print('Dans with')
